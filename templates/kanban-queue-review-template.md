# Kanban Queue Review Template

A weekly review for teams that run continuous work (service desk, bug triage, request intake). It replaces sprint planning for a Kanban team: look at flow, act on the oldest items, refill the queue, and adjust the policies.

The four flow measures and the Service Level Expectation (SLE) come from the [Kanban Guide (2020)](https://kanbanguides.org/english/). Replenishment and service delivery reviews are cadences from the Kanban Method; this template folds the weekly part of both into one meeting.

**Team:**
**Week of:**
**Facilitator:**
**Attendees:**

Timebox: 30 to 45 minutes.

---

## 1. Flow Since Last Review

Pull these from your board or tool before the meeting. Compare with the last review, not with another team.

| Measure | This week | Last week | Notes |
|---|---|---|---|
| Work in Progress (items started, not finished) | | | |
| Throughput (items finished) | | | |
| Cycle Time, 85th percentile (days) | | | |
| Oldest Work Item Age (days) | | | |

**Service Level Expectation:** 85% of items finish within ___ days.
**Did we meet it this week?** Yes / No

---

## 2. Oldest Items First

List every unfinished item whose age is already past the SLE, or close to it. For each one, decide one action.

| Item | Column | Age (days) | Why it is stuck | Action (swarm, split, unblock, drop) | Owner |
|---|---|---|---|---|---|
| | | | | | |

---

## 3. Blockers and Dependencies

| Blocker or dependency | Item(s) affected | Who can remove it | Owner | By when |
|---|---|---|---|---|
| | | | | |

---

## 4. Replenishment

Pull new work only up to the space the WIP limits leave. Work that is not pulled stays in the options list; it is not a commitment.

**Free slots in the first column:**

| Item pulled | Requested by | Class of service (Standard, Fixed date, Expedite) | Why now |
|---|---|---|---|
| | | | |

**Items left waiting, and the reason:**

---

## 5. Policy and WIP Changes

Change one thing at a time, then check its effect at the next review.

| Change (WIP limit, column policy, entry or exit rule) | Reason from the data above | Review on |
|---|---|---|
| | | |

---

## Checklist

- [ ] Flow measures updated before the meeting
- [ ] Every item past the SLE has an owner and an action
- [ ] New work pulled only into free WIP slots
- [ ] At most one policy change, with a date to check it

**AI assist:** Paste an export of the board (titles, columns, start dates, no personal data) into the [Kanban flow summary prompt](../ai-workflows/claude-prompt-library.md#kanban-flow-summary) to pre-fill sections 1 and 2. Follow the [AI Guardrails](../ai-workflows/ai-guardrails.md) first.
