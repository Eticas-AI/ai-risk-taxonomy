#!/usr/bin/env python3
"""Validate taxonomy.yaml structure with human-friendly error messages."""

import sys
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

VALID_TYPES = {"category", "subgroup", "subcategory"}
VALID_SCOPES = {"ALL", "ADM", "LLM"}
VALID_MATURITIES = {"established", "emerging"}
VALID_STATUS = {"active", "retired"}
VALID_STAGES = {"pre-processing", "in-processing", "post-processing"}
VALID_RELATIONS = {"exactMatch", "closeMatch", "broadMatch", "narrowMatch", "relatedMatch"}
VALID_PERSPECTIVES = {"rights & ethics", "technical soundness", "governance & compliance", "operational viability"}
VALID_FRAMEWORK_TYPES = {"compliance", "reference", "taxonomy"}

REQUIRED_FIELDS = {"id", "type", "label", "definition"}


def validate_mappings(path):
    """Validate mappings.yaml: framework definitions, type field, required fields."""
    errors = []
    warnings = []
    known_frameworks = set()

    if not path.exists():
        warnings.append(f"{path.name} not found; skipping framework validation.")
        return errors, warnings, known_frameworks

    try:
        with open(path) as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        errors.append(f"YAML syntax error in {path.name}: {e}")
        return errors, warnings, known_frameworks

    if not data or "frameworks" not in data:
        errors.append(f"{path.name} must contain a 'frameworks' key at the top level.")
        return errors, warnings, known_frameworks

    frameworks = data["frameworks"]
    if not isinstance(frameworks, dict):
        errors.append(f"{path.name}: 'frameworks' must be a mapping of framework_id to definition.")
        return errors, warnings, known_frameworks

    for fw_id, fw in frameworks.items():
        prefix = f'Framework "{fw_id}"'
        known_frameworks.add(fw_id)
        if not isinstance(fw, dict):
            errors.append(f"{prefix}: definition must be a mapping.")
            continue
        if "type" not in fw:
            errors.append(f'{prefix}: missing required "type" field. Must be one of {sorted(VALID_FRAMEWORK_TYPES)}.')
        elif fw["type"] not in VALID_FRAMEWORK_TYPES:
            errors.append(
                f'{prefix}: invalid type "{fw["type"]}". Must be one of {sorted(VALID_FRAMEWORK_TYPES)}.'
            )
        if "name" not in fw:
            errors.append(f'{prefix}: missing required "name" field.')
        if "url" not in fw:
            warnings.append(f'{prefix}: missing "url" field (recommended).')

    return errors, warnings, known_frameworks


def validate_taxonomy(path, known_frameworks=None):
    known_frameworks = known_frameworks or set()
    errors = []
    warnings = []

    try:
        with open(path) as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        if hasattr(e, 'problem_mark'):
            line = e.problem_mark.line + 1
            col = e.problem_mark.column + 1
            errors.append(f"YAML syntax error at line {line}, column {col}.\n  Detail: {e.problem}")
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

    for i, concept in enumerate(concepts):
        prefix = f"Entry #{i+1}"
        if not isinstance(concept, dict):
            errors.append(f"{prefix}: Each entry must be a YAML mapping.")
            continue

        cid = concept.get("id")
        if cid:
            prefix = f'"{cid}"'
            if cid in seen_ids:
                errors.append(f'{prefix}: Duplicate id.')
            seen_ids[cid] = i
        else:
            errors.append(f"Entry #{i+1}: Missing 'id' field.")
            continue

        for field in REQUIRED_FIELDS:
            if field not in concept:
                errors.append(f'{prefix}: Missing required field "{field}".')

        ctype = concept.get("type", "")
        if ctype and ctype not in VALID_TYPES:
            errors.append(f'{prefix}: Invalid type "{ctype}". Must be "category", "subgroup", or "subcategory".')

        scope = concept.get("scope", "")
        if scope and scope not in VALID_SCOPES:
            errors.append(f'{prefix}: Invalid scope "{scope}". Must be "ALL", "ADM", or "LLM".')

        maturity = concept.get("maturity", "")
        if maturity and maturity not in VALID_MATURITIES:
            errors.append(f'{prefix}: Invalid maturity "{maturity}". Must be "established" or "emerging".')

        # Status validation (defaults to "active" if not specified)
        status = concept.get("status", "active")
        if status not in VALID_STATUS:
            errors.append(f'{prefix}: Invalid status "{status}". Must be "active" or "retired".')

        # Operationalisation field validation
        operationalisation = concept.get("operationalisation", [])
        if operationalisation:
            if not isinstance(operationalisation, list):
                errors.append(f'{prefix}: operationalisation must be a list.')
            else:
                for j, op in enumerate(operationalisation):
                    if not isinstance(op, dict):
                        errors.append(f'{prefix}: operationalisation #{j+1} must be a key: value block.')
                        continue
                    if "label" not in op:
                        errors.append(f'{prefix}: operationalisation #{j+1} missing "label".')
                    if "description" not in op:
                        errors.append(f'{prefix}: operationalisation #{j+1} missing "description".')

        if ctype == "category":
            if "maturity" not in concept:
                errors.append(f'{prefix}: Categories must have a "maturity" field.')
            perspective = concept.get("perspective", "")
            if perspective and perspective not in VALID_PERSPECTIVES:
                errors.append(f'{prefix}: Invalid perspective "{perspective}".')

        if ctype in ("subgroup", "subcategory"):
            if "broader" not in concept:
                errors.append(f'{prefix}: {ctype.title()}s must have a "broader" field.')
            elif concept["broader"] not in seen_ids:
                all_ids = {c.get("id") for c in concepts}
                if concept["broader"] not in all_ids:
                    errors.append(f'{prefix}: broader "{concept["broader"]}" not found. Check for typos.')

        stages = concept.get("lifecycle_stages", [])
        if stages and isinstance(stages, list):
            for stage in stages:
                if stage not in VALID_STAGES:
                    errors.append(f'{prefix}: Invalid lifecycle stage "{stage}".')

        mappings = concept.get("mappings", [])
        if mappings and isinstance(mappings, list):
            for j, m in enumerate(mappings):
                if not isinstance(m, dict):
                    continue
                fw = m.get("framework")
                if not fw:
                    errors.append(f'{prefix}: mapping #{j+1} missing "framework".')
                elif known_frameworks and fw not in known_frameworks:
                    errors.append(
                        f'{prefix}: mapping #{j+1} references unknown framework "{fw}". '
                        f'Add it to mappings.yaml or fix the typo.'
                    )
                if "target_id" not in m:
                    errors.append(f'{prefix}: mapping #{j+1} missing "target_id".')
                rel = m.get("relation", "")
                if rel and rel not in VALID_RELATIONS:
                    errors.append(f'{prefix}: mapping #{j+1} invalid relation "{rel}".')

        label = concept.get("label", "")
        if isinstance(label, bool):
            errors.append(f'{prefix}: Label interpreted as true/false. Wrap in quotes.')

    return errors, warnings


def main():
    taxonomy_path = SRC / "taxonomy.yaml"
    mappings_path = SRC / "mappings.yaml"

    if not taxonomy_path.exists():
        print(f"ERROR: {taxonomy_path} not found.")
        sys.exit(1)

    all_errors = []
    all_warnings = []

    print(f"Validating {mappings_path}...")
    errs, warns, known_frameworks = validate_mappings(mappings_path)
    all_errors.extend(errs)
    all_warnings.extend(warns)

    print(f"Validating {taxonomy_path}...")
    errs, warns = validate_taxonomy(taxonomy_path, known_frameworks=known_frameworks)
    all_errors.extend(errs)
    all_warnings.extend(warns)

    for w in all_warnings:
        print(f"  WARNING: {w}")
    for e in all_errors:
        print(f"  ERROR: {e}")

    if all_errors:
        print(f"\n✗ Validation FAILED with {len(all_errors)} error(s).")
        sys.exit(1)
    else:
        print(f"✓ Validation PASSED. No errors found.")


if __name__ == "__main__":
    main()
