# How to add a new category

A category is a top-level risk area — like "Bias & Fairness" or "Reliability". This is less common than adding a subcategory; discuss with the team before adding a new one.

## Step 1: Open the taxonomy file

Go to: [src/taxonomy.yaml](https://github.com/Eticas-Foundation/ai-risk-taxonomy/blob/main/src/taxonomy.yaml)

Click the **pencil icon** to edit.

## Step 2: Scroll to the end of the file

New categories go at the end, after the last existing category block.

## Step 3: Copy and paste this template

```yaml
  # ============================================================
  # YOUR CATEGORY NAME (IN CAPS)
  # ============================================================

  - id: your-category-id
    type: category
    label: "Your Category Name"
    alt_labels:
      - "Alternative name if any"
    definition: >
      Your definition here. Describe the risk area clearly.
      This can be multiple sentences. Keep the indentation
      (6 spaces before the text).
    scope: ALL
    lifecycle_stages: [pre-processing, in-processing, post-processing]
    inclusion: audit-dependent
    maturity: provisional
```

### Notes on filling in the fields

All the same rules as [adding a subcategory](add-subcategory.md#how-to-fill-in-each-field) apply, plus:

**`inclusion`** — Use `audit-dependent` for new categories. Promotion to `required` is a team decision made later.

**`maturity`** — Use `provisional` for new categories. It moves to `developing` and then `established` as the category is used in audits and methods are refined.

**No `broader` field** — Categories are top-level concepts. They don't have a parent.

### Optional: add mappings

If you know the equivalent concept in an external framework, add a mappings section:

```yaml
    mappings:
      - framework: mit
        target_id: "subdomain-X.X"
        target_label: "MIT equivalent concept"
        relation: closeMatch
```

Valid framework ids: `mit`, `nist_600`, `nist_rmf`, `oecd`, `dpv_ai`, `iso_42001`, `eu_ai_act`, `airo`, `vair`

You can also skip mappings and add them later — they're not required for the validation to pass.

## Steps 4–7: Commit, PR, check, merge

Same as for subcategories — see [steps 4–7 in the subcategory guide](add-subcategory.md#step-4-commit-your-change).

---

[← Back to editing guide](editing-guide.md)
