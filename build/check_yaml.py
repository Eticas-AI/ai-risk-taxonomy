#!/usr/bin/env python3
"""Validate taxonomy.yaml structure with human-friendly error messages.

This runs before the SKOS conversion to catch common editing mistakes
(missing fields, bad indentation, invalid values) and report them
in plain language.
"""

import sys
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

VALID_TYPES = {"category", "subcategory"}
VALID_SCOPES = {"ALL", "ADM", "LLM"}
VALID_INCLUSIONS = {"required", "audit-dependent"}
VALID_MATURITIES = {"established", "developing", "provisional"}
VALID_STAGES = {"pre-processing", "in-processing", "post-processing"}
VALID_RELATIONS = {"exactMatch", "closeMatch", "broadMatch", "narrowMatch", "relatedMatch"}
VALID_PERSPECTIVES = {"rights & ethics", "technical soundness", "governance & compliance", "operational viability"}

REQUIRED_FIELDS = {"id", "type", "label", "definition"}
REQUIRED_CATEGORY_FIELDS = {"inclusion", "maturity"}


def validate_taxonomy(path):
    errors = []
    warnings = []

    # Try to parse the YAML
    try:
        with open(path) as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        # Extract line number if available
        if hasattr(e, 'problem_mark'):
            line = e.problem_mark.line + 1
            col = e.problem_mark.column + 1
            errors.append(
                f"YAML syntax error at line {line}, column {col}.\n"
                f"  This usually means incorrect indentation or a missing quote.\n"
                f"  Detail: {e.problem}"
            )
        else:
            errors.append(f"YAML syntax error: {e}")
        return errors, warnings

    if not data or "concepts" not in data:
        errors.append("The file must contain a 'concepts' list at the top level.")
        return errors, warnings

    concepts = data["concepts"]
    if not isinstance(concepts, list):
        errors.append("'concepts' must be a list of entries (starting with '- id:').")
        return errors, warnings

    seen_ids = {}
    category_ids = set()

    for i, concept in enumerate(concepts):
        prefix = f"Entry #{i+1}"

        if not isinstance(concept, dict):
            errors.append(f"{prefix}: Each entry must be a YAML mapping (key: value pairs). Got something else.")
            continue

        # Check for id first since we use it in messages
        cid = concept.get("id")
        if cid:
            prefix = f'"{cid}"'
            if cid in seen_ids:
                errors.append(f'{prefix}: Duplicate id. This id already appears earlier in the file.')
            seen_ids[cid] = i
        else:
            errors.append(f"Entry #{i+1}: Missing 'id' field. Every entry needs an id.")
            continue

        # Required fields
        for field in REQUIRED_FIELDS:
            if field not in concept:
                errors.append(f'{prefix}: Missing required field "{field}".')

        # Type validation
        ctype = concept.get("type", "")
        if ctype and ctype not in VALID_TYPES:
            errors.append(
                f'{prefix}: Invalid type "{ctype}". Must be "category" or "subcategory".'
            )

        # Scope validation
        scope = concept.get("scope", "")
        if scope and scope not in VALID_SCOPES:
            errors.append(
                f'{prefix}: Invalid scope "{scope}". Must be "ALL", "ADM", or "LLM".'
            )

        # Category-specific fields
        if ctype == "category":
            category_ids.add(cid)
            for field in REQUIRED_CATEGORY_FIELDS:
                if field not in concept:
                    errors.append(f'{prefix}: Categories must have a "{field}" field.')

            inclusion = concept.get("inclusion", "")
            if inclusion and inclusion not in VALID_INCLUSIONS:
                errors.append(
                    f'{prefix}: Invalid inclusion "{inclusion}". '
                    f'Must be "required" or "audit-dependent".'
                )

            maturity = concept.get("maturity", "")
            if maturity and maturity not in VALID_MATURITIES:
                errors.append(
                    f'{prefix}: Invalid maturity "{maturity}". '
                    f'Must be "established", "developing", or "provisional".'
                )

            perspective = concept.get("perspective", "")
            if perspective and perspective not in VALID_PERSPECTIVES:
                errors.append(
                    f'{prefix}: Invalid perspective "{perspective}". '
                    f'Must be one of: {", ".join(sorted(VALID_PERSPECTIVES))}.'
                )

        # Subcategory must have broader
        if ctype == "subcategory":
            if "broader" not in concept:
                errors.append(
                    f'{prefix}: Subcategories must have a "broader" field '
                    f'pointing to their parent category id.'
                )
            elif concept["broader"] not in seen_ids:
                # Check if it appears later
                all_ids = {c.get("id") for c in concepts}
                if concept["broader"] not in all_ids:
                    errors.append(
                        f'{prefix}: broader "{concept["broader"]}" does not match any id '
                        f'in the file. Check for typos.'
                    )

            maturity = concept.get("maturity", "")
            if maturity and maturity not in VALID_MATURITIES:
                errors.append(
                    f'{prefix}: Invalid maturity "{maturity}". '
                    f'Must be "established", "developing", or "provisional".'
                )

        # Lifecycle stages validation
        stages = concept.get("lifecycle_stages", [])
        if stages:
            if not isinstance(stages, list):
                errors.append(
                    f'{prefix}: lifecycle_stages must be a list like '
                    f'[pre-processing, in-processing, post-processing]'
                )
            else:
                for stage in stages:
                    if stage not in VALID_STAGES:
                        errors.append(
                            f'{prefix}: Invalid lifecycle stage "{stage}". '
                            f'Must be one of: pre-processing, in-processing, post-processing.'
                        )

        # Mappings validation
        mappings = concept.get("mappings", [])
        if mappings:
            if not isinstance(mappings, list):
                errors.append(f'{prefix}: mappings must be a list.')
            else:
                for j, m in enumerate(mappings):
                    if not isinstance(m, dict):
                        errors.append(f'{prefix}: mapping #{j+1} must be a key: value block.')
                        continue
                    if "framework" not in m:
                        errors.append(f'{prefix}: mapping #{j+1} is missing "framework".')
                    if "target_id" not in m:
                        errors.append(f'{prefix}: mapping #{j+1} is missing "target_id".')
                    rel = m.get("relation", "")
                    if rel and rel not in VALID_RELATIONS:
                        errors.append(
                            f'{prefix}: mapping #{j+1} has invalid relation "{rel}". '
                            f'Must be one of: {", ".join(VALID_RELATIONS)}.'
                        )

        # Check for common YAML mistakes
        label = concept.get("label", "")
        if isinstance(label, bool):
            errors.append(
                f'{prefix}: The label was interpreted as true/false instead of text. '
                f'Wrap it in quotes: label: "Yes" instead of label: Yes'
            )

        defn = concept.get("definition", "")
        if isinstance(defn, dict):
            errors.append(
                f'{prefix}: The definition looks malformed. '
                f'Make sure the text after "definition: >" is indented with spaces.'
            )

    return errors, warnings


def main():
    path = SRC / "taxonomy.yaml"
    if not path.exists():
        print(f"ERROR: {path} not found.")
        sys.exit(1)

    print(f"Validating {path}...")
    errors, warnings = validate_taxonomy(path)

    for w in warnings:
        print(f"  WARNING: {w}")
    for e in errors:
        print(f"  ERROR: {e}")

    if errors:
        print(f"\n✗ Validation FAILED with {len(errors)} error(s).")
        print("  Fix the errors above and try again.")
        sys.exit(1)
    else:
        print(f"✓ Validation PASSED. No errors found.")


if __name__ == "__main__":
    main()
