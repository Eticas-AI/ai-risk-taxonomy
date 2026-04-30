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

REQUIRED_FIELDS = {"id", "type", "label", "definition"}


def validate_taxonomy(path):
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
                if "framework" not in m:
                    errors.append(f'{prefix}: mapping #{j+1} missing "framework".')
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
        sys.exit(1)
    else:
        print(f"✓ Validation PASSED. No errors found.")


if __name__ == "__main__":
    main()
