# Sprint Ceremonies Guide

Practical, no-fluff guide to running each Agile ceremony effectively. Based on 9+ years leading Scrum and Nexus teams across Healthcare, Fintech, and SaaS.

---

## Sprint Planning

**Goal:** Align the team on what will be built and how, resulting in a committed sprint backlog and a clear sprint goal.

**Duration:** 2 hours max for a 2-week sprint.

**Common mistakes:**
- Starting without a sprint goal → fills sprint with tasks, not outcomes
- PO presents stories cold without prior refinement → planning becomes discovery
- Team commits to more than capacity allows → sprint fails predictably

**My format:**
1. PO states sprint goal (5 min)
2. Team reviews top backlog items — questions and clarifications only (20 min)
3. Team self-selects stories up to capacity (30 min)
4. Task breakdown for Day 1-3 items (30 min)
5. Confirm sprint goal and commitment (5 min)

**AI assist:** Use Claude to pre-draft a candidate sprint backlog based on velocity and backlog priority. Start planning from a draft, not a blank slate.

---

## Daily Scrum

**Goal:** Synchronize the team and surface blockers. Not a status report.

**Duration:** 15 minutes hard stop.

**Format (3 questions):**
1. What did I complete that moves us toward the sprint goal?
2. What will I do today toward the sprint goal?
3. Is anything blocking me?

**Facilitator role:** Surface blockers immediately. Do not solve them in standup. Schedule a follow-up with the relevant people.

**Nexus add-on:** 15-min Nexus Daily Scrum after individual standups. Each team sends one rep. Focus: cross-team dependencies and integration risks only.

---

## Sprint Review

**Goal:** Inspect the increment and adapt the backlog based on stakeholder feedback.

**Duration:** 1 hour for a 2-week sprint.

**Who attends:** Team + Product stakeholders + Key users when possible.

**Format:**
1. Sprint goal recap — did we achieve it? (5 min)
2. Demo of completed work (30 min)
3. Stakeholder Q&A and feedback (15 min)
4. PO updates backlog based on feedback (10 min)

**Common mistakes:**
- Demoing in a dev environment full of bugs
- Showing work that isn't done to avoid awkward conversations
- No stakeholder feedback captured → review has no impact on the backlog

---

## Retrospective

**Goal:** Inspect how the team worked and commit to one improvement for the next sprint.

**Duration:** 1 hour.

**Format I use (Start / Stop / Continue + Action):**
1. Individual silent reflection (5 min)
2. Share and group themes (15 min)
3. Vote on top 3 themes (5 min)
4. Discuss and define 1-2 action items with owners (25 min)
5. Read back the actions and confirm ownership (10 min)

**Rule:** One action item that actually gets done beats five that get ignored.

**AI assist:** Use Claude to generate targeted prompts based on the team's recent pattern (late dependency discovery, unclear goals, etc.). See [prompt library](../ai-workflows/claude-prompt-library.md).

---

## Backlog Refinement

**Goal:** Ensure the top of the backlog is ready for sprint planning.

**Duration:** 30-45 min, weekly.

**Ready criteria (Definition of Ready):**
- User story has acceptance criteria
- Dependencies identified
- Estimated by the team
- No open questions blocking start

**Common mistakes:**
- Refining stories the sprint before they are needed → not enough time for questions
- PO refines alone and presents to team → team has no context, estimation is guesswork

---

## Nexus Sprint Planning (Multi-Team)

**Goal:** Align 3+ Scrum teams on cross-team dependencies before individual sprint planning.

**Duration:** 1 hour before team-level planning.

**Format:**
1. Review integrated product backlog — what is the overall sprint goal? (10 min)
2. Each team identifies which items they own and flags dependencies (20 min)
3. Resolve dependency conflicts and assign integration work to NIT (20 min)
4. Teams proceed to individual sprint planning with dependencies locked (10 min)
