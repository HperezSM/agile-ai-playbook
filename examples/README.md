# Worked Example: One Sprint, Every Template Filled In

The templates are easier to use once you have seen them filled in. This example follows one Scrum team through one two-week sprint, from planning to the stakeholder update, using the playbook's templates and prompts as written.

Everything here is invented. The product, the clinics and the numbers are fictional, and people appear only as roles, which is how the [AI Guardrails](../ai-workflows/ai-guardrails.md#2-strip-what-the-model-does-not-need) ask you to write anything you might paste into an AI tool.

---

## The Setup

**Product:** Sonrisa Booking, a web app that books appointments for a small chain of dental clinics. Patients get an SMS reminder two days before each visit.

**Problem this sprint goes after:** Patients who need to move an appointment have to call the clinic. Front desks at the pilot clinic log about 40 reschedule calls a week.

**Team Ceiba:** Product Owner, Scrum Master (the PM writing these documents), two backend developers, two frontend developers and one QA engineer. Seven people, one Scrum Team.

**Sprint 14:** Monday 2 March to Friday 13 March 2026, ten working days.

**Outside the team:** the Integrations team owns the connection to the clinics' calendar system. An SMS provider sends the reminders and must approve every new message template.

**Method:** Scrum, picked with the [decision matrix](../framework/hybrid-agile-model.md#decision-matrix-which-method-to-apply) because the team builds new product features against a clear goal. The Integrations team runs Kanban, which is where this sprint's main dependency comes from.

---

## Read in This Order

| Step | File | Template used | What to notice |
|---|---|---|---|
| 1 | [Sprint Planning](./sprint-14/01-sprint-planning.md) | [Sprint Planning](../templates/sprint-planning-template.md) | An outcome-based Sprint Goal and a dependency with no confirmed date |
| 2 | [Daily Brief, Day 4](./sprint-14/02-daily-brief-day-4.md) | [Daily brief prompt](../ai-workflows/claude-prompt-library.md#how-these-prompts-are-built) | The AI invented a fact; the PM's review caught it |
| 3 | [RAID Log](./sprint-14/03-raid-log.md) | [RAID Log](../templates/raid-log-template.md) | How the dependency turned from a risk into an issue |
| 4 | [Sprint Review](./sprint-14/04-sprint-review.md) | [Sprint Review](../templates/sprint-review-template.md) | A partially met goal, reported plainly |
| 5 | [Retrospective](./sprint-14/05-retrospective.md) | [Retrospective](../templates/retrospective-template.md) | Actions with owners and one metric |
| 6 | [Stakeholder Update](./sprint-14/06-stakeholder-update.md) | [Stakeholder Update](../templates/stakeholder-update-template.md) | Named asks with dates |

---

## The Sprint in Numbers

These numbers stay the same in every file, so you can check one document against another the way a stakeholder would.

| | Value |
|---|---|
| Team capacity | 44 person-days |
| Committed | 7 items, 29 points |
| Delivered | 5 items, 21 points |
| Deferred | SB-203 calendar sync (5 points), SB-190 CSV export (3 points) |
| Sprint Goal | Partially met |
| Cause | The calendar webhook from the Integrations team arrived on Day 7 instead of Day 3, too late to test against the clinic calendar |

---

## What the Example Teaches

1. A Sprint Goal written as an outcome ("patients can reschedule") lets the team drop work that does not serve it. The CSV export went first when time ran short.
2. A dependency without a confirmed date is a risk on Day 1, so log it then. The team logged it but only escalated on Day 4, after the Day 3 deadline had passed, and got an answer on Day 6. The retrospective fixes that.
3. AI drafts save time only if a person checks them. On Day 4 the brief said the Integrations team had confirmed a date. They had not.
4. "Partially" is an honest answer at a Sprint Review. The stakeholder update says the same thing in the first line.
