# Sprint Ceremonies Guide

Practical, no-fluff guide to running each Agile ceremony effectively. Based on 9+ years leading Scrum and Nexus teams across Healthcare, Fintech, and SaaS.

---

## Sprint Planning

**Goal:** Agree why the sprint is valuable, what can be done, and how the work will get done. The output is a Sprint Goal, the selected backlog items, and a plan for delivering them (together, the Sprint Backlog).

**Duration:** The Scrum Guide caps it at 8 hours for a one-month sprint, shorter for shorter sprints. In practice I aim for 2 hours on a 2-week sprint.

**The three topics (Scrum Guide 2020):**
1. **Why** is this sprint valuable? The Product Owner proposes how the product could increase its value; the whole Scrum Team then shapes the Sprint Goal together.
2. **What** can be done this sprint? Developers select items from the Product Backlog based on past performance and upcoming capacity.
3. **How** will the chosen work get done? Developers break items into work small enough to start, often a day or less.

**Common mistakes:**
- Starting without a sprint goal → fills sprint with tasks, not outcomes
- PO presents stories cold without prior refinement → planning becomes discovery
- Team commits to more than capacity allows → sprint fails predictably

**My format:**
1. PO proposes the value of the sprint; team drafts the Sprint Goal (10 min)
2. Team reviews top backlog items — questions and clarifications only (20 min)
3. Developers select items up to capacity (30 min)
4. Breakdown of the work for the first days of the sprint (30 min)
5. Read back the Sprint Goal and confirm the plan (5 min)

**Template:** [Sprint Planning template](../templates/sprint-planning-template.md)

**AI assist:** Use Claude to pre-draft a candidate sprint backlog based on velocity and backlog priority. Start planning from a draft, not a blank slate.

---

## Daily Scrum

**Goal:** Synchronize the team and surface blockers. Not a status report.

**Duration:** 15 minutes hard stop, same time and place every working day.

**Format:** Since the 2020 Scrum Guide, the Developers choose any structure that keeps the focus on progress toward the Sprint Goal. The classic three questions are now optional. They still work well for new teams:
1. What did I complete that moves us toward the sprint goal?
2. What will I do today toward the sprint goal?
3. Is anything blocking me?

Mature teams often "walk the board" instead: go right to left across the board and talk about the work that is closest to done.

**Facilitator role:** Surface blockers immediately. Do not solve them in standup. Schedule a follow-up with the relevant people.

**Nexus add-on:** The Nexus Daily Scrum is attended by representatives of each team. Focus: integration issues and new cross-team dependencies only. Teams then carry what they learned into their own Daily Scrums.

---

## Sprint Review

**Goal:** Inspect the increment and adapt the backlog based on stakeholder feedback.

**Duration:** The Scrum Guide caps it at 4 hours for a one-month sprint. I run 1 hour for a 2-week sprint.

**Who attends:** Team + Product stakeholders + Key users when possible. Treat it as a working session, not a presentation.

**Template:** [Sprint Review template](../templates/sprint-review-template.md)

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

**Duration:** The Scrum Guide caps it at 3 hours for a one-month sprint. One hour is enough for a 2-week sprint.

**Format I use (Start / Stop / Continue + Action):**
1. Individual silent reflection (5 min)
2. Share and group themes (15 min)
3. Vote on top 3 themes (5 min)
4. Discuss and define 1-2 action items with owners (25 min)
5. Read back the actions and confirm ownership (10 min)

**Rule:** One action item that actually gets done beats five that get ignored.

**AI assist:** Use Claude to generate targeted prompts based on the team's recent pattern (late dependency discovery, unclear goals, etc.). See [prompt library](../ai-workflows/claude-prompt-library.md#retrospective-prompts).

**Template:** [Retrospective template](../templates/retrospective-template.md)

---

## Backlog Refinement

**Goal:** Ensure the top of the backlog is ready for sprint planning.

Refinement is an ongoing activity in the Scrum Guide, not a formal event. Most teams still book a regular slot so it actually happens.

**Duration:** 30-45 min, weekly.

**Ready criteria (Definition of Ready):** This is a team practice, not part of the Scrum Guide. Keep it short so it does not become a gate. See the [Definition of Done and Ready template](../templates/definition-of-done-and-ready.md).
- User story has acceptance criteria
- Dependencies identified
- Estimated by the team
- No open questions blocking start

**Common mistakes:**
- Refining stories the sprint before they are needed → not enough time for questions
- PO refines alone and presents to team → team has no context, estimation is guesswork

---

## Nexus Sprint Planning (Multi-Team)

**Goal:** Align the Scrum Teams in a Nexus (3 to 9 teams) on one Nexus Sprint Goal and on cross-team dependencies before individual sprint planning.

**Duration:** 1 hour before team-level planning.

**Who attends:** Appropriate representatives from each team, plus the Product Owner. The Nexus Integration Team makes sure integration is planned for.

**Format:**
1. Review the single Product Backlog and agree the Nexus Sprint Goal (10 min)
2. Each team identifies which items they own and flags dependencies (20 min)
3. Resolve dependency conflicts; resequence or reassign work to remove them (20 min)
4. Teams proceed to individual sprint planning with dependencies visible (10 min)

The other Nexus events follow the same pattern: the **Nexus Daily Scrum** (see above), a single **Nexus Sprint Review** that replaces the individual team reviews, and a **Nexus Sprint Retrospective** that looks at cross-team issues before or after the team retros.
