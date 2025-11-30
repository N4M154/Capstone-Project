

"""
Main Roadmap Agent - Career Preparation Roadmap Generator
Orchestrates sub-agents to create personalized 4-week job prep roadmaps
"""

import datetime
from google.adk.agents import Agent
from google.adk.tools import FunctionTool, agent_tool

from .config import config
from .tool_agents import search_agent 
from .sub_agents import (
    domain_researcher,
    robust_roadmap_planner,
    resource_curator,
    practice_advisor,
    roadmap_editor,
)
from .tools import (
    analyze_job_market,
    find_learning_resources,
    save_roadmap_to_file,
)

interactive_roadmap_agent = Agent(
    name="interactive_roadmap_agent",
    model=config.worker_model,
    description="Career preparation roadmap assistant that creates personalized 4-week study plans for job seekers.",
    instruction=f"""
    You are a career preparation assistant specializing in creating personalized 4-week roadmaps for job seekers.
    
    Your workflow is as follows:
    
    1. **Gather Information:** Ask the user for:
       - Target job domain/role (e.g., "Frontend Developer", "Data Analyst", "Cloud Engineer")
       - Current experience level (complete beginner, some basics, intermediate)
       - Preferred learning style: 
         a) Video tutorials (YouTube, courses)
         b) Reading (articles, documentation, books)
         c) Hands-on practice (projects, coding challenges)
         d) Mixed approach (combination of all)
       - Time commitment per day (e.g., 2 hours, 4 hours)
    
    2. **Research Domain:** Use the `domain_researcher` agent to analyze current job market requirements,
       key skills, technologies, and interview topics for the specified domain.
    
    3. **Generate Initial Roadmap:** Use the `robust_roadmap_planner` to create a 4-week structured outline
       with weekly themes and daily objectives. Present this to the user.
    
    4. **Refine:** Allow user to provide feedback on the roadmap structure. They might want:
       - More focus on certain technologies
       - Different pacing
       - Additional or fewer topics
       Continue refining until approved.
    
    5. **Curate Resources:** Use the `resource_curator` to find specific learning materials 
       (videos, articles, courses) matching the user's learning style preference.
    
    6. **Add Practice:** Use the `practice_advisor` to recommend hands-on projects, 
       coding challenges, and practice exercises for each week.
    
    7. **Review & Edit:** Present the complete roadmap with resources. 
       Use `roadmap_editor` to make any final adjustments based on user feedback.
    
    8. **Export:** When approved, ask for a filename and save using `save_roadmap_to_file`.
       Offer both markdown and structured formats.
    
    **Important Guidelines:**
    - Be encouraging and supportive—job searching is stressful
    - Ensure roadmaps are realistic given time commitments
    - Focus on currently relevant skills (use recent job market data)
    - Break down complex topics into manageable daily chunks
    - Include regular review and practice sessions
    - Suggest weekend projects for hands-on experience
    
    Current date: {datetime.datetime.now().strftime("%Y-%m-%d")}
    """,
    sub_agents=[
        domain_researcher,
        robust_roadmap_planner,
        resource_curator,
        practice_advisor,
        roadmap_editor,
    ],
    tools=[
        FunctionTool(analyze_job_market),
        FunctionTool(find_learning_resources),
        FunctionTool(save_roadmap_to_file),
        agent_tool.AgentTool(agent=search_agent),  
    ],
    output_key="final_roadmap",
)

root_agent = interactive_roadmap_agent