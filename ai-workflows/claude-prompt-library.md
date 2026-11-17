# Claude AI Prompt Library for PMs

A curated set of prompts for Senior PMs and Scrum Masters. Tested in real delivery contexts.

Read the [AI Guardrails for PMs](./ai-guardrails.md) before pasting real project data into any prompt.

---

## How These Prompts Are Built

The short prompts below work as they are. When you need better output, rebuild them with this structure. Claude and most current models follow it well.

1. **Role and context first.** Say who the output is for and what situation the team is in.
2. **Separate your inputs with XML tags.** `<sprint_data>`, `<notes>`, `<story>` and similar tags stop the model from mixing your instructions with your data.
3. **State the task plainly.** One clear instruction beats several vague ones.
4. **Specify the output format.** A table, numbered list or fixed headings make the output easy to paste into a template.
5. **Give an example** of a good answer when the format matters.
6. **Tell it what to do when data is missing.** "Say 'not in the data'" prevents invented numbers.

Example, the daily brief rebuilt:

```
You are helping a Senior PM prepare for today's Daily Scrum. The reader is the PM, who will review your brief before sharing anything.

<sprint_data>
[paste sprint data]
</sprint_data>

<open_items>
[paste open items]
</open_items>

Write a morning brief with these headings:
1. Sprint health: on track / at risk / off track, with the reason
2. Top 3 blockers, each with a recommended action and owner
3. Decisions needed today
4. Stakeholder items waiting for a reply

Use only the data above. If something is missing, write "not in the data" instead of guessing. Bullet points, no more than 200 words.
```

---

## Daily Brief

```
You are a Senior PM assistant. Given the following sprint data and open items, produce a morning brief with:
1. Sprint health summary (on track / at risk / off track + reason)
2. Top 3 blockers and recommended actions
3. Decisions needed today
4. Stakeholder items pending response

Be direct. Use bullet points. No fluff.

Sprint data: [paste data]
Open items: [paste items]
```

---

## Sprint Goal Drafting

```
Draft 3 candidate sprint goals for a [team type] team working on [product area]. Each goal should be outcome-focused, measurable by end of sprint, and achievable given a velocity of [X] points. Format: one sentence each.
```

---

## Risk Assessment

```
Given the following sprint status and team context, identify the top 3 delivery risks. For each risk: state it plainly, rate likelihood (H/M/L) and impact (H/M/L), and give one specific mitigation action. Do not hedge. Be direct.

Context: [paste context]
```

---

## Stakeholder Report

```
Write a sprint summary for executive stakeholders. Tone: professional and direct. Structure:
- One-paragraph executive summary
- What was delivered (bullet list)
- What was deferred and why
- Next sprint focus
- Any asks or decisions needed from stakeholders

Source data: [paste sprint data]
```

---

## Retrospective Prompts

```
Generate 5 retrospective prompts for a Scrum team experiencing [specific problem]. Use Start / Stop / Continue format. Make prompts specific to the problem — avoid generic questions like "what went well?"
```

```
Summarize these retrospective notes into:
1. Top 3 themes
2. Agreed action items with suggested owners
3. One metric to track improvement next sprint

Notes: [paste notes]
```

---

## Backlog Refinement

```
Review the following user story and tell me: (1) Is the acceptance criteria testable and complete? (2) Are there hidden dependencies? (3) What clarifying questions should the team ask before estimating?

Story: [paste story]
```

---

## Dependency Mapping

```
Given these items across 3 Scrum teams, identify cross-team dependencies that could block sprint delivery. Flag which ones need resolution before sprint planning. Output as a table: Item | Owner Team | Depends On | Risk Level.

Items: [paste items]
```

Paste the result into the [Nexus Sprint Planning template](../templates/nexus-sprint-planning-template.md) after you check it with the teams.

---

## Kanban Flow Summary

```
You are helping a team lead prepare a weekly Kanban queue review.

<board_export>
[paste items: title, current column, start date, finish date if done, class of service. No customer or personal data.]
</board_export>

Today is [date]. Our Service Level Expectation is 85% of items finished within [N] days.

1. Count Work in Progress, Throughput for the last 7 days, and the 85th percentile Cycle Time of items finished in the last 30 days.
2. List every unfinished item whose Work Item Age is above [N] days, oldest first, as a table: Item | Column | Age (days).
3. Name the column where most of the old items are waiting.

Use only the data above. If a date is missing, say "not in the data" for that item instead of guessing. Show how you counted.
```

Use the output to pre-fill sections 1 and 2 of the [Kanban Queue Review template](../templates/kanban-queue-review-template.md). Check the numbers against the board before the meeting.

---

## Hiring and Team Assessment

```
I am interviewing a candidate for a [role] position on a Scrum team. Based on the following job requirements, generate 5 behavioral interview questions that reveal whether they can [specific skill]. Include what a strong answer looks like for each.

Requirements: [paste JD]
```

---

## PRD Drafting

```
Draft a Product Requirements Document for the following feature. Include: problem statement, target user, success metrics, functional requirements, non-functional requirements, out of scope, and open questions. Be specific. Avoid vague requirements.

Feature brief: [paste brief]
```
