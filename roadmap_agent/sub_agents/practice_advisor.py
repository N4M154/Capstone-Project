

"""
Practice Advisor Agent
Recommends hands-on projects and practice exercises
"""

from google.adk.agents import Agent
from google.adk.tools import agent_tool

from ..config import config
from ..agent_utils import suppress_output_callback
from ..tool_agents import search_agent  

practice_advisor = Agent(
    model=config.worker_model,  # Using gemini-2.5-flash
    name="practice_advisor",
    description="Recommends practical projects and exercises to reinforce learning.",
    instruction="""
    You are a hands-on learning specialist and project mentor.
    
    [Your existing instruction...]
    
    Use the SearchAgent to find:
    - Current popular project ideas for the domain
    - Trending practice platforms
    - Example project implementations (for inspiration)
    
    Output detailed practice recommendations in markdown.
    Store in `practice_activities` state key.
    """,
    tools=[agent_tool.AgentTool(agent=search_agent)], 
    output_key="practice_activities",
    after_agent_callback=suppress_output_callback,
)