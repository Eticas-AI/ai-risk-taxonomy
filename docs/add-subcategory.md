# How to add a new subcategory

A subcategory is a specific type of risk under an existing category — for example, "Hallucination" under "Reliability" or "Prompt injection" under "Security & Misuse".

## Step 1: Open the taxonomy file

Go to: [src/taxonomy.yaml](https://github.com/Eticas-Foundation/ai-risk-taxonomy/blob/main/src/taxonomy.yaml)

Click the **pencil icon** (top right of the file view) to edit.

GitHub may show a message about creating a branch. This is normal — it means your changes will be reviewed before going live.

## Step 2: Find where to add your entry

Scroll to the category your subcategory belongs under. Categories are marked with comments like:

```
# ============================================================
# 1. BIAS & FAIRNESS
# ============================================================
```

Find the **last subcategory** under that category. You'll add your new entry right after it, before the next category's comment block.

## Step 3: Copy and paste this template

Copy the block below and paste it after the last subcategory. Then replace everything in CAPS with your content:

```yaml
  - id: YOUR-ID-HERE
    type: subcategory
    broader: PARENT-CATEGORY-ID
    label: "YOUR LABEL HERE"
    definition: >
      YOUR DEFINITION HERE. This can be multiple sentences.
      Keep the indentation (6 spaces before the text).
    scope: ALL
    lifecycle_stages: [post-processing]
```

### How to fill in each field

**`id`** — A short identifier using lowercase letters and hyphens. No spaces, no special characters.
- Good: `automation-bias`, `data-drift`, `model-card-gaps`
- Bad: `Automation Bias`, `data_drift`, `model card gaps`

**`broader`** — The `id` of the parent category. Copy it exactly from [the list of valid category ids](editing-guide.md#parent-category-ids).

**`label`** — The human-readable name. Always wrap in double quotes.
- Example: `"Automation bias"`

**`definition`** — A clear description of the risk. Write `>` after `definition:`, then start your text on the next line, indented with 6 spaces. You can write multiple sentences across multiple lines — just keep the same indentation.

```yaml
    definition: >
      The tendency of humans to over-rely on automated outputs,
      accepting AI recommendations without sufficient scrutiny.
      This can lead to missed errors and reduced human judgment.
```

**`scope`** — Who this applies to: `ALL` (both ADM and LLM systems), `ADM` (only traditional ML/decision systems), or `LLM` (only language model systems).

**`lifecycle_stages`** — When this risk manifests. Use square brackets with any combination of: `pre-processing`, `in-processing`, `post-processing`.
- Example: `[pre-processing, post-processing]`

### Optional fields

You can also add these if relevant:

```yaml
    alt_labels:
      - "Alternative name"
      - "Another name"
    source: HRA
```

## Step 4: Commit your change

Scroll to the bottom. In the "Commit changes" section:

1. Write a short description: `Add automation-bias subcategory under Bias & Fairness`
2. Select **"Create a new branch for this commit and start a pull request"**
3. Click **"Propose changes"**

## Step 5: Open the pull request

GitHub takes you to a "Open a pull request" page. Add any context about why you're adding this, then click **"Create pull request"**.

## Step 6: Check the result

Within 30 seconds, a status check appears on the pull request:

- **Green check ✓** — Your YAML is valid. Ask a colleague to review and merge.
- **Red X ✗** — Something is wrong. Click "Details" to see the error message. It will say exactly what's wrong, like:
  - `"automation-bias": Missing required field "definition".`
  - `"automation-bias": broader "bias-fariness" does not match any id in the file. Check for typos.`
  - `YAML syntax error at line 847. This usually means incorrect indentation or a missing quote.`

To fix an error: go to the "Files changed" tab on your pull request, click the pencil icon, make the correction, and commit again. The check re-runs automatically.

## Step 7: Merge

Once the check is green and a colleague approves, click **"Merge pull request"** then **"Confirm merge"**. The system regenerates all pages automatically.

---

[← Back to editing guide](editing-guide.md)
