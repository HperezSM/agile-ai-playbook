# Daily Brief: Sprint 14, Day 4

Thursday 5 March 2026. Part of the [worked example](../README.md).

This is [Workflow 1: AI Daily Brief](../../ai-workflows/ai-pm-workflows.md#workflow-1-ai-daily-brief-morning-routine) as it ran on one morning: what went into the model, what came back, and what the Scrum Master changed before anyone else saw it.

---

## 1. What Went Into the Prompt

The Scrum Master exported the board and the open threads, then cleaned them up before pasting:

- People's names became roles (Backend 2, Integrations queue lead).
- Patient details in two bug comments were deleted. The brief does not need them, and this is health data.
- A staging password pasted into a ticket comment was removed, and the Scrum Master asked QA to rotate it.

The prompt is the structured daily brief from the [prompt library](../../ai-workflows/claude-prompt-library.md#how-these-prompts-are-built), unchanged except for the data:

```
You are helping a Senior PM prepare for today's Daily Scrum. The reader is the PM, who will review your brief before sharing anything.

<sprint_data>
Sprint 14, day 4 of 10. Sprint Goal: Patients can move their own appointment from the SMS reminder link, without calling the clinic.
Committed: 29 points. Done: 3 points (SB-198).
SB-202 Move-appointment API, 5 pts, In Progress, Backend 1. Lock on target slot merged; API endpoint in review.
SB-201 Reschedule page, 8 pts, In Progress, Frontend 1. Built against a stub; waiting for SB-202.
SB-204 SMS link, 2 pts, Blocked, Frontend 2. Template submitted to SMS provider on 2 March; no answer yet.
SB-203 Calendar sync, 5 pts, In Progress, Backend 2. Payload agreed with Integrations team on 3 March.
SB-205 Audit log, 3 pts, To Do.
SB-190 CSV export, 3 pts, To Do.
</sprint_data>

<open_items>
- Backend 2 asked the Integrations queue lead on 3 March for a delivery date for the appointment-changed webhook. No reply in the thread.
- QA: staging SMS sandbox allows 50 messages a day; yesterday's test run hit the limit at 14:00.
- Pilot clinic manager has not answered the question about patient moves without a confirmation call (asked 2 March).
</open_items>

Write a morning brief with these headings:
1. Sprint health: on track / at risk / off track, with the reason
2. Top 3 blockers, each with a recommended action and owner
3. Decisions needed today
4. Stakeholder items waiting for a reply

Use only the data above. If something is missing, write "not in the data" instead of guessing. Bullet points, no more than 200 words.
```

---

## 2. What Came Back

> **1. Sprint health: on track.** 3 of 29 points done on day 4, and the core API is nearly ready. The Integrations team has confirmed the webhook for Friday, so calendar sync should land next week.
>
> **2. Top 3 blockers**
> - SB-204 waiting on SMS template approval. Action: Product Owner chases the provider today.
> - Staging SMS sandbox limit is stopping QA. Action: QA asks the provider for a higher test limit.
> - SB-201 waiting on SB-202. Action: Backend 1 prioritises the API review.
>
> **3. Decisions needed today**
> - Whether QA tests SMS with a mock instead of the sandbox for the rest of the sprint.
>
> **4. Stakeholder items waiting**
> - Pilot clinic manager: moves without a confirmation call (asked 2 March).
> - SMS provider: template approval (submitted 2 March).

---

## 3. What the Scrum Master Changed

| Brief said | Source said | Change |
|---|---|---|
| "The Integrations team has confirmed the webhook for Friday" | No reply from the Integrations queue lead | Deleted. The model filled a gap with something plausible, so the [guardrails](../../ai-workflows/ai-guardrails.md#3-ai-drafts-a-person-decides) say to treat it as wrong. |
| Sprint health: on track | 3 of 29 points done; the goal's last step depends on a webhook with no date | Changed to **at risk**. The reason is the missing date, not the burndown. |
| Top 3 blockers did not include the webhook | Day 3 has passed without a date, and that was the deadline set at planning | Added as blocker 1. Action: Scrum Master raises it with the Integrations team's manager today. |
| Waiting items did not include the Integrations team | Thread open since 3 March | Added. |

Everything else checked out against the board.

**Time:** about 4 minutes for the model and 6 minutes for review. Writing the brief by hand used to take about 25 minutes.

---

## 4. The Brief as Shared at the Daily Scrum

1. **Sprint health: at risk.** The webhook SB-203 needs has no delivery date, and Day 3 has passed. The rest is moving.
2. **Blockers**
   - Calendar webhook has no date. Scrum Master escalates to the Integrations team's manager today.
   - SMS template approval pending since 2 March. Product Owner chases the provider.
   - Staging SMS limit. QA switches to the provider's mock for functional tests.
3. **Decision today:** mock SMS for functional tests, real sandbox only for one end-to-end run per day. Agreed by the Developers at the Daily Scrum.
4. **Waiting on:** Integrations queue lead (webhook date), SMS provider (template), pilot clinic manager (moves without a call).

---

## What Happened Next

The escalation went out on Day 4, but the Integrations team's manager answered on Day 6 that the webhook would ship on Day 7. The team had lost three days of slack before anyone outside the team knew there was a problem. The [RAID log](./03-raid-log.md) shows the dependency becoming an issue, and the [retrospective](./05-retrospective.md) deals with why the escalation came late.
