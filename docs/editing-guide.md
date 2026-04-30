# Editing the taxonomy

This guide is for anyone who needs to add or change risk categories, sub-groups, and subcategories. You don't need to install anything — everything is done through the GitHub website.

The key safety feature: **you never edit the live version directly.** You make changes on a copy (a "branch"), the system checks your changes automatically, and someone reviews before they go live. If you make a mistake, nothing breaks.

## How-to guides

- **[Add a new subcategory](add-subcategory.md)** — the most common task. Add a new type of risk under an existing category or sub-group.
- **[Add a new category](add-category.md)** — add a new top-level risk area.
- **[Edit an existing entry](edit-existing.md)** — change a definition, add an alternative name, change the scope.

## Quick reference

### Valid values

| Field | Valid values |
|-------|------------|
| `type` | `category`, `subgroup`, `subcategory` |
| `scope` | `ALL`, `ADM`, `LLM` |
| `maturity` | `established`, `emerging` |
| `status` | `active` (default), `retired` |
| `perspective` | `rights & ethics`, `technical soundness`, `governance & compliance`, `operational viability` |
| `lifecycle_stages` | `pre-processing`, `in-processing`, `post-processing` |
| `mappings[].relation` | `exactMatch`, `closeMatch`, `broadMatch`, `narrowMatch`, `relatedMatch` |
| `mappings[].framework` | Must match a key under `frameworks:` in `src/mappings.yaml` |

The `operationalisation` field is a list of mechanism descriptions attached to a parent risk concept (each entry has `id`, `label`, `description`). Use it when a v0.2 concept needs to be preserved as a method or indicator of a risk rather than as a risk in itself.

The `status: retired` value is used for concepts kept in the YAML for institutional memory but no longer rendered as pages or included in public outputs. A `retirement_note` field is required alongside, explaining where the concept's content went.

### Parent concept ids

**Categories:** `bias-fairness`, `privacy-confidentiality`, `reliability`, `governance`, `security-misuse`, `environmental-impact`, `transparency-explainability`, `autonomy-agency`, `organisational-readiness`

**Sub-groups** (point your subcategory's `broader` to one of these if adding under a sub-group):
See the relevant category page for the full list of sub-group ids.

### The golden rules

1. **Always work on a branch, never edit main directly.** GitHub's "Propose changes" flow does this for you automatically.
2. **Use the templates in the how-to guides.** Copy-paste and replace — don't write from scratch.
3. **Watch the indentation.** Use spaces, not tabs. When in doubt, copy the indentation from the entry above yours.
4. **Wrap labels in quotes.** Always write `label: "Your Label"` with the double quotes.
5. **Check the green/red status** on your pull request before asking someone to merge.
