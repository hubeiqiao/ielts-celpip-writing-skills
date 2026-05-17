# Public IELTS and CELPIP Writing Coach Skills

This folder contains the public export package for two reusable writing coach skills:

- `ielts-writing-coach/`: IELTS Academic and General Training Writing coaching.
- `celpip-writing-coach/`: CELPIP Writing Task 1 email and Task 2 survey coaching.

For normal installation, use the repo-level `skills/` folder through skills.sh:

```bash
npx skills add hubeiqiao/ielts-celpip-writing-skills
```

## Plain-Language Introduction

These skills tell an AI agent how to review exam writing in a structured way. You paste a task and your answer, and the agent gives focused feedback, a score-aware breakdown, the most important fixes, and reusable phrases to practise next.

No coding knowledge is required. A skill is just a reusable instruction folder that helps your AI agent follow the same coaching method every time.

The IELTS skill uses the same coaching method but adapts it to IELTS Academic and General Training criteria.

The CELPIP skill was developed from repeated practice and used by Joe Hu, who achieved CLB 9 in CELPIP Writing. This CLB 9 result is not AI-generated; it is a real outcome and a case study, not a score guarantee.

## Scoring Method

The score estimate is not a free-form AI guess. Each skill checks binary criteria first:

- task type and required elements
- word count and format
- register and tone
- paragraphing and coherence
- official rubric signals
- visible evidence from the learner's draft

After these checks, the agent gives a coaching estimate and explains the evidence. Official scores still come only from CELPIP or IELTS examiners.

## IELTS vs CELPIP: Core Differences

| Area | IELTS Writing Coach | CELPIP Writing Coach |
|---|---|---|
| Main task types | Academic Task 1, General Training Task 1, and Task 2 essays | Task 1 emails and Task 2 surveys |
| Language setting | Academic or semi-formal international English | Canadian workplace and community writing |
| Coaching priority | Official IELTS criteria, overview or position control, Task 2 2:1 weighting | Practical clarity, format gates, Canadian tone, reusable sentence chunks |
| Best output | Rubric-aligned estimate plus targeted revision path | Short, deep feedback on the highest-impact fixes |

## JoeSpeaking

JoeSpeaking is the IELTS and CELPIP Speaking practice app Joe built for his own preparation. Joe used it to reach CLB 9 on his first CELPIP attempt. Try it at [JoeSpeaking.com](https://JoeSpeaking.com).

## Files

- `ielts-writing-coach/SKILL.md`
- `celpip-writing-coach/SKILL.md`
- `VALIDATION.md`: source checks and calibration smoke tests against public IELTS and CELPIP materials.
- `OFFICIAL_SAMPLE_CASES.md`: public official sample case-study template and filled examples.
- `validate_public_skills.py`: deterministic public-readiness check.

## Source Attribution

Official example scores in `OFFICIAL_SAMPLE_CASES.md` are attributed to public British Council IELTS sample PDFs and CELPIP public scoring pages. The package links to the official sources and paraphrases examiner or source comments instead of redistributing full sample answers.

## Verify

Run:

```bash
python3 public-skills/validate_public_skills.py
python3 path/to/skill-creator/scripts/quick_validate.py public-skills/ielts-writing-coach
python3 path/to/skill-creator/scripts/quick_validate.py public-skills/celpip-writing-coach
python3 path/to/skill-creator/scripts/quick_validate.py skills/ielts-writing-coach
python3 path/to/skill-creator/scripts/quick_validate.py skills/celpip-writing-coach
```
