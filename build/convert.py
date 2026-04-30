#!/usr/bin/env python3
"""Convert taxonomy.yaml to SKOS Turtle and JSON-LD.

Generates two versions:
- Internal (taxonomy.ttl, taxonomy.jsonld): full taxonomy
- Public (taxonomy-public.ttl, taxonomy-public.jsonld): categories + sub-groups, established only
"""

import yaml
from pathlib import Path
from rdflib import Graph, Namespace, Literal, URIRef
from rdflib.namespace import RDF, RDFS, SKOS, DCTERMS, XSD

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
DIST = ROOT / "dist"


def load_yaml(path):
    with open(path) as f:
        return yaml.safe_load(f)


def is_visible(concept, audience, by_id=None):
    """Should this concept appear in the given audience's view?"""
    if concept.get("status", "active") == "retired":
        return False
    if audience == "internal":
        return True
    if concept.get("type") == "subcategory":
        return False
    if concept.get("maturity") == "emerging":
        return False
    if by_id and "broader" in concept:
        parent = by_id.get(concept["broader"])
        if parent and not is_visible(parent, audience, by_id):
            return False
    return True


def build_graph(config, taxonomy, mappings_def, audience):
    g = Graph()
    ns = Namespace(config["namespace"])
    eticas = Namespace("https://taxonomy.eticas.ai/ontology/")

    g.bind("eticas", ns)
    g.bind("eticas-ont", eticas)
    g.bind("skos", SKOS)
    g.bind("dcterms", DCTERMS)

    # Bind external framework namespaces
    fw_namespaces = {}
    for fw_id, fw in mappings_def.get("frameworks", {}).items():
        fw_ns = Namespace(fw["base_uri"])
        g.bind(fw_id.replace("_", "-"), fw_ns)
        fw_namespaces[fw_id] = fw_ns

    # Build by_id lookup for parent visibility checks
    by_id = {c["id"]: c for c in taxonomy["concepts"]}

    # Create the ConceptScheme
    scheme = ns["scheme"]
    g.add((scheme, RDF.type, SKOS.ConceptScheme))
    g.add((scheme, SKOS.prefLabel, Literal(config["title"], lang="en")))
    g.add((scheme, DCTERMS.description, Literal(config["description"].strip(), lang="en")))
    g.add((scheme, DCTERMS.publisher, Literal(config["publisher"])))
    g.add((scheme, DCTERMS.license, URIRef(config["license"])))
    g.add((scheme, DCTERMS.language, Literal(config["language"])))

    for concept in taxonomy["concepts"]:
        # Filter by audience visibility
        if not is_visible(concept, audience, by_id):
            continue

        cid = concept["id"]
        uri = ns[cid]

        g.add((uri, RDF.type, SKOS.Concept))
        g.add((uri, SKOS.inScheme, scheme))
        g.add((uri, SKOS.prefLabel, Literal(concept["label"], lang="en")))

        if "definition" in concept:
            g.add((uri, SKOS.definition, Literal(concept["definition"].strip(), lang="en")))

        for alt in concept.get("alt_labels", []):
            g.add((uri, SKOS.altLabel, Literal(alt, lang="en")))

        if "note" in concept:
            g.add((uri, SKOS.note, Literal(concept["note"].strip(), lang="en")))

        # Hierarchy
        if concept["type"] == "category":
            g.add((uri, SKOS.topConceptOf, scheme))
            g.add((scheme, SKOS.hasTopConcept, uri))
        elif "broader" in concept:
            g.add((uri, SKOS.broader, ns[concept["broader"]]))
            g.add((ns[concept["broader"]], SKOS.narrower, uri))

        # Custom properties
        if "scope" in concept:
            g.add((uri, eticas.scope, Literal(concept["scope"])))
        if "maturity" in concept:
            g.add((uri, eticas.maturity, Literal(concept["maturity"])))
        if "perspective" in concept:
            g.add((uri, eticas.perspective, Literal(concept["perspective"])))
        if "source" in concept:
            g.add((uri, DCTERMS.source, Literal(concept["source"])))

        for stage in concept.get("lifecycle_stages", []):
            g.add((uri, eticas.lifecycleStage, Literal(stage)))

        # External mappings
        for m in concept.get("mappings", []):
            fw = m["framework"]
            target_id = m["target_id"]
            relation = m.get("relation", "closeMatch")

            if fw in fw_namespaces:
                target_uri = fw_namespaces[fw][target_id]
            else:
                target_uri = URIRef(target_id)

            relation_prop = {
                "exactMatch": SKOS.exactMatch,
                "closeMatch": SKOS.closeMatch,
                "broadMatch": SKOS.broadMatch,
                "narrowMatch": SKOS.narrowMatch,
                "relatedMatch": SKOS.relatedMatch,
            }.get(relation, SKOS.closeMatch)

            g.add((uri, relation_prop, target_uri))

            if "target_label" in m:
                g.add((target_uri, SKOS.prefLabel, Literal(m["target_label"], lang="en")))

    return g


def write_outputs(g, suffix=""):
    ttl_path = DIST / f"taxonomy{suffix}.ttl"
    g.serialize(destination=str(ttl_path), format="turtle")
    print(f"  Written {ttl_path.name} ({len(g)} triples)")

    jsonld_path = DIST / f"taxonomy{suffix}.jsonld"
    g.serialize(destination=str(jsonld_path), format="json-ld", indent=2)
    print(f"  Written {jsonld_path.name}")


def main():
    DIST.mkdir(exist_ok=True)

    config = load_yaml(SRC / "config.yaml")
    taxonomy = load_yaml(SRC / "taxonomy.yaml")
    mappings_def = load_yaml(SRC / "mappings.yaml")

    print("Generating SKOS:")

    # Internal (full)
    g_internal = build_graph(config, taxonomy, mappings_def, "internal")
    write_outputs(g_internal, suffix="")

    # Public (filtered)
    g_public = build_graph(config, taxonomy, mappings_def, "public")
    write_outputs(g_public, suffix="-public")


if __name__ == "__main__":
    main()
