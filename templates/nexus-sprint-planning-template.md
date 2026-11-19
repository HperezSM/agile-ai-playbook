# Nexus Sprint Planning Template

For 3 to 9 Scrum Teams working from one Product Backlog. Fill it in before the teams run their own Sprint Planning, so every cross-team dependency has an owner and a date.

Based on the [Nexus Guide](https://www.scrum.org/resources/online-nexus-guide). Each team then plans with the [Sprint Planning template](./sprint-planning-template.md).

**Nexus:**
**Sprint:**
**Sprint dates:**
**Product Owner:**
**Nexus Integration Team contact:**
**Teams represented:**

---

## Nexus Sprint Goal

> One objective the whole Nexus delivers as a single integrated increment.

**Nexus Sprint Goal:**

**How we will know the increment is integrated (environment, test, demo):**

---

## Work by Team

| Product Backlog item | Team | Supports the Nexus Sprint Goal? | Notes |
|---|---|---|---|
| | | Yes/No | |

---

## Cross-Team Dependencies

One row per dependency. "Needed by" is the sprint day the receiving team must have it; if it falls late in the sprint, consider moving the work to one team instead.

| ID | Item that waits | Waiting team | Item it depends on | Providing team | Needed by (sprint day) | Type (code, API, data, environment, decision) | Resolution (resequence, move to one team, stub, accept risk) | Owner | Status |
|---|---|---|---|---|---|---|---|---|---|
| ND-01 | | | | | | | | | Open |

Status: Open / Agreed / Delivered / At risk.

---

## Integration Plan

| What gets integrated | When (sprint day) | How it is checked | Owner |
|---|---|---|---|
| | | | |

**Shared Definition of Done for the integrated increment:** link it here. See the [Definition of Done and Ready template](./definition-of-done-and-ready.md).

---

## Confirmation

- [ ] Nexus Sprint Goal agreed by the Product Owner and every team
- [ ] Every dependency has a providing team, a date and an owner
- [ ] No dependency is needed in the last two days of the sprint without an agreed fallback
- [ ] Teams leave with the dependencies they must honor in their own Sprint Planning

Track any dependency still open after planning in the [RAID log](./raid-log-template.md#dependencies) and raise it at the Nexus Daily Scrum.

**AI assist:** The [dependency mapping prompt](../ai-workflows/claude-prompt-library.md#dependency-mapping) gives a first draft of the dependency table. Check every row with the teams; the model cannot know what each team has already agreed.
