# How to add a new category

A category is a top-level risk area — like "Bias & Fairness" or "Reliability". This is uncommon — discuss with the team before adding a new one.

## Step 1: Open the taxonomy file

Go to: [src/taxonomy.yaml](https://github.com/Eticas-Foundation/ai-risk-taxonomy/blob/main/src/taxonomy.yaml)

Click the **pencil icon** to edit.

## Step 2: Scroll to the end of the file

New categories go at the end, after the last existing category block.

## Step 3: Copy and paste this template

```yaml
  - id: your-category-id
    type: category
    label: "Your Category Name"
    alt_labels:
      - "Alternative name if any"
    definition: >
      Your definition here. Describe the risk area clearly.
      This can be multiple sentences.
    scope: ALL
    lifecycle_stages: [pre-processing, in-processing, post-processing]
    maturity: emerging
    perspective: "rights & ethics"
```

### Notes on filling in the fields

**`maturity`** — New categories should be `emerging`. Promotion to `established` is a team decision.

**`perspective`** — Which client concern this addresses. Must be one of: `"rights & ethics"`, `"technical soundness"`, `"governance & compliance"`, or `"operational viability"`. Wrap in quotes.

**No `broader` field** — Categories are top-level concepts.

### Optional: add sub-groups

If your category needs intermediate groupings, add sub-group entries after the category:

```yaml
  - id: your-subgroup-id
    type: subgroup
    broader: your-category-id
    label: "Your Sub-group Name"
    definition: >
      Brief description of what this group covers.
```

Then point subcategories to the sub-group id rather than the category id.

## Steps 4–7: Commit, PR, check, merge

Same process — see [steps 4–7 in the subcategory guide](add-subcategory.md).

---

[← Back to editing guide](editing-guide.md)
