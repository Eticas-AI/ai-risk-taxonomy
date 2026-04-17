#!/usr/bin/env python3
"""Generate Markdown concept pages from taxonomy.yaml."""

import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
OUT = ROOT / "risk"


def load_yaml(path):
    with open(path) as f:
        return yaml.safe_load(f)


def generate_concept_page(c, by_id, children, config):
    """Generate a Markdown page for a single concept."""
    ns = config["namespace"]
    maturity = c.get("maturity", "")
    lines = []

    # Front matter
    lines.append("---")
    lines.append(f'layout: concept')
    lines.append(f'title: "{c["label"]}"')
    lines.append(f'id: {c["id"]}')
    lines.append(f'uri: {ns}{c["id"]}')
    lines.append(f'type: {c["type"]}')
    if maturity:
        lines.append(f'maturity: {maturity}')
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

    # Maturity badge
    if maturity:
        lines.append(f'**Maturity:** <span class="badge badge-{maturity}">{maturity}</span>')
        lines.append("")

    # Definition
    if "definition" in c:
        lines.append(c["definition"].strip())
        lines.append("")

    # Status notices
    if maturity == "emerging" and c["type"] == "category":
        lines.append("> **This category is emerging.** Assessment methods are still being developed. Definitions and subcategories may evolve.")
        lines.append("")
    elif maturity == "emerging" and c["type"] == "subcategory":
        lines.append("> **This subcategory is emerging.** It has not yet been validated through established assessment methods.")
        lines.append("")

    # Alt labels
    alts = c.get("alt_labels", [])
    if alts:
        lines.append(f'**Also known as:** {" · ".join(alts)}')
        lines.append("")

    # Scope and lifecycle
    scope = c.get("scope", "")
    if scope:
        lines.append(f'**Applies to:** {scope}  ')
    stages = c.get("lifecycle_stages", [])
    if stages:
        stage_str = ", ".join(s.replace("-", " ").title() for s in stages)
        lines.append(f'**Lifecycle stages:** {stage_str}')
    if scope or stages:
        lines.append("")

    # Children: sub-groups with their subcategories, or direct subcategories
    child_ids = children.get(c["id"], [])
    if child_ids:
        # Separate sub-groups from direct subcategories
        subgroups = [by_id[cid] for cid in child_ids if by_id[cid]["type"] == "subgroup"]
        direct_subs = [by_id[cid] for cid in child_ids if by_id[cid]["type"] == "subcategory"]

        if subgroups:
            for sg in subgroups:
                lines.append(f'### {sg["label"]}')
                lines.append("")
                if "definition" in sg:
                    lines.append(sg["definition"].strip())
                    lines.append("")
                sg_children = children.get(sg["id"], [])
                for sc_id in sg_children:
                    sc = by_id[sc_id]
                    lines.append(f'- [{sc["label"]}]({sc_id}.md)')
                lines.append("")

        if direct_subs:
            lines.append("## Subcategories")
            lines.append("")
            for sub in direct_subs:
                lines.append(f'- [{sub["label"]}]({sub["id"]}.md)')
            lines.append("")

    # Mappings
    mappings_cfg = load_yaml(SRC / "mappings.yaml") if (SRC / "mappings.yaml").exists() else {}
    fw_meta = mappings_cfg.get("frameworks", {})
    mappings = c.get("mappings", [])
    if mappings:
        lines.append("## Mappings to external frameworks")
        lines.append("")
        lines.append("| Framework | Concept | Relationship |")
        lines.append("|-----------|---------|-------------|")
        for m in mappings:
            fw_id = m.get("framework", "")
            fw_info = fw_meta.get(fw_id, {})
            fw_name = fw_info.get("name", fw_id)
            fw_url = fw_info.get("url", "")
            target = m.get("target_label", m.get("target_id", ""))
            target_url = m.get("target_url", "")
            rel = m.get("relation", "").replace("Match", " match")

            fw_cell = f'[{fw_name}]({fw_url})' if fw_url else fw_name
            concept_cell = f'[{target}]({target_url})' if target_url else target

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
    lines.append("## Categories")
    lines.append("")

    cats = [c for c in concepts if c["type"] == "category"]
    for cat in cats:
        maturity = cat.get("maturity", "")

        lines.append(f'### [{cat["label"]}]({cat["id"]}.md)')
        lines.append("")
        if maturity:
            lines.append(f'<span class="badge badge-{maturity}">{maturity}</span>')
            lines.append("")
        if "definition" in cat:
            defn = cat["definition"].strip()
            first_sentence = defn.split(". ")[0] + "."
            first_sentence = first_sentence.replace("..", ".")
            lines.append(first_sentence)
            lines.append("")

    return "\n".join(lines)


def main():
    config = load_yaml(SRC / "config.yaml")
    taxonomy = load_yaml(SRC / "taxonomy.yaml")
    concepts = taxonomy["concepts"]

    by_id = {c["id"]: c for c in concepts}
    children = {}
    for c in concepts:
        broader = c.get("broader")
        if broader:
            children.setdefault(broader, []).append(c["id"])

    OUT.mkdir(exist_ok=True)

    # Generate concept pages for all types
    for c in concepts:
        page = generate_concept_page(c, by_id, children, config)
        (OUT / f'{c["id"]}.md').write_text(page)

    # Generate index
    index = generate_index(concepts, by_id, children, config)
    (OUT / "index.md").write_text(index)

    total = len(concepts)
    cats = sum(1 for c in concepts if c["type"] == "category")
    sgs = sum(1 for c in concepts if c["type"] == "subgroup")
    subs = sum(1 for c in concepts if c["type"] == "subcategory")
    print(f"Generated {total} concept pages + index in {OUT}/")
    print(f"  {cats} categories, {sgs} sub-groups, {subs} subcategories")


if __name__ == "__main__":
    main()
