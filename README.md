# AI Industry Digest Crew

A CrewAI workflow that researches the latest AI and LLM developments, organizes the findings, and writes a sourced daily digest in Markdown.

![Python](https://img.shields.io/badge/Python-3.10--3.13-3776AB?style=flat&logo=python&logoColor=white)
![CrewAI](https://img.shields.io/badge/CrewAI-0.201-FF5A50?style=flat)
![Tavily](https://img.shields.io/badge/Search-Tavily-166534?style=flat)
![License](https://img.shields.io/badge/License-MIT-6D28D9?style=flat)

## What it does

The crew turns a broad request for recent AI news into a structured report through three specialized agents:

1. An **AI Industry Researcher** searches the previous 24 hours for model releases, research, events, collaborations, and announcements.
2. An **AI Trends Analyst** groups the findings and condenses each item into a short, plain-language summary.
3. An **AI Industry Reporter** produces `daily_ai_digest.md` with categorized updates and source links.

The agents run sequentially, so each stage builds on the output of the previous one.

## Architecture

```mermaid
flowchart LR
    run[Run crew with today's date] --> research[Researcher uses Tavily to collect 10-15 sourced findings]
    research --> analysis[Analyst categorizes and summarizes findings]
    analysis --> report[Reporter writes the daily digest]
    report --> output[daily_ai_digest.md]

    classDef entry fill:#0969DA,stroke:#79C0FF,color:#FFFFFF,stroke-width:2px
    classDef process fill:#334155,stroke:#CBD5E1,color:#FFFFFF,stroke-width:2px
    classDef service fill:#166534,stroke:#86EFAC,color:#FFFFFF,stroke-width:2px
    classDef output fill:#9F1239,stroke:#FDA4AF,color:#FFFFFF,stroke-width:2px

    class run entry
    class research service
    class analysis,report process
    class output output
```

The agent roles and goals live in [`agents.yaml`](src/ai_industry_digest_crew/config/agents.yaml); task prompts and the output file are defined in [`tasks.yaml`](src/ai_industry_digest_crew/config/tasks.yaml).

## Tech stack

- Python 3.10-3.13
- CrewAI for sequential multi-agent orchestration
- Tavily for web search
- An LLM provider supported by CrewAI; the example environment uses OpenAI
- uv for dependency and environment management

## Setup and run

Prerequisites: [uv](https://docs.astral.sh/uv/) and API keys for Tavily and your CrewAI LLM provider.

```bash
git clone https://github.com/parthkulshreshtha/ai-industry-digest-crew.git
cd ai-industry-digest-crew

uv sync --locked
cp .env.example .env
# Add your API keys to .env

uv run crewai run
```

The completed report is written to `daily_ai_digest.md` in the project root. Each run replaces that file.

You can also invoke the project entry point directly:

```bash
uv run ai-industry-digest
```

CrewAI's training, replay, and evaluation helpers remain available:

```bash
uv run train <iterations> <output-file>
uv run replay <task-id>
uv run test <iterations> <evaluation-model>
```

## Configuration

Edit the YAML files under `src/ai_industry_digest_crew/config/` to change agent responsibilities, categories, report structure, or the number of requested findings. Never commit a populated `.env` file.

## Current scope

This repository is a local CLI workflow. It does not schedule runs, publish reports, provide a web interface, or independently verify every claim returned by its search and language-model providers. Review sources before sharing a generated digest.

## License

Released under the [MIT License](LICENSE).
