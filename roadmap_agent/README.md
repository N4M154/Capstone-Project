## Project Overview - Career Prep Roadmap Agent

This project contains the core logic for a multi-agent system designed to help job seekers create personalized 4-week preparation roadmaps. Built using Google Agent Development Kit (ADK), it follows a modular architecture to generate tailored study plans based on domain expertise and learning preferences.

### Problem Statement

Job preparation for freshers is overwhelming due to the vast amount of resources available and unclear prioritization of topics. Without a structured approach, candidates often waste time on irrelevant materials or miss critical concepts employers expect. The lack of personalization means that visual learners may struggle with text-heavy resources, while those preferring hands-on practice might get stuck in tutorial hell. Manual roadmap creation requires extensive research into job market trends, skill requirements, and effective learning resources—a time-consuming process that delays actual preparation.

### Solution Statement

An AI-powered multi-agent system can automatically research current job market requirements for specific domains, analyze skill gaps, and generate personalized 4-week roadmaps tailored to individual learning styles. The agent synthesizes information from job postings, industry trends, and educational resources to create week-by-week plans with clear daily objectives. It recommends appropriate learning materials (videos, articles, practice problems) based on user preferences and adjusts difficulty progression to ensure steady skill development. This transforms job preparation from a scattered, anxiety-inducing process into a structured, confidence-building journey.

### Architecture

The system is built around the `roadmap_agent`—a sophisticated multi-agent orchestrator that coordinates specialized agents for research, planning, content curation, and personalization. The central coordinator is the `interactive_roadmap_agent`.

**Core Agents:**

**Domain Researcher: `domain_research_agent`**
Analyzes the job market for the specified domain, identifying key skills, technologies, and interview topics currently in demand. Uses web search to gather real-time job posting data and industry trends.

**Roadmap Planner: `robust_roadmap_planner`**
Creates a comprehensive 4-week structured outline with week-by-week themes and daily learning objectives. Implements progressive difficulty and ensures realistic time commitments. Uses `RoadmapValidationChecker` to ensure quality.

**Resource Curator: `resource_curator_agent`**
Finds and organizes learning resources (videos, articles, documentation, practice platforms) matching the user's learning style preference. Prioritizes high-quality, up-to-date materials.

**Practice Advisor: `practice_advisor_agent`**
Recommends hands-on projects, coding challenges, and mock interview questions for each week to reinforce learning through application.

**Roadmap Refiner: `roadmap_editor`**
Iteratively improves the roadmap based on user feedback, adjusting difficulty, pacing, or focus areas as needed.

### Essential Tools and Utilities

**Job Market Analysis (`analyze_job_market`)**
Searches current job postings for the specified domain and extracts common skill requirements, technologies, and experience levels.

**Resource Search (`find_learning_resources`)**
Searches for high-quality learning materials filtered by resource type (video, article, interactive) and difficulty level.

**Roadmap Export (`save_roadmap_to_file`)**
Exports the finalized roadmap as a markdown or PDF file for easy reference during preparation.

**Validation Checkers (`RoadmapValidationChecker`, `ResourceValidationChecker`)**
Ensure the generated roadmap meets quality standards: realistic time commitments, progressive difficulty, clear objectives, and verified resource links.

### Workflow

1. **Domain Discovery:** User specifies target job domain (e.g., "Frontend Developer", "Data Analyst", "DevOps Engineer")
2. **Learning Style:** User indicates preference (video-based, reading/articles, hands-on projects, or mixed)
3. **Research:** Agent analyzes current job market requirements for the domain
4. **Plan:** Generates initial 4-week roadmap outline with weekly themes
5. **Refine:** User provides feedback to adjust focus areas or pacing
6. **Curate:** Agent finds specific learning resources matching preferences
7. **Practice:** Adds recommended projects and exercises for each week
8. **Review:** User approves or requests modifications
9. **Export:** Saves finalized roadmap as downloadable file

### Value Statement

This agent eliminates the 10-15 hours typically spent researching and planning job preparation, providing a structured path from day one. By personalizing to learning styles, it increases engagement and retention. The research-backed approach ensures candidates focus on currently relevant skills rather than outdated tutorials, improving job-ready confidence and interview performance.

**Future Enhancements:**

- Progress tracking dashboard
- Integration with learning platforms (Udemy, Coursera, LeetCode)
- Skill gap analysis with resume upload
- Community-sourced roadmap ratings
- Interview preparation module with mock questions
- Career path progression (junior → mid-level → senior)

## Project Structure

```
roadmap_agent/
├── __init__.py
├── agent.py                    # Main orchestrator agent
├── config.py                   # Model and parameter configuration
├── agent_utils.py              # Shared utilities
├── tools.py                    # Custom tools for job market analysis
├── validation_checkers.py      # Quality validation agents
└── sub_agents/
    ├── __init__.py
    ├── domain_researcher.py    # Job market analysis
    ├── roadmap_planner.py      # 4-week plan generation
    ├── resource_curator.py     # Learning material finder
    ├── practice_advisor.py     # Project recommendations
    └── roadmap_editor.py       # Iterative refinement
tests/
├── test_agent.py              # Integration tests
eval/
├── evaluation.py              # Roadmap quality metrics
```

## Installation

```bash
# Create virtual environment (Python 3.11+)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run in ADK web mode
adk web

# Run integration test
python -m tests.test_agent
```

## Example Usage

```
User: "I want to prepare for a Data Analyst role"
Agent: "Great! To create the best roadmap for you, what's your preferred learning style?
        1. Video tutorials
        2. Reading articles and documentation
        3. Hands-on projects
        4. Mixed approach"

User: "Mixed approach"
Agent: [Generates 4-week roadmap with SQL, Python, Excel, and visualization tools,
        mixing video courses, articles, and practice datasets]
```
