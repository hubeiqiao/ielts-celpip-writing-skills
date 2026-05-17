#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent
REPO_ROOT = ROOT.parent
PUBLIC_SKILLS = [
    ROOT / "celpip-writing-coach" / "SKILL.md",
    ROOT / "ielts-writing-coach" / "SKILL.md",
]
MIRROR_ROOT = REPO_ROOT / "skills"
MIRROR_SKILLS = [
    MIRROR_ROOT / "celpip-writing-coach" / "SKILL.md",
    MIRROR_ROOT / "ielts-writing-coach" / "SKILL.md",
]
README = ROOT / "README.md"
ROOT_README = REPO_ROOT / "README.md"
VALIDATION = ROOT / "VALIDATION.md"
OFFICIAL_CASES = ROOT / "OFFICIAL_SAMPLE_CASES.md"
MIRROR_OFFICIAL_CASES = MIRROR_ROOT / "OFFICIAL_SAMPLE_CASES.md"

FORBIDDEN = [
    "/Users/",
    "joehu",
    "Final Project_Local",
    "Daily Test Log",
    "daily-feedback",
    "practice-records",
    "Mad English",
    "CLB9",
    "CLB 9 practice progress",
    "hubeiqiao/CELPIP-Writing",
    "hubeiqiao/celpip-ielts-writing-coach",
    "hubeiqiao/ielts-celpip-writing-coach",
    "CELPIP vs IELTS: Core Differences",
]

README_REQUIRED = [
    "CLB 9 in CELPIP Writing",
    "not AI-generated",
    "binary criteria",
    "JoeSpeaking.com",
    "npx skills add hubeiqiao/ielts-celpip-writing-skills",
    "skills.sh",
    "IELTS vs CELPIP: Core Differences",
    "No coding knowledge is required",
    "Official scores still come only from CELPIP or IELTS examiners",
]

IELTS_REQUIRED = [
    "Academic Task 1",
    "General Training Task 1",
    "Task 2 carries more weight",
    "2:1 coaching weighting",
    "(Task 1 + 2 * Task 2) / 3",
    "Task Achievement",
    "Task Response",
    "Coherence and Cohesion",
    "Lexical Resource",
    "Grammatical Range and Accuracy",
    "coaching estimate",
    "not official",
    "https://ielts.org/cdn/ielts-guides/ielts-writing-key-assessment-criteria.pdf",
    "../OFFICIAL_SAMPLE_CASES.md",
]

CELPIP_REQUIRED = [
    "Task 1 email",
    "Task 2 survey",
    "Content/Coherence",
    "Vocabulary",
    "Readability",
    "Task Fulfilment",
    "learning approximations",
    "dimensional ratings are transformed into a CELPIP level",
    "coaching estimates",
    "not official",
    "answer key",
    "../OFFICIAL_SAMPLE_CASES.md",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def label(path: Path) -> str:
    return str(path.relative_to(REPO_ROOT))


def parse_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        fail("missing YAML frontmatter")
    fields = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            fail(f"invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    if set(fields) != {"name", "description"}:
        fail(f"frontmatter fields must be only name and description, got {sorted(fields)}")
    if not re.fullmatch(r"[a-z0-9-]+", fields["name"]):
        fail(f"invalid skill name: {fields['name']}")
    if not fields["description"].startswith("Use when"):
        fail(f"description must start with 'Use when': {fields['name']}")
    if len(match.group(1)) > 1024:
        fail(f"frontmatter too long: {fields['name']}")
    return fields


def main() -> None:
    combined = ""
    all_public_files = PUBLIC_SKILLS + MIRROR_SKILLS + [
        VALIDATION,
        OFFICIAL_CASES,
        MIRROR_OFFICIAL_CASES,
        README,
        ROOT_README,
    ]
    for path in all_public_files:
        if not path.exists():
            fail(f"missing file: {label(path)}")
        text = path.read_text()
        combined += "\n" + text
        if path.name == "SKILL.md":
            parse_frontmatter(text)
        if "TODO" in text:
            fail(f"TODO left in {label(path)}")

    for term in FORBIDDEN:
        if term in combined:
            fail(f"forbidden public term found: {term}")
    for stale in [
        "A subagent was asked",
        "This note validates",
        "Score each criterion from 0-9, usually to the nearest 0.5",
        "Score each dimension 1-12",
        "weight Task 2 more heavily than Task 1 and state the weighting assumption",
    ]:
        if stale in combined:
            fail(f"stale overclaim or vague wording found: {stale}")

    for readme_path in [README, ROOT_README]:
        readme_text = readme_path.read_text()
        for term in README_REQUIRED:
            if term not in readme_text:
                fail(f"{label(readme_path)} missing public README term: {term}")

    mirror_pairs = [
        (
            ROOT / "celpip-writing-coach" / "SKILL.md",
            MIRROR_ROOT / "celpip-writing-coach" / "SKILL.md",
        ),
        (
            ROOT / "ielts-writing-coach" / "SKILL.md",
            MIRROR_ROOT / "ielts-writing-coach" / "SKILL.md",
        ),
        (
            ROOT / "celpip-writing-coach" / "agents" / "openai.yaml",
            MIRROR_ROOT / "celpip-writing-coach" / "agents" / "openai.yaml",
        ),
        (
            ROOT / "ielts-writing-coach" / "agents" / "openai.yaml",
            MIRROR_ROOT / "ielts-writing-coach" / "agents" / "openai.yaml",
        ),
        (OFFICIAL_CASES, MIRROR_OFFICIAL_CASES),
    ]
    for source, mirror in mirror_pairs:
        if not source.exists():
            fail(f"missing source file: {label(source)}")
        if not mirror.exists():
            fail(f"missing mirror file: {label(mirror)}")
        if source.read_text() != mirror.read_text():
            fail(f"skills mirror is stale: {label(mirror)} differs from {label(source)}")

    ielts_text = (ROOT / "ielts-writing-coach" / "SKILL.md").read_text()
    for term in IELTS_REQUIRED:
        if term not in ielts_text:
            fail(f"IELTS skill missing required term: {term}")

    celpip_text = (ROOT / "celpip-writing-coach" / "SKILL.md").read_text()
    for term in CELPIP_REQUIRED:
        if term not in celpip_text:
            fail(f"CELPIP skill missing required term: {term}")

    validation_text = VALIDATION.read_text()
    cases_text = OFFICIAL_CASES.read_text()
    for case in [
        "Source Attribution",
        "Official source title:",
        "Official source URL:",
        "Source role:",
        "Use official sample names, scores, and paraphrased examiner/source comments.",
        "Full Case Template",
        "Case IELTS-A2-7.5",
        "Case IELTS-A1-3.5",
        "Case IELTS-GT1-5.0",
        "Case CELPIP-W10",
        "Do not reproduce the full sample answer",
        "Official band: 7.5",
        "Official band: 3.5",
        "Official band: 5",
        "Skill estimate: 7.5. Official band: 7.5. Match.",
        "Skill estimate: 3.5. Official band: 3.5. Match.",
        "Skill estimate: 5.0. Official band: 5. Match.",
    ]:
        if case not in cases_text:
            fail(f"official sample cases missing required item: {case}")
    for profile in [
        "Academic Task 1 Response 1",
        "Academic Task 1 Response 2",
        "Academic Task 2 Response 1",
        "Academic Task 2 Response 2",
        "General Training Task 1 Script A",
        "General Training Task 2 Script A",
        "TR 5, CC 6, LR 5, GRA 5 -> 5.5",
        "TR 7-8, CC 7-8, LR 8, GRA 7 -> 7.5",
    ]:
        if profile not in validation_text:
            fail(f"validation note missing calibration profile: {profile}")
    for source in [
        "https://ielts.org/organisations/ielts-for-organisations/test-types/ielts-academic-test/academic-test-format-in-detail",
        "https://ielts.org/take-a-test/your-results/ielts-scoring-in-detail",
        "https://takeielts.britishcouncil.org/sites/default/files/academic-writing-sample-candidate-responses-and-examiner-comments.pdf",
        "https://takeielts.britishcouncil.org/sites/default/files/general-training-writing-sample-candidate-responses-and-examiner-comments.pdf",
        "https://www.celpip.ca/take-celpip/test-results/",
    ]:
        if source not in validation_text:
            fail(f"validation note missing source: {source}")

    print("public skill export validation passed")


if __name__ == "__main__":
    main()
