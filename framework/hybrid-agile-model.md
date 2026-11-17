# Hybrid Agile Model

## The Core Principle

No single methodology fits all contexts. The right approach depends on team size, product maturity, stakeholder expectations, and the nature of the work. This framework maps those variables to the right blend.

---

## Decision Matrix: Which Method to Apply

| Context | Recommended Approach |
|---|---|
| Single product team, defined sprint goal | Scrum |
| 3 to 9 teams on one product | Nexus |
| Operations, ITSM, or support workloads | Kanban |
| Mixed product + ops team | Hybrid: Scrum for dev, Kanban for ops |
| Rapid prototyping / discovery phase | Lean + timeboxed spikes |
| AI tooling integration | Any of the above + AI layer |

---

## Scrum Foundation

Use Scrum as your backbone for product development squads.

**Non-negotiables:**
- 2-week sprints (default). Adjust to 1-week for early-stage products.
- Definition of Done shared across the team, not left to individual interpretation
- Sprint Goal set before sprint planning begins — not after
- Retrospective is not optional. It is where the team compounds

**Common failure modes I have seen:**
- Sprint planning without a clear goal → teams fill sprints with tasks, not outcomes
- Retros that produce no action items → trust erodes, nothing improves
- PO who is unavailable during the sprint → blockers pile up, velocity drops

---

## Nexus for Multi-Team Scaling

When 3 to 9 Scrum Teams work on a single product, introduce Nexus. Nexus is a defined framework with its own accountabilities and events. It is often confused with a "Scrum of Scrums", which is an informal sync meeting with no fixed rules.

**What changes:**
- Add a Nexus Integration Team (NIT) accountable for making sure an integrated increment is produced at least once per sprint. The NIT coaches and unblocks; the Scrum Teams still do most of the integration work.
- One Product Backlog and one Product Owner for the whole Nexus
- Nexus Sprint Planning precedes individual team planning and sets a Nexus Sprint Goal
- Nexus Daily Scrum surfaces integration issues and cross-team dependencies before they escalate
- Nexus Sprint Review replaces the individual team reviews with one stakeholder event
- Nexus Sprint Retrospective looks at problems that cross team boundaries

**From experience (3 concurrent teams):**
The biggest value of Nexus is forcing explicit dependency mapping. Without it, teams discover conflicts at integration — after the sprint ends. The [Nexus Sprint Planning template](../templates/nexus-sprint-planning-template.md) makes the mapping part of planning.

---

## Kanban for Operations

Apply Kanban to any workflow that is continuous rather than iterative.

**Best fits:**
- IT service desk and ITSM queues, whatever the tool
- Bug triage and hotfix queues
- Stakeholder request intake
- Hiring pipelines

**Key practices:**
- WIP limits per column. Start low (about one item per person in the column) and adjust from data.
- Explicit policies for each column — teams should not guess what "In Review" means
- Flow metrics instead of velocity (see below)
- Weekly queue review replaces sprint planning (see the [Kanban Queue Review](../ceremonies/ceremonies-guide.md#kanban-queue-review))

**The four flow metrics (Kanban Guide 2020):**

| Metric | What it measures | Question it answers |
|---|---|---|
| Work in Progress (WIP) | Items started but not finished | Are we starting more than we finish? |
| Throughput | Items finished per unit of time | How much do we deliver per week? |
| Work Item Age | Time since an unfinished item started | Which item is getting stuck right now? |
| Cycle Time | Time from start to finish of an item | How long does a typical item take? |

Work Item Age is the one most teams skip and the one that catches problems earliest. Review the oldest items in every queue review.

---

## Hybrid in Practice

Most mature product orgs run a hybrid without naming it explicitly.

A typical week for a Sr PM leading a hybrid team:

| Time | Activity | Method |
|---|---|---|
| Mon AM | Nexus Daily Scrum + dependency check | Nexus |
| Mon PM | ITSM queue review + WIP rebalance | Kanban |
| Mid-sprint | AI brief review, risk radar scan | AI-assisted |
| Wed | Stakeholder sync | Scrum (Sprint artifact review) |
| Fri | Team 1:1s + retrospective prep | Scrum |
| EOSprint | Sprint review + integrated demo | Nexus |

---

## How AI Fits In

AI does not replace the methodology. It accelerates the information layer.

See [AI-Assisted PM Workflows](../ai-workflows/ai-pm-workflows.md) for specifics, and [AI Guardrails for PMs](../ai-workflows/ai-guardrails.md) before you put real project data into any AI tool.

---

## Sources

The method descriptions follow the official guides. Read them; they are short.

- [The Scrum Guide (2020)](https://scrumguides.org/scrum-guide.html)
- [The Nexus Guide (2021)](https://www.scrum.org/resources/online-nexus-guide)
- [The Kanban Guide (2020)](https://kanbanguides.org/english/)
