# RAID Log: Sonrisa Booking

Filled-in copy of the [RAID Log template](../../templates/raid-log-template.md), as it stood at the end of Sprint 14. Part of the [worked example](../README.md).

**Project:** Sonrisa Booking, patient self-reschedule
**Owner:** Scrum Master
**Last reviewed:** Friday 13 March 2026

Scales: Likelihood and Impact are H / M / L. Status is Open / Monitoring / Closed.

---

## Risks

Something that might happen and would hurt delivery.

| ID | Risk | Likelihood | Impact | Mitigation | Owner | Status |
|---|---|---|---|---|---|---|
| R-01 | Webhook from the Integrations team arrives too late to finish SB-203 this sprint | H | H | Escalated on Day 4. Became I-02 on Day 6 | Scrum Master | Closed |
| R-02 | SMS provider rejects the template because the link domain is new | M | M | Submitted on Day 1 with the domain's verification attached | Product Owner | Closed |
| R-03 | Clinic calendar shows a stale slot for up to 15 minutes, so a front desk books a slot a patient just took | M | H | The double-booking guard in SB-202 rejects the second booking. Pilot stays off until SB-203 ships | Backend 1 | Monitoring |

---

## Assumptions

Something you are treating as true without proof. Each one needs a date by which you will check it.

| ID | Assumption | Check by | How we will check | Owner | Status |
|---|---|---|---|---|---|
| A-01 | The pilot clinic accepts patient moves without phoning the patient to confirm | 11 March 2026 | Ask the clinic manager directly | Product Owner | Closed: confirmed on 9 March, with a request for a daily summary email |
| A-02 | Patients open reminder links on their phones, so the reschedule page only needs a mobile layout | 10 April 2026 | Device data from the first two pilot weeks | Product Owner | Open |

---

## Issues

Something that is already happening and hurting delivery.

| ID | Issue | Impact | Action | Owner | Due | Status |
|---|---|---|---|---|---|---|
| I-01 | Staging SMS sandbox allows 50 messages a day, which blocked QA on Day 3 | M | Mock SMS for functional tests, one real end-to-end run a day | QA | 5 March 2026 | Closed |
| I-02 | Webhook delivered on Day 7 instead of Day 3; SB-203 cannot meet the Definition of Done this sprint | H | SB-203 carried to Sprint 15. Pilot moved to Sprint 15 | Product Owner | 13 March 2026 | Open |

---

## Dependencies

Work you need from someone outside the team, or work others need from you.

| ID | Dependency | Direction (In/Out) | Other team | Needed by | Owner | Status |
|---|---|---|---|---|---|---|
| D-01 | Appointment-changed webhook in staging | In | Integrations | 4 March 2026 | Backend 2 | Closed: delivered 10 March |
| D-02 | Approval of the new reminder SMS template | In | SMS provider | 9 March 2026 | Product Owner | Closed: approved 6 March |
| D-03 | Webhook enabled in production for the pilot clinic | In | Integrations | 18 March 2026 | Scrum Master | Open |
| D-04 | Short guide for front desks on what a patient move looks like in their calendar | Out | Clinic operations | 20 March 2026 | Product Owner | Open |

---

## Note From the Scrum Master

R-01 sat at High / High from Day 1 and was still only "Open" on Day 3. A risk rated that high needs a dated escalation step in the Mitigation column, not just an owner. That change is now a retrospective action.
