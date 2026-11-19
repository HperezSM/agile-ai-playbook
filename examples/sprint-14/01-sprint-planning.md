# Sprint Planning: Team Ceiba, Sprint 14

Filled-in copy of the [Sprint Planning template](../../templates/sprint-planning-template.md). Part of the [worked example](../README.md).

**Team:** Ceiba
**Sprint:** 14
**Sprint dates:** Monday 2 March to Friday 13 March 2026
**Facilitator:** Scrum Master
**Attendees:** Product Owner, Scrum Master, Backend 1, Backend 2, Frontend 1, Frontend 2, QA

---

## Capacity

| Team member | Available days | Notes (leave, on-call, training) |
|---|---|---|
| Backend 1 | 10 | |
| Backend 2 | 8 | Leave on 12 and 13 March |
| Frontend 1 | 10 | |
| Frontend 2 | 9 | Accessibility training on 4 March |
| QA | 7 | Support rotation for three days |

**Total available days:** 44
**Recent throughput or velocity (last 3 sprints):** Sprints 11, 12 and 13 delivered 31, 26 and 30 points. Average 29.

---

## 1. Why: Sprint Goal

> One sentence describing the outcome this sprint delivers, not a list of tasks.

**Sprint Goal:** Patients can move their own appointment from the SMS reminder link, without calling the clinic.

**How we will know we reached it:**
- In staging, a test patient opens the reminder link, picks a free slot and the appointment moves.
- The clinic's calendar shows the new time within one minute.
- The pilot clinic is switched on by Friday 13 March.

---

## 2. What: Selected Items

| Item | Estimate | Supports the Sprint Goal? | Dependencies |
|---|---|---|---|
| SB-201 Reschedule page opened from a signed reminder link | 8 | Yes | |
| SB-202 Move-appointment API with a double-booking guard | 5 | Yes | |
| SB-203 Push changes to the clinic calendar within one minute | 5 | Yes | D-01: Integrations team webhook |
| SB-204 Reminder SMS includes the reschedule link | 2 | Yes | D-02: SMS provider template approval |
| SB-205 Audit log entry for every change a patient makes | 3 | Yes | |
| SB-198 Bug: reminders sent an hour early after the clinic's time zone changed | 3 | No | |
| SB-190 Front desk can export the day's bookings as CSV | 3 | No | |

**Total selected:** 29 points
**Compared with capacity:** About right. 29 matches the three-sprint average, and capacity is close to a normal sprint.

The Product Owner kept SB-198 because patients are missing visits. SB-190 is in on the condition that it is the first item dropped if the goal is at risk.

---

## 3. How: First Days Plan

| Item | First tasks | Who starts it |
|---|---|---|
| SB-202 | Data model for a move; lock on the target slot | Backend 1 |
| SB-201 | Page layout and slot picker against a stubbed API | Frontend 1 |
| SB-204 | Draft the new SMS text and submit it to the provider | Frontend 2, with the Product Owner |
| SB-203 | Agree the webhook payload with the Integrations team | Backend 2 |
| SB-198 | Reproduce with a clinic set to a different time zone | QA |

---

## Risks and Dependencies Raised

| Risk / Dependency | Owner | Action before Day 3 |
|---|---|---|
| D-01: the Integrations team has not given a date for the appointment-changed webhook | Backend 2 | Get a date in writing from their queue lead by Day 3 (4 March), when Backend 2 needs the webhook |
| D-02: the SMS provider takes up to five business days to approve a template | Product Owner | Submit the template on Day 1 |
| A-01: the pilot clinic will accept patient moves without phoning to confirm | Product Owner | Ask the clinic manager by 11 March |

All three went into the [RAID log](./03-raid-log.md).

---

## Confirmation

- [x] Sprint Goal read back and agreed by the whole team
- [x] Selected work fits capacity
- [ ] Every item meets the team's [Definition of Ready](../../templates/definition-of-done-and-ready.md#definition-of-ready)
- [x] Dependencies have an owner

SB-203 did not meet the Definition of Ready, because its dependency had no date. The team took it anyway, since the Sprint Goal needs it. That was a reasonable call. The mistake came later: nobody escalated when Day 3 passed without a date.

---

## AI Use in This Event

The Scrum Master used the [Sprint Goal drafting prompt](../../ai-workflows/claude-prompt-library.md#sprint-goal-drafting) before the meeting to get three candidate goals. The team rewrote the best one in the room. The prompt received only the backlog item titles and the average velocity.
