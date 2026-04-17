# How to add a new subcategory

A subcategory is a specific type of risk under an existing category or sub-group — for example, "Hallucination" under "Reliability > Output quality" or "Prompt injection" under "Security & Misuse > AI-specific attacks".

## Step 1: Open the taxonomy file

Go to: [src/taxonomy.yaml](https://github.com/Eticas-Foundation/ai-risk-taxonomy/blob/main/src/taxonomy.yaml)

Click the **pencil icon** (top right of the file view) to edit.

## Step 2: Find where to add your entry

Find the category or sub-group your subcategory belongs under. Add your new entry after the last subcategory in that group.

## Step 3: Copy and paste this template

```yaml
  - id: YOUR-ID-HERE
    type: subcategory
    broader: PARENT-ID
    maturity: emerging
    label: "YOUR LABEL HERE"
    definition: >
      YOUR DEFINITION HERE. This can be multiple sentences.
      Keep the indentation (6 spaces before the text).
    scope: ALL
    lifecycle_stages: [post-processing]
```

### How to fill in each field

**`id`** — A short identifier using lowercase letters and hyphens. No spaces.
- Good: `automation-bias`, `data-drift`
- Bad: `Automation Bias`, `data_drift`

**`broader`** — The `id` of the parent concept. This can be a category id or a sub-group id. Copy it exactly from the file.

**`maturity`** — New subcategories should be `emerging`. They become `established` after being validated in audits.

**`label`** — The human-readable name. Always wrap in double quotes.

**`definition`** — A clear description. Write `>` after `definition:`, then start your text on the next line, indented with 6 spaces.

**`scope`** — `ALL` (both ADM and LLM), `ADM` (only), or `LLM` (only).

**`lifecycle_stages`** — When this risk manifests: `[pre-processing]`, `[in-processing]`, `[post-processing]`, or a combination.

## Steps 4–7: Commit, PR, check, merge

Same as before — commit on a branch, open a pull request, wait for the green check, then merge.

---

[← Back to editing guide](editing-guide.md)
