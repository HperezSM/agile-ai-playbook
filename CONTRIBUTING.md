# Contributing

Suggestions and fixes are welcome. Open an issue first for anything larger than a typo, so we can agree on the change before you write it.

## What fits this playbook

- Practical guidance a PM or Scrum Master can use this week
- Templates that work when copied as-is
- Prompts you have actually used on real delivery work
- Corrections where the content disagrees with the official [Scrum](https://scrumguides.org/scrum-guide.html), [Nexus](https://www.scrum.org/resources/online-nexus-guide) or [Kanban](https://kanbanguides.org/english/) guides

## Style

- Plain language, short sentences, active voice
- Headings in Title Case to match the existing files
- Use relative links between files (`../templates/raid-log-template.md`)
- Templates ship with blank fields: no names, companies or dates filled in
- No client names, employer names, real project data or personal data in examples
- Label opinions as opinions ("In practice I...") and keep guide facts accurate

## Before you open a pull request

Run the checks locally. They need only Python 3.

```bash
python3 -m unittest discover -s tests
python3 scripts/check_docs.py
```

The same checks run in GitHub Actions on every push and pull request. They verify that relative links and heading anchors resolve, that no leftover to-do markers remain, and that templates have blank Author and Owner fields.

## License

By contributing you agree that your contribution is licensed under [CC BY 4.0](./LICENSE).
