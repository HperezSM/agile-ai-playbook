# Sprint Review: Team Ceiba, Sprint 14

Filled-in copy of the [Sprint Review template](../../templates/sprint-review-template.md). Part of the [worked example](../README.md).

**Team:** Ceiba
**Sprint:** 14
**Date:** Friday 13 March 2026
**Attendees:** Scrum Team, pilot clinic manager, head of clinic operations, Integrations team manager

---

## Sprint Goal

> Patients can move their own appointment from the SMS reminder link, without calling the clinic.

**Achieved?** Partially

A patient can open the reminder link, pick a free slot and move the appointment in staging. The clinic calendar picks up the change on its existing 15-minute sync, not within one minute, so the pilot clinic was not switched on.

---

## Delivered This Sprint

| Story / Feature | Points | Demo? | Notes |
|---|---|---|---|
| SB-201 Reschedule page from a signed reminder link | 8 | Yes | Shown on a phone by the pilot clinic manager |
| SB-202 Move-appointment API with a double-booking guard | 5 | Yes | Demo included two people trying to take the same slot |
| SB-204 Reminder SMS includes the reschedule link | 2 | Yes | Template approved by the SMS provider on 6 March |
| SB-205 Audit log entry for every patient change | 3 | No | Shown as a log extract; no screen for it yet |
| SB-198 Bug: reminders an hour early after a time zone change | 3 | No | Fixed on Day 2; no new reports since |

All five meet the team's [Definition of Done](../../templates/definition-of-done-and-ready.md#definition-of-done).

---

## Deferred Items

| Item | Reason for Deferral | Next Sprint? |
|---|---|---|
| SB-203 Push changes to the clinic calendar within one minute | Webhook arrived on Day 7. Code is written but not tested against the clinic calendar, so it does not meet the Definition of Done | Yes |
| SB-190 CSV export for front desks | Dropped on Day 6 to protect the Sprint Goal, as agreed at planning | No, back to the Product Backlog |

SB-203 was not demonstrated. Work that is not done is not shown as finished at the review.

---

## Velocity

| | This Sprint | Last Sprint | 3-Sprint Avg |
|---|---|---|---|
| Committed | 29 | 30 | 30.3 |
| Delivered | 21 | 30 | 25.7 |

The averages cover Sprints 12 to 14, including this one: Sprint 12 committed 32 and delivered 26, Sprint 13 committed 30 and delivered 30. The 29-point average used at planning covered Sprints 11 to 13. Delivered points fell because of one 5-point item blocked from outside the team and one 3-point item dropped on purpose. The team does not treat this as a capacity problem.

---

## Stakeholder Feedback

| Feedback | Source | Action? |
|---|---|---|
| Front desks need a daily email listing the appointments patients moved | Pilot clinic manager | Yes: new item SB-210 |
| The slot picker should show the clinic's address, since some patients book at the wrong clinic | Head of clinic operations | Yes: new item SB-211 |
| Webhook can be enabled in production for one clinic by 18 March | Integrations team manager | Yes: logged as D-03 |
| Could patients cancel from the same link? | Pilot clinic manager | No: Product Owner will decide after the first pilot data |

---

## Backlog Changes Post-Review

- Added SB-210 daily email of patient moves (needed before the pilot starts) and SB-211 clinic address on the slot picker.
- SB-203 moved to the top of the Product Backlog.
- SB-190 CSV export moved below the pilot work.
- "Cancel from the reminder link" written as an idea, not yet refined.

---

## Next Sprint Focus

Sprint 15 finishes what Sprint 14 started. The likely goal is to switch the pilot clinic on with calendar changes visible within one minute and a daily summary email for its front desk. The team will confirm the goal at Sprint Planning on Monday 16 March, once the Integrations team has confirmed the production date in writing.
