
"""
Roadmap Planner Agent
Creates structured 4-week learning roadmaps
"""

from google.adk.agents import Agent, LoopAgent
from google.adk.tools import agent_tool

from ..config import config
from ..agent_utils import suppress_output_callback
from ..validation_checkers import RoadmapValidationChecker
from ..tool_agents import search_agent  

roadmap_planner = Agent(
    model=config.critic_model,  # Using gemini-2.5-pro
    name="roadmap_planner",
    description="Creates a detailed 4-week learning roadmap with daily objectives.",
    instruction="""
    You are an expert instructional designer and career coach.
    
    Create a comprehensive 4-week roadmap based on:
    - Domain analysis (from `domain_analysis` state key)
    - User's experience level (from `experience_level` state key)
    - Daily time commitment (from `time_commitment` state key)
    - Learning style preference (from `learning_style` state key)
    
    [Rest of your instruction stays the same...]
    
    Use the SearchAgent to find current best practices for learning these technologies.
    
    Output the complete 4-week roadmap in detailed markdown format.
    Store in `roadmap_outline` state key.
    """,
    tools=[agent_tool.AgentTool(agent=search_agent)],  
    output_key="roadmap_outline",
    after_agent_callback=suppress_output_callback,
)

robust_roadmap_planner = LoopAgent(
    name="robust_roadmap_planner",
    description="Robust roadmap planner with validation and retry logic.",
    sub_agents=[
        roadmap_planner,
        RoadmapValidationChecker(name="roadmap_validation_checker"),
    ],
    max_iterations=3,
    after_agent_callback=suppress_output_callback,
)