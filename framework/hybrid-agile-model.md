# Hybrid Agile Model

## The Core Principle

No single methodology fits all contexts. The right approach depends on team size, product maturity, stakeholder expectations, and the nature of the work. This framework maps those variables to the right blend.

---

## Decision Matrix: Which Method to Apply

| Context | Recommended Approach |
|---|---|
| Single product team, defined sprint goal | Scrum |
| 3+ teams on one product | Nexus (Scrum of Scrums) |
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

When you have 3 or more Scrum teams working on a single product, introduce Nexus.

**What changes:**
- Add a Nexus Integration Team (NIT) responsible for cross-team dependency resolution
- Nexus Sprint Planning precedes individual team planning
- Integrated backlog sits above team-level backlogs
- Nexus Daily Scrum (15 min) surfaces cross-team blockers before they escalate
- Nexus Sprint Review combines team demos into one stakeholder event

**From experience (3 concurrent teams):**
The biggest value of Nexus is forcing explicit dependency mapping. Without it, teams discover conflicts at integration — after the sprint ends.

---

## Kanban for Operations

Apply Kanban to any workflow that is continuous rather than iterative.

**Best fits:**
- IT service desk and ITSM (ManageEngine SDP)
- Bug triage and hotfix queues
- Stakeholder request intake
- Hiring pipelines

**Key practices:**
- WIP limits per column (start with 2x team members, adjust from data)
- Explicit policies for each column — teams should not guess what "In Review" means
- Cycle time as the primary metric, not velocity
- Weekly queue review replaces sprint planning

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

See [AI-Assisted PM Workflows](../ai-workflows/ai-pm-workflows.md) for specifics.
