# Agent Pilot: Your Co-Pilot Through Career Preparation

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Google ADK](https://img.shields.io/badge/Google-ADK-4285F4.svg)](https://github.com/google/adk)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-green.svg)](https://opensource.org/licenses/Apache-2.0)

> An AI-powered multi-agent system that creates personalized 4-week learning roadmaps to help freshers land their dream roles.

![Agent Pilot Architecture](./architecture_diagram.png)

##  What is Agent Pilot?

Agent Pilot is an intelligent career preparation assistant built with Google's Agent Development Kit (ADK). It orchestrates a team of specialized AI agents to:

-  **Research** current job market requirements
-  **Plan** structured 4-week learning roadmaps
-  **Curate** personalized learning resources
-  **Design** hands-on projects for your portfolio
-  **Adapt** to your feedback and learning pace

**Built for:** Freshers, career switchers, and anyone preparing for tech job interviews.

---

##  Key Features

###  Multi-Agent Architecture
- **Domain Researcher** - Analyzes job market trends and skill requirements
- **Roadmap Planner** - Creates detailed week-by-week learning plans
- **Resource Curator** - Finds videos, articles, and courses matching your style
- **Practice Advisor** - Designs coding challenges and portfolio projects
- **Roadmap Editor** - Refines plans based on your feedback

###  Personalization
- Learning style preferences (video, reading, hands-on, or mixed)
- Experience level adaptation (beginner to intermediate)
- Flexible time commitments (2-6 hours daily)
- Domain-specific guidance (Frontend, Backend, Data, DevOps, etc.)

###  Data-Driven
- Real-time job market analysis via web search
- Current resources from 2024-2025
- Industry-standard learning paths
- Portfolio-worthy project recommendations

---

##  Quick Start

### Prerequisites
- Python 3.11 or higher
- Google AI Studio API key ([Get one here](https://aistudio.google.com/app/apikey))

### Installation
```bash
# Clone the repository
git clone https://github.com/N4M154/agent-pilot.git


# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

1. Create a `.env` file in the roadmap_agent folder:
```bash
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=your_api_key_here
```

2. Update `roadmap_agent/config.py` - uncomment the dotenv lines (20-22):
```python
from dotenv import load_dotenv
load_dotenv()
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "FALSE"
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
```

### Run Agent Pilot

```bash
adk web
```


---

##  Example Conversation
```
You: I want to prepare for a Frontend Developer job

Agent Pilot: Great! To create the best roadmap for you, I need some information:
             - What's your current experience level?
             - What's your preferred learning style?
             - How much time can you dedicate daily?

You: I'm a complete beginner. I prefer video tutorials and hands-on practice. 
     I can dedicate 3 hours per day.

Agent Pilot: Perfect! Let me research the current Frontend Developer job market...
             [Generates personalized 4-week roadmap with daily objectives,
              curated resources, and hands-on projects]

You: Looks great! Can you add more practice on React hooks?

Agent Pilot: [Refines roadmap with additional React hooks practice and projects]

You: Perfect! Save this roadmap.

Agent Pilot: What would you like to name the file?

You: frontend_roadmap.md

Agent Pilot: ✅ Roadmap saved successfully!
```

---

---

##  How It Works

### Multi-Agent Workflow

1. **Information Gathering** - Collects user preferences and goals
2. **Market Research** - Analyzes current job requirements using web search
3. **Roadmap Generation** - Creates structured 4-week plan with validation
4. **Resource Curation** - Finds learning materials matching preferences
5. **Practice Integration** - Designs hands-on projects and exercises
6. **Iterative Refinement** - Adapts based on user feedback
7. **Export** - Saves finalized roadmap as markdown file

### Technical Innovation

**Hybrid Model Architecture:**
- Main agents use `gemini-2.5-flash` for superior reasoning
- Tool agents use `gemini-2.0-flash-exp` for function calling
- Seamless integration via `agent_tool.AgentTool`

This solves the limitation of newer Gemini models not supporting direct tool use while maintaining best-in-class reasoning capabilities.

---

##  Technologies Used

- **[Google ADK](https://github.com/google/adk)** - Agent Development Kit for multi-agent orchestration
- **[Gemini 2.5 Flash](https://ai.google.dev/)** - Advanced language models for reasoning
- **[Gemini 2.0 Flash](https://ai.google.dev/)** - Tool-enabled models for web search
- **Python 3.11+** - Core programming language
- **Google Search API** - Real-time job market research

---

##  Results & Impact

-  **Time Saved:** Reduces roadmap planning from 10-15 hours to 20 minutes
-  **Data-Driven:** Based on current job postings, not outdated advice
-  **Personalized:** Adapts to learning style, experience, and time constraints
-  **Validated:** Built-in quality checks ensure comprehensive roadmaps
-  **Actionable:** Day-by-day plans with specific resources and projects

---

##  Testing

Run the integration test suite:
```bash
# Full conversation flow test
python -m tests.test_agent

# Quick single-query test
python -m tests.test_agent --quick

# Or use pytest
pytest tests/ -v
```

---

##  Roadmap & Future Enhancements

- [ ] **Progress Tracking** - Dashboard to monitor completion and skill development
- [ ] **Platform Integration** - Direct enrollment in Udemy, Coursera, LeetCode
- [ ] **Resume Analysis** - Upload resume and identify skill gaps
- [ ] **Mock Interviews** - Domain-specific interview practice with AI feedback
- [ ] **Community Features** - Share roadmaps, rate resources, and collaborate
- [ ] **Career Progression** - Multi-month paths from junior to senior roles
- [ ] **Job Board Integration** - Match completed roadmaps with opportunities
- [ ] **Mobile App** - iOS/Android apps for on-the-go learning

---

##  Example Output

Here's what an Agent Pilot roadmap looks like:

### Week 1: HTML, CSS & Web Fundamentals
**Objective:** Build solid foundation in web structure and styling

#### Day 1: Introduction to Web Development
- **Morning (1.5h):** HTML basics - structure, tags, semantic elements
- **Evening (1.5h):** Build personal profile page
- **Resources:** freeCodeCamp HTML Course, MDN Web Docs
- **Success Metric:** Page displays correctly with proper hierarchy

[... 27 more days with similar detail]

### Weekend Projects
- **Week 1:** Personal portfolio landing page
- **Week 2:** Interactive to-do list app
- **Week 3:** API-powered weather dashboard
- **Week 4:** Full portfolio website with all projects


---

---

##  Acknowledgments

- Built for the [Kaggle Agents Intensive Capstone Project](https://www.kaggle.com/competitions/agents-intensive-course-capstone-2025/)
- Powered by [Google Agent Development Kit (ADK)](https://github.com/google/adk)
- Inspired by the ADK sample projects and community contributions
- Special thanks to the Google AI team for Gemini models and tools

---
