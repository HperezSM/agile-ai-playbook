# AI Guardrails for PMs

AI tools make PM work faster. They also make it easy to paste a client contract into a chat window or send a stakeholder a number the model invented. These rules keep the speed without those mistakes. Agree them with your team and your security or legal contact before you automate anything.

---

## 1. Know Where the Data Goes

Before you paste anything, answer three questions:

- **Which tool and which plan?** Consumer chat apps, team plans and API access often have different data retention and training terms. Use the one your organization has approved.
- **Is it allowed by contract?** Client agreements and NDAs may forbid sending their data to third parties, including AI providers.
- **Would I be fine seeing this in a breach report?** If not, do not paste it.

When in doubt, use a tool your company has approved for the data's classification, or a model that runs locally.

---

## 2. Strip What the Model Does Not Need

Most PM prompts work just as well with less data.

- Replace people's names with roles ("Backend dev 1", "Client sponsor").
- Remove emails, phone numbers, customer names, account IDs and anything else that identifies a person.
- Never paste passwords, API keys, tokens or connection strings. Rotate any that slip in.
- Summarize sensitive context yourself instead of pasting the raw document.
- Keep health, financial and HR data out unless the tool is approved for that data type.

---

## 3. AI Drafts, a Person Decides

Every output that leaves your hands has a named human reviewer. In practice:

- Check every number, date and name against the source system before sending.
- Ask the model to quote or point to the input it used for each claim, then spot-check those.
- Be extra careful with anything that affects a person: performance, hiring, blame in a post-mortem. Do not let a model's summary be the evidence.
- If the model fills a gap with something plausible, treat it as wrong until proven otherwise.

---

## 4. Automations Need Extra Care

Scheduled workflows (for example n8n pulling tickets into a daily brief) run without anyone watching.

- Give the automation read-only access and the narrowest scope that works.
- Send output to the PM for review first, not straight to a stakeholder channel.
- Log what was sent to the model and what came back, so you can audit it later.
- Treat text inside tickets, emails and documents as data, not instructions. A ticket that says "ignore previous instructions" should not change what the workflow does.

---

## 5. Be Open About It

- Tell your team which ceremonies and reports use AI help.
- Do not record or transcribe meetings without everyone's consent.
- Keep the prompts you rely on in a shared library (like [this one](./claude-prompt-library.md)) so others can review and improve them.

---

## Quick Checklist

Before sending any AI-assisted output:

- [ ] Approved tool for this data
- [ ] Names and personal data removed or replaced
- [ ] No secrets in the prompt
- [ ] Numbers and dates checked against the source
- [ ] A person read the whole thing and owns it
