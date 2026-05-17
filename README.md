# IELTS and CELPIP Writing Coach Skills

[![skills.sh](https://skills.sh/b/hubeiqiao/ielts-celpip-writing-skills)](https://skills.sh/hubeiqiao/ielts-celpip-writing-skills)

This repository shares two reusable AI agent skills for exam writing practice:

- `ielts-writing-coach`: for IELTS Academic Writing and IELTS General Training Writing.
- `celpip-writing-coach`: for CELPIP Writing Task 1 emails and Task 2 survey responses.

They are designed for learners who want focused feedback, reusable sentence structures, and score-aware coaching without writing a full new essay every day.

## Quick Start

If your AI agent supports skills, install this repo with the Skills CLI:

```bash
npx skills add hubeiqiao/ielts-celpip-writing-skills
```

Then ask your agent:

```text
Use the IELTS writing coach skill to review this IELTS Task 2 essay.
```

or:

```text
Use the CELPIP writing coach skill to review this Task 2 survey response.
```

No coding knowledge is required. A skill is just a reusable instruction folder that tells your AI agent how to coach, score, and explain writing more consistently.

## What Makes This Trustworthy

The CELPIP workflow was developed from repeated practice and used by Joe Hu, who achieved CLB 9 in CELPIP Writing. This CLB 9 credential is not AI-generated; it is a real learner result and a case study, not a guarantee of your score.

The skills do not ask the AI to invent a band score from instinct. They first check visible binary criteria such as task coverage, format, word count, register, paragraphing, required Task 1 or Task 2 elements, and evidence from official public sample scoring. Only after those checks do they provide a coaching estimate.

Official scores still come only from CELPIP or IELTS examiners. These skills are preparation tools.

## IELTS vs CELPIP: Core Differences

| Skill | Best for | Main scoring focus | Output style |
|---|---|---|---|
| IELTS Writing Coach | Academic and General Training IELTS writing | IELTS Task Achievement or Task Response, Coherence and Cohesion, Lexical Resource, Grammatical Range and Accuracy | Official-criteria-aligned coaching estimate with targeted revision steps |
| CELPIP Writing Coach | Canadian workplace and community writing | Task 1 email gates, Task 2 survey gates, Canadian English, practical clarity | Deep feedback on a small number of repeatable fixes |

Use the IELTS skill when the task is IELTS Academic Task 1, General Training Task 1, or Task 2 essay writing.

Use the CELPIP skill when the task is an email or survey response in a Canadian daily-life or workplace context.

## What You Get

- Clear task detection before feedback.
- Score breakdowns with evidence, not vague comments.
- Focus on the few error clusters that most limit the score.
- Sentence structures and vocabulary to remember for the next attempt.
- Answer keys for drills, so learners can practise directly.
- Official-source validation notes and public sample case templates.

## JoeSpeaking

JoeSpeaking is the IELTS and CELPIP Speaking practice app I built for my own preparation. I used my app to reach CLB 9 on my first CELPIP attempt, and you are welcome to try it at [JoeSpeaking.com](https://JoeSpeaking.com).

## Repository Layout

| Path | Purpose |
|---|---|
| `skills/ielts-writing-coach/` | Standard skills.sh-compatible IELTS skill folder. |
| `skills/celpip-writing-coach/` | Standard skills.sh-compatible CELPIP skill folder. |
| `docs/VALIDATION.md` | Source checks and calibration notes against public IELTS and CELPIP materials. |
| `docs/OFFICIAL_SAMPLE_CASES.md` | Public official sample case-study templates and filled examples. |
| `scripts/validate_public_skills.py` | Deterministic public-readiness check. |

## Skills.sh Discoverability

This repo is prepared for [The Agent Skills Directory](https://www.skills.sh/) by exposing a standard `skills/` folder and an install command:

```bash
npx skills add hubeiqiao/ielts-celpip-writing-skills
```

According to the skills.sh documentation, skills are installed from GitHub repositories with `npx skills add <owner>/<repo>`, and repositories appear on the leaderboard through anonymous install telemetry after users install them.

## Verification

Run these checks before publishing changes:

```bash
python3 scripts/validate_public_skills.py
python3 path/to/skill-creator/scripts/quick_validate.py skills/ielts-writing-coach
python3 path/to/skill-creator/scripts/quick_validate.py skills/celpip-writing-coach
```

## Public Sources

- Skills documentation: https://www.skills.sh/docs
- Skills CLI documentation: https://www.skills.sh/docs/cli
- IELTS scoring detail: https://ielts.org/take-a-test/your-results/ielts-scoring-in-detail
- IELTS writing criteria: https://ielts.org/cdn/ielts-guides/ielts-writing-key-assessment-criteria.pdf
- CELPIP test results: https://www.celpip.ca/take-celpip/test-results/
- CELPIP writing scores: https://www.celpip.ca/prepare-for-celpip/free-resources/writing-scores/
