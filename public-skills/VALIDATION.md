# Public Writing Coach Skills Calibration Notes

Last updated: 2026-05-17

## Scope

This note records source checks and calibration smoke tests for two public-shareable skills:

- `public-skills/celpip-writing-coach/SKILL.md`
- `public-skills/ielts-writing-coach/SKILL.md`

The public CELPIP skill is generalized from a project-specific coaching workflow. It intentionally removes private file paths, personal archive requirements, and project-only references.

The IELTS skill is based on official public IELTS scoring and sample materials. It is not an official scoring engine.

## Official Sources Used

IELTS:

- IELTS Academic test format page: Writing has Task 1 and Task 2, minimum word counts, four criteria, and Task 2 contributes twice as much as Task 1.
  - `https://ielts.org/organisations/ielts-for-organisations/test-types/ielts-academic-test/academic-test-format-in-detail`
- IELTS scoring in detail: Writing uses four equal criteria per task; Task 2 carries more weight than Task 1; scores may be whole or half bands.
  - `https://ielts.org/take-a-test/your-results/ielts-scoring-in-detail`
- IELTS Writing Key Assessment Criteria PDF: defines Task Achievement, Task Response, Coherence and Cohesion, Lexical Resource, and Grammatical Range and Accuracy for Academic and General Training.
  - `https://ielts.org/cdn/ielts-guides/ielts-writing-key-assessment-criteria.pdf`
- British Council Academic sample candidate responses and examiner comments.
  - `https://takeielts.britishcouncil.org/sites/default/files/academic-writing-sample-candidate-responses-and-examiner-comments.pdf`
- British Council General Training sample candidate responses and examiner comments.
  - `https://takeielts.britishcouncil.org/sites/default/files/general-training-writing-sample-candidate-responses-and-examiner-comments.pdf`

CELPIP:

- CELPIP scoring levels and sample responses.
  - `https://www.celpip.ca/prepare-for-celpip/free-resources/scoring-levels/`
- CELPIP test results and scoring process: Writing is rated by trained raters across Content/Coherence, Vocabulary, Readability, and Task Fulfillment.
  - `https://www.celpip.ca/take-celpip/test-results/`

## Baseline Risk Test

A baseline risk review was run before drafting the IELTS skill. It identified the likely failure modes:

- overclaiming official scoring accuracy;
- missing separate rubrics for Academic Task 1, General Training Task 1, and Task 2;
- forgetting Task 2 double weighting;
- missing Academic Task 1 data accuracy and overview;
- missing General Training Task 1 tone/register;
- giving false precision around 6.5 versus 7.0;
- not tying drills to weakest criteria.

The IELTS skill now includes explicit gates and safeguards for each of these risks.

## Calibration Smoke Test Against Official Samples

The skill is expected to align with the direction of official examiner comments, not reproduce examiner judgment perfectly. The profiles below are coaching estimates made from the official sample responses and checked against the published examiner bands/comments.

| Official sample | Official band | Skill-estimated criterion profile | Match logic |
|---|---:|---|---|
| British Council Academic Task 1 Response 1 | 5.5 | TA 5, CC 5-6, LR 5-6, GRA 5-6 -> 5.5 | Covers key features but lacks overview; cohesion and accuracy are generally controlled but not flexible enough for higher bands. |
| British Council Academic Task 1 Response 2 | 3.5 | TA 3-4, CC 3, LR 3, GRA 3-4 -> 3.5 | Under-length, missed key feature, weak progression, repetitive basic vocabulary, frequent spelling/grammar errors. |
| British Council Academic Task 2 Response 1 | 5.5 | TR 5, CC 6, LR 5, GRA 5 -> 5.5 | Clear position and generally coherent progression, but under-length, underdeveloped ideas, word-choice/formation errors, and high sentence-error density. |
| British Council Academic Task 2 Response 2 | 7.5 | TR 7-8, CC 7-8, LR 8, GRA 7 -> 7.5 | Clear position, alternative view considered, logical progression, wider vocabulary, rare spelling errors; held below 8+ by content balance and sentence-form issues. |
| British Council General Training Task 1 Script A | 5 | TA 5, CC 5, LR 5, GRA 5 -> 5.0 | Purpose is clear, but response is under-length, repeats task wording, linking is weak, and complex sentences break down. |
| British Council General Training Task 2 Script A | 5 | TR 5, CC 5, LR 5, GRA 4-5 -> 5.0 | Relevant ideas and apparent view, but support is uneven, organisation weakens, and errors make some parts difficult to follow. |

## Accuracy Limits

- These skills provide coaching estimates only.
- They should show evidence and uncertainty rather than claiming official examiner precision.
- A mismatch larger than about 0.5 band against official samples should trigger recalibration of the relevant criterion. Smaller differences can still matter, but they are common in unofficial coaching estimates.
- Official samples are not definitive models for every prompt type, so validation must focus on criterion reasoning, not template imitation.
