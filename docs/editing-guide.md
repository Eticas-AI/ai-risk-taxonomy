# Editing the taxonomy

This guide is for anyone who needs to add or change risk categories and subcategories. You don't need to install anything — everything is done through the GitHub website.

The key safety feature: **you never edit the live version directly.** You make changes on a copy (a "branch"), the system checks your changes automatically, and someone reviews before they go live. If you make a mistake, nothing breaks.

## How-to guides

- **[Add a new subcategory](add-subcategory.md)** — the most common task. Add a new type of risk under an existing category.
- **[Add a new category](add-category.md)** — add a new top-level risk area.
- **[Edit an existing entry](edit-existing.md)** — change a definition, add an alternative name, change the scope.

## Quick reference

### Valid values

| Field | Valid values |
|-------|------------|
| `type` | `category`, `subcategory` |
| `scope` | `ALL`, `ADM`, `LLM` |
| `inclusion` | `required`, `audit-dependent` |
| `maturity` | `established`, `developing`, `provisional` |
| `perspective` | `rights & ethics`, `technical soundness`, `governance & compliance`, `operational viability` |
| `lifecycle_stages` | `pre-processing`, `in-processing`, `post-processing` |

### Parent category ids

`bias-fairness`, `privacy-confidentiality`, `reliability`, `governance`, `security-misuse`, `environmental-impact`, `transparency-explainability`, `responsibility-redress`, `autonomy`, `agentic-risks`, `manipulation-misinformation`

### The golden rules

1. **Always work on a branch, never edit main directly.** GitHub's "Propose changes" flow does this for you automatically.
2. **Use the templates in the how-to guides.** Copy-paste and replace — don't write from scratch.
3. **Watch the indentation.** Use spaces, not tabs. When in doubt, copy the indentation from the entry above yours.
4. **Wrap labels in quotes.** Always write `label: "Your Label"` with the double quotes.
5. **Check the green/red status** on your pull request before asking someone to merge.
