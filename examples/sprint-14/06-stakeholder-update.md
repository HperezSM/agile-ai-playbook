# Stakeholder Update: Sonrisa Booking, Sprint 14

Filled-in copy of the [Stakeholder Update template](../../templates/stakeholder-update-template.md), sent on Friday 13 March 2026 after the Sprint Review. Part of the [worked example](../README.md).

**Project / Product:** Sonrisa Booking, patient self-reschedule
**Period covered:** Sprint 14, 2 to 13 March 2026
**Author:** Scrum Master
**Overall status:** 🟡 At risk

---

## Executive Summary

> Three sentences at most: where we are, what changed since last update, and what you need from the reader.

Patients can now move their own appointment from the SMS reminder in staging, but the pilot clinic did not go live this sprint because the clinic calendar update depends on a webhook that arrived six days late. We plan to switch the pilot on by 27 March. We need the Integrations team to confirm in writing that the webhook will be live in production by 18 March.

---

## Delivered

| Item | Outcome for users or the business |
|---|---|
| Reschedule page from the reminder link | Patients can pick a new slot on their phone without calling |
| Double-booking guard | Two people cannot take the same slot, even while the calendar sync lags |
| Reminder SMS with the reschedule link | Provider approved the new message; ready to send |
| Audit log of patient changes | Every patient move is traceable, which clinic operations asked for before the pilot |
| Time zone fix for reminders | Reminders go out at the right hour again; no new reports since the fix |

---

## Deferred or Slipped

| Item | Why | New target |
|---|---|---|
| Clinic calendar updated within one minute | The Integrations team's webhook arrived on 10 March instead of 4 March | Sprint 15 (ends 27 March) |
| Pilot clinic switched on | Waits for the calendar update and a daily summary email the clinic asked for | 27 March |
| CSV export for front desks | Dropped to protect the reschedule work | Back in the backlog, below the pilot |

---

## Next Period Focus

1. Calendar changes visible to the clinic within one minute.
2. A daily email to the pilot clinic's front desk listing patient moves.
3. Switch the pilot clinic on and start measuring reschedule calls.

---

## Risks and Issues

| Risk / Issue | Impact (H/M/L) | Mitigation | Owner |
|---|---|---|---|
| Production webhook not ready by 18 March | H | Integrations manager agreed the date at the review; we will check in writing on 16 March | Scrum Master |
| Front desk books a slot a patient just took, during the sync gap | M | The double-booking guard rejects the second booking; pilot waits for the one-minute sync | Backend 1 |

Full list: [RAID log](./03-raid-log.md)

---

## Decisions and Asks

> What do you need from stakeholders, by when? Name the person. An ask without a date is a wish.

| Ask | From | Needed by |
|---|---|---|
| Written confirmation that the webhook is live in production for the pilot clinic | Integrations team manager | 16 March 2026 |
| Approve the daily patient-moves email as a pilot requirement | Head of clinic operations | 17 March 2026 |
| Name the front desk lead who will report problems during the pilot | Pilot clinic manager | 20 March 2026 |

---

## Key Metrics

| Metric | Last period | This period | Target |
|---|---|---|---|
| Sprint Goal met | Yes | Partially | Yes |
| Points delivered / committed | 30 / 30 | 21 / 29 | Steady at about 29 |
| Reschedule calls to the pilot clinic per week | 40 | 40 (pilot not live) | 25 after four weeks of pilot |
| Reminder time zone complaints | 6 | 0 | 0 |

---

**AI assist:** The Scrum Master drafted this with the [stakeholder report prompt](../../ai-workflows/claude-prompt-library.md#stakeholder-report), using the sprint review notes with names replaced by roles. Every number was checked against the board and the RAID log before sending. The draft's first version called the status green, so that line was rewritten by hand.
