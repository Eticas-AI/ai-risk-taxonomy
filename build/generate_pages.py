#!/usr/bin/env python3
"""Generate Markdown concept pages from taxonomy.yaml."""

import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
RISK_DIR = ROOT / "risk"

RELATION_LABELS = {
    "exactMatch": "exact match",
    "closeMatch": "close match",
    "broadMatch": "broad match",
    "narrowMatch": "narrow match",
    "relatedMatch": "related",
}


def load_yaml(path):
    with open(path) as f:
        return yaml.safe_load(f)


def build_index(concepts):
    """Build lookup structures."""
    by_id = {c["id"]: c for c in concepts}
    children = {}
    for c in concepts:
        if "broader" in c:
            children.setdefault(c["broader"], []).append(c["id"])
    return by_id, children


def generate_concept_page(concept, by_id, children, frameworks, config):
    c = concept
    ns = config["namespace"]
    lines = []

    # YAML front matter
    lines.append("---")
    lines.append(f'layout: concept')
    lines.append(f'title: "{c["label"]}"')
    lines.append(f'id: {c["id"]}')
    lines.append(f'uri: {ns}{c["id"]}')
    lines.append(f'type: {c["type"]}')
    inclusion = c.get("inclusion", "")
    maturity = c.get("maturity", "")
    perspective = c.get("perspective", "")
    if inclusion:
        lines.append(f'inclusion: {inclusion}')
    if maturity:
        lines.append(f'maturity: {maturity}')
    if perspective:
        lines.append(f'perspective: "{perspective}"')
    lines.append(f'scope: {c.get("scope", "ALL")}')
    if "broader" in c:
        lines.append(f'broader: {c["broader"]}')
    lines.append("---")
    lines.append("")

    # Title
    lines.append(f'# {c["label"]}')
    lines.append("")

    # URI
    lines.append(f'`{ns}{c["id"]}`')
    lines.append("")

    # Classification metadata (labelled badges)
    meta_badges = []
    if c["type"] == "category" and inclusion:
        meta_badges.append(f'**Inclusion:** <span class="badge badge-{inclusion}">{inclusion}</span>')
    if maturity:
        meta_badges.append(f'**Maturity:** <span class="badge badge-{maturity}">{maturity}</span>')
    if c["type"] == "category" and perspective:
        meta_badges.append(f'**Perspective:** <span class="badge badge-perspective">{perspective}</span>')
    if meta_badges:
        lines.append(" · ".join(meta_badges))
        lines.append("")

    # Definition
    if "definition" in c:
        lines.append(c["definition"].strip())
        lines.append("")

    # Provisional/proposed notice
    if maturity == "provisional" and c["type"] == "category":
        lines.append("> **This category is provisional.** Definitions may change, subcategories are incomplete, and assessment methods are under development. Findings referencing this category should note its provisional status.")
        lines.append("")
    elif maturity == "provisional" and c["type"] == "subcategory":
        lines.append("> **This subcategory is provisional.** It has not yet been validated in a completed audit.")
        lines.append("")
    elif maturity == "proposed" and c["type"] == "category":
        lines.append("> **This category has been proposed but not yet validated by the team.** It is included to show how it would integrate into the taxonomy. Definitions, subcategories, and scope are subject to discussion.")
        lines.append("")
    elif maturity == "proposed" and c["type"] == "subcategory":
        lines.append("> **This subcategory has been proposed but not yet validated by the team.**")
        lines.append("")

    # Alt labels
    alts = c.get("alt_labels", [])
    if alts:
        lines.append(f'**Also known as:** {" · ".join(alts)}')
        lines.append("")

    # Metadata
    meta = []
    if "scope" in c:
        meta.append(f'**Applies to:** {c["scope"]}')
    stages = c.get("lifecycle_stages", [])
    if stages:
        meta.append(f'**Lifecycle stages:** {", ".join(s.replace("-", " ").title() for s in stages)}')
    if meta:
        lines.append("  \n".join(meta))
        lines.append("")

    # Broader
    if "broader" in c and c["broader"] in by_id:
        parent = by_id[c["broader"]]
        lines.append(f'**Parent category:** [{parent["label"]}]({c["broader"]}.md)')
        lines.append("")

    # Children
    child_ids = children.get(c["id"], [])
    if child_ids:
        lines.append("## Subcategories")
        lines.append("")
        for child_id in child_ids:
            child = by_id[child_id]
            lines.append(f'- [{child["label"]}]({child_id}.md)')
        lines.append("")

    # Notes
    if "note" in c:
        lines.append(f'> {c["note"].strip()}')
        lines.append("")

    # Mappings
    maps = c.get("mappings", [])
    if maps:
        lines.append("## Mappings to external frameworks")
        lines.append("")
        lines.append("| Framework | Concept | Relationship |")
        lines.append("|-----------|---------|-------------|")
        for m in maps:
            fw_id = m["framework"]
            fw = frameworks.get(fw_id, {})
            fw_name = fw.get("name", fw_id)
            fw_url = fw.get("url", "")
            target_label = m.get("target_label", m["target_id"])
            rel = RELATION_LABELS.get(m.get("relation", "closeMatch"), m.get("relation", ""))

            # Framework name links to framework URL
            if fw_url:
                fw_cell = f"[{fw_name}]({fw_url})"
            else:
                fw_cell = fw_name

            # Concept links to concept-level URL if available
            concept_url_prefix = fw.get("concept_url_prefix", "")
            if concept_url_prefix:
                concept_url = concept_url_prefix + m["target_id"]
                concept_cell = f"[{target_label}]({concept_url})"
            else:
                concept_cell = target_label

            lines.append(f"| {fw_cell} | {concept_cell} | {rel} |")
        lines.append("")

    # Source
    if "source" in c:
        lines.append(f'*Source: {c["source"]} project taxonomy*')
        lines.append("")

    return "\n".join(lines)


def generate_index(concepts, by_id, children, config):
    """Generate the index page for the risk/ directory."""
    lines = []
    lines.append("---")
    lines.append("layout: default")
    lines.append(f'title: "{config["title"]}"')
    lines.append("---")
    lines.append("")
    lines.append(f'# {config["title"]}')
    lines.append("")
    lines.append(f'Version {config["version"]}')
    lines.append("")
    lines.append(config["description"].strip())
    lines.append("")

    # Flat list of all categories with badges
    lines.append("## Categories")
    lines.append("")
    cats = [c for c in concepts if c["type"] == "category"]
    for cat in cats:
        inclusion = cat.get("inclusion", "")
        maturity = cat.get("maturity", "")
        perspective = cat.get("perspective", "")

        # Build labelled badge line
        meta_badges = []
        if inclusion:
            meta_badges.append(f'<span class="badge badge-{inclusion}">{inclusion}</span>')
        if maturity:
            meta_badges.append(f'<span class="badge badge-{maturity}">{maturity}</span>')
        if perspective:
            meta_badges.append(f'<span class="badge badge-perspective">{perspective}</span>')
        badge_str = " · ".join(meta_badges)

        lines.append(f'### [{cat["label"]}]({cat["id"]}.md)')
        lines.append("")
        if badge_str:
            lines.append(badge_str)
            lines.append("")
        if "definition" in cat:
            defn = cat["definition"].strip()
            first_sentence = defn.split(". ")[0] + "."
            lines.append(first_sentence)
            lines.append("")

    return "\n".join(lines)


def main():
    config = load_yaml(SRC / "config.yaml")
    taxonomy = load_yaml(SRC / "taxonomy.yaml")
    mappings_def = load_yaml(SRC / "mappings.yaml")
    frameworks = mappings_def.get("frameworks", {})

    concepts = taxonomy["concepts"]
    by_id, children = build_index(concepts)

    RISK_DIR.mkdir(exist_ok=True)

    # Generate individual concept pages
    for concept in concepts:
        page = generate_concept_page(concept, by_id, children, frameworks, config)
        path = RISK_DIR / f'{concept["id"]}.md'
        path.write_text(page)

    # Generate index
    index = generate_index(concepts, by_id, children, config)
    (RISK_DIR / "index.md").write_text(index)

    print(f"Generated {len(concepts)} concept pages + index in {RISK_DIR}/")


if __name__ == "__main__":
    main()
