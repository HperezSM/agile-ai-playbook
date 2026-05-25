# AI-Assisted PM Workflows

## The Problem AI Solves for PMs

Senior PMs spend 60-90 minutes daily on information gathering before making a single prioritization decision. Across Jira, Slack, email, and dashboards — the synthesis is manual, slow, and error-prone.

AI compresses that to minutes. Not by deciding — by surfacing and organizing.

---

## Workflow 1: AI Daily Brief (Morning Routine)

**Tool:** Claude + n8n
**Time saved:** 45-60 min/day

**How it works:**
1. n8n pulls open tickets, sprint metrics, and flagged messages at 7:30 AM
2. Claude summarizes into a structured brief:
   - Sprint health (velocity vs. plan)
   - Active blockers and owner
   - Decisions needed today
   - Stakeholder items pending
3. Brief delivered to Slack DM before standup

**Prompt pattern:**
```
You are a Senior PM assistant. Given the following sprint data and open items, produce a morning brief with: (1) sprint health summary, (2) top 3 blockers and recommended actions, (3) decisions needed today, (4) stakeholder follow-ups due. Be direct. No fluff.
```

---

## Workflow 2: AI-Assisted Sprint Planning

**Tool:** Claude
**Time saved:** 30 min per sprint planning session

**How it works:**
- Feed Claude the product backlog, team velocity history, and sprint goal
- Ask it to draft a candidate sprint backlog with story point allocation
- Use the output as a starting point for team discussion — not a final answer

**Key principle:** AI drafts, team decides. The planning session becomes a review and refinement, not a build-from-scratch exercise.

---

## Workflow 3: Automated Stakeholder Reporting

**Tool:** n8n + Claude
**Time saved:** 2-3 hours per reporting cycle

**How it works:**
1. n8n pulls sprint data at sprint end
2. Claude formats into stakeholder-ready summary: what was delivered, what was deferred, why, and what is next
3. PM reviews and sends — no manual formatting

**Output format:**
- Executive summary (3 sentences)
- Delivered this sprint (bullet list)
- Deferred and reason
- Next sprint focus
- Risks and asks

---

## Workflow 4: Retrospective Facilitation

**Tool:** Claude
**Time saved:** 1 hour prep per retro

**Prompt library for retros:**
```
Generate 5 retrospective prompts for a Scrum team that has been struggling with sprint goal clarity and late dependency discovery. Use the Start / Stop / Continue format. Make prompts specific, not generic.
```

```
Summarize the following retrospective notes into: (1) top 3 themes, (2) agreed action items with owners, (3) one metric to track improvement next sprint. Notes: [paste notes]
```

---

## Workflow 5: Risk Radar

**Tool:** Claude
**Cadence:** Weekly

**Prompt:**
```
Given the following sprint status, team capacity, and open dependencies, identify the top 3 delivery risks for this sprint. For each: state the risk, likelihood (H/M/L), impact (H/M/L), and one mitigation action. Be direct.
```

---

## What AI Cannot Replace

- Stakeholder relationship management
- Team morale reads and 1:1 judgment
- Product vision and prioritization decisions
- Conflict resolution
- Trust-building with engineering

AI accelerates information processing. The PM still owns the judgment layer.
