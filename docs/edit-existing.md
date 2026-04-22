# How to edit an existing entry

Use this guide when you need to change a definition, add an alternative name, change the scope, or make any other modification to an entry that already exists.

## Step 1: Open the taxonomy file

Go to: [src/taxonomy.yaml](https://github.com/Eticas-AI/ai-risk-taxonomy/blob/main/src/taxonomy.yaml)

Click the **pencil icon** to edit.

## Step 2: Find the entry

Use your browser's search (Ctrl+F or Cmd+F) to find the entry by its id or label. For example, search for `hallucination` or `Bias & Fairness`.

## Step 3: Make your change

### Changing a definition

Find the `definition: >` line and edit the text below it. Keep the indentation (6 spaces).

```yaml
    definition: >
      Your updated definition text here.
      Can be multiple lines at the same indentation.
```

### Adding an alternative label

Find the `alt_labels:` section (or add one if it doesn't exist) and add a new line with a dash:

```yaml
    alt_labels:
      - "Existing name"
      - "Your new alternative name"
```

If the entry doesn't have `alt_labels` yet, add it after the `label` line:

```yaml
    label: "Existing Label"
    alt_labels:
      - "New Alternative Name"
```

### Changing the scope

Replace the value after `scope:`. Valid values: `ALL`, `ADM`, `LLM`.

### Adding a lifecycle stage

Edit the list inside the square brackets:

```yaml
    lifecycle_stages: [pre-processing, in-processing, post-processing]
```

### Changing inclusion or maturity (categories only)

```yaml
    inclusion: required           # or: audit-dependent
    maturity: established         # or: developing, provisional
```

These are significant changes — add a note in your pull request explaining why.

## Steps 4–7: Commit, PR, check, merge

Same process as for adding entries — see [steps 4–7 in the subcategory guide](add-subcategory.md#step-4-commit-your-change).

---

[← Back to editing guide](editing-guide.md)
