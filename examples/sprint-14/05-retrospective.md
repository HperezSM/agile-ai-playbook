# Sprint Retrospective: Team Ceiba, Sprint 14

Filled-in copy of the [Retrospective template](../../templates/retrospective-template.md). Part of the [worked example](../README.md).

**Team:** Ceiba
**Sprint:** 14
**Facilitator:** Scrum Master
**Date:** Friday 13 March 2026
**Attendees:** Product Owner, Scrum Master, Backend 1, Backend 2, Frontend 1, Frontend 2, QA

---

## Sprint Goal: Did We Achieve It?

- [ ] Yes, fully
- [x] Partially: patients can move appointments in staging, but the clinic calendar update within one minute is not done, so the pilot did not start
- [ ] No

---

## Start / Stop / Continue

### What should we START doing?

| Item | Votes |
|---|---|
| Ask for a delivery date for every outside dependency during refinement, before Sprint Planning | 6 |
| Escalate any dependency that misses its date by one day, without waiting for the Daily Scrum | 5 |
| Pair the frontend and backend on the API contract on Day 1 | 2 |

### What should we STOP doing?

| Item | Votes |
|---|---|
| Taking items into the sprint whose dependency has no date, and treating that as fine | 5 |
| Using the shared SMS sandbox for every test run | 3 |

### What should we CONTINUE doing?

| Item | Votes |
|---|---|
| Naming the first item to drop at planning (SB-190 went cleanly) | 4 |
| Demoing on a real phone with the clinic in the room | 4 |
| The AI daily brief, with the Scrum Master's review before it is shared | 3 |

---

## Top Themes This Sprint

1. Outside dependencies: the team knew about the webhook on Day 1 but did not push for a date until Day 4.
2. Test environment limits slowed QA (the SMS sandbox).
3. The Sprint Goal helped: dropping SB-190 took one conversation.

---

## Action Items

| Action | Owner | Due Date | Status |
|---|---|---|---|
| Add "outside dependency has a confirmed date" to the team's Definition of Ready | Product Owner | 16 March 2026 | Pending |
| Add an "escalate on" date to every High-impact risk in the RAID log | Scrum Master | 16 March 2026 | Pending |
| Ask the Integrations team to join our refinement once per sprint for items that need them | Scrum Master | 18 March 2026 | Pending |
| Write a mock SMS provider that the test suite uses by default | QA | 20 March 2026 | Pending |

---

## Metric to Track Next Sprint

> One number that tells us if we improved.

**Metric:** Outside dependencies with no confirmed date at the start of the sprint
**Current baseline:** 1 (D-01 in Sprint 14)
**Target:** 0

---

## Facilitator Notes

- The team discussed the Day 4 daily brief, where the AI claimed the Integrations team had confirmed a date. Nobody wants to drop the brief. The team asked that blockers in it always link to the ticket or thread they come from, so anyone can check them in one click.
- The Scrum Master used the [retrospective summary prompt](../../ai-workflows/claude-prompt-library.md#retrospective-prompts) to group the sticky notes into themes, then read the themes back to the team before voting. The team merged two themes the model had kept apart.
- Kept to 60 minutes. No discussion of individual performance.
