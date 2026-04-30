#!/usr/bin/env python3
"""Generate Markdown concept pages from taxonomy.yaml.

Generates two versions:
- Public (/risk/): categories + sub-groups, established only, no match types in tables
- Internal (/risk-internal/): full taxonomy with subcategories, all maturities, full mappings
"""

import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
OUT_PUBLIC = ROOT / "risk"
OUT_INTERNAL = ROOT / "risk-internal"


def load_yaml(path):
    with open(path) as f:
        return yaml.safe_load(f)


def is_visible(concept, audience, by_id=None):
    """Should this concept appear in the given audience's view?"""
    # Retired never visible
    if concept.get("status", "active") == "retired":
        return False

    if audience == "internal":
        return True

    # Public filters
    # 1. Only categories and sub-groups (no subcategories)
    if concept.get("type") == "subcategory":
        return False

    # 2. Only established maturity (concepts without maturity inherit from parent)
    if concept.get("maturity") == "emerging":
        return False

    # 3. If parent is not visible, child isn't either (handles sub-groups
    #    whose parent category is emerging or retired)
    if by_id and "broader" in concept:
        parent = by_id.get(concept["broader"])
        if parent and not is_visible(parent, audience, by_id):
            return False

    return True


def generate_concept_page(c, by_id, children, config, audience):
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

    # Children: filter by audience visibility
    child_ids = children.get(c["id"], [])
    if child_ids:
        # Filter children by what's visible to this audience
        visible_children = [by_id[cid] for cid in child_ids if is_visible(by_id[cid], audience, by_id)]
        subgroups = [s for s in visible_children if s["type"] == "subgroup"]
        direct_subs = [s for s in visible_children if s["type"] == "subcategory"]

        if subgroups:
            lines.append("## Risk groups")
            lines.append("")
            for sg in subgroups:
                defn = sg.get("definition", "").strip()
                if defn:
                    lines.append(f'- [{sg["label"]}]({sg["id"]}.md) — {defn}')
                else:
                    lines.append(f'- [{sg["label"]}]({sg["id"]}.md)')
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
        # Public version: no relationship column (no match types)
        if audience == "public":
            lines.append("| Framework | Concept |")
            lines.append("|-----------|---------|")
        else:
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

            if audience == "public":
                lines.append(f"| {fw_cell} | {concept_cell} |")
            else:
                lines.append(f"| {fw_cell} | {concept_cell} | {rel} |")
        lines.append("")

    # References (papers, benchmarks, tools, regulatory sources)
    references = c.get("references", [])
    if references:
        lines.append("## References")
        lines.append("")
        for ref in references:
            label = ref.get("label", "")
            url = ref.get("url", "")
            ref_type = ref.get("type", "")
            domain = ref.get("domain", "")
            note = ref.get("note", "")

            if url:
                line = f'- **[{label}]({url})**'
            else:
                line = f'- **{label}**'

            tags = []
            if ref_type:
                tags.append(ref_type)
            if domain:
                tags.append(f'domain: {domain}')
            if tags:
                line += f' <sub>[{", ".join(tags)}]</sub>'

            lines.append(line)
            if note:
                lines.append(f'  {note}')
        lines.append("")

    # Operationalisation (mechanisms by which the risk manifests) — internal only
    if audience == "internal":
        operationalisation = c.get("operationalisation", [])
        if operationalisation:
            lines.append("## How this risk manifests")
            lines.append("")
            lines.append("The mechanisms below describe *how* this risk arises in practice. They are operationalisation aids, not risks in themselves — useful when designing assessment methods.")
            lines.append("")
            for op in operationalisation:
                label = op.get("label", "")
                description = op.get("description", "").strip()
                lines.append(f'**{label}**  ')
                if description:
                    lines.append(description)
                lines.append("")

    # Source
    if "source" in c:
        lines.append(f'*Source: {c["source"]} project taxonomy*')
        lines.append("")

    return "\n".join(lines)


def generate_index(visible_concepts, by_id, children, config, audience):
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

    if audience == "internal":
        lines.append("> **Internal view** — full taxonomy including subcategories and emerging concepts. The [public version](../risk/) shows only categories and sub-groups, established only.")
        lines.append("")

    lines.append("## Categories")
    lines.append("")

    cats = [c for c in visible_concepts if c["type"] == "category"]
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


def render(audience, out_dir, concepts, by_id, children, config):
    """Render the full site for one audience."""
    out_dir.mkdir(exist_ok=True)

    visible = [c for c in concepts if is_visible(c, audience, by_id)]
    visible_ids = {c["id"] for c in visible}

    # Clean stale pages
    for md_file in out_dir.glob("*.md"):
        if md_file.stem == "index":
            continue
        if md_file.stem not in visible_ids:
            md_file.unlink()

    # Generate concept pages
    for c in visible:
        page = generate_concept_page(c, by_id, children, config, audience)
        (out_dir / f'{c["id"]}.md').write_text(page)

    # Generate index
    index = generate_index(visible, by_id, children, config, audience)
    (out_dir / "index.md").write_text(index)

    cats = sum(1 for c in visible if c["type"] == "category")
    sgs = sum(1 for c in visible if c["type"] == "subgroup")
    subs = sum(1 for c in visible if c["type"] == "subcategory")
    print(f"  [{audience}] {out_dir.name}/: {len(visible)} pages — {cats} categories, {sgs} sub-groups, {subs} subcategories")


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

    print("Generating pages:")
    render("public", OUT_PUBLIC, concepts, by_id, children, config)
    render("internal", OUT_INTERNAL, concepts, by_id, children, config)

    retired = sum(1 for c in concepts if c.get("status") == "retired")
    if retired:
        print(f"  ({retired} concepts retired, not rendered in either version)")


if __name__ == "__main__":
    main()
