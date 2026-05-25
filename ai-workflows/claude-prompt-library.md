# Claude AI Prompt Library for PMs

A curated set of prompts for Senior PMs and Scrum Masters. Tested in real delivery contexts.

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
