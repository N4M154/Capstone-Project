

"""
Resource Curator Agent
Finds and organizes learning resources
"""

from google.adk.agents import Agent
from google.adk.tools import agent_tool

from ..config import config
from ..agent_utils import suppress_output_callback
from ..tool_agents import search_agent  

resource_curator = Agent(
    model=config.worker_model,  # Using gemini-2.5-flash
    name="resource_curator",
    description="Finds high-quality learning resources matching user preferences.",
    instruction="""
    You are a learning resource curator with expertise in educational content.
    
    [Your existing instruction...]
    
    Use the SearchAgent extensively to find the best current resources.
    Delegate searches like:
    - "Search for '[topic] tutorial 2025'"
    - "Search for 'best [topic] course for beginners'"
    - "Search for '[topic] practice exercises'"
    
    Output in detailed markdown format with clickable links.
    Store in `learning_resources` state key.
    """,
    tools=[agent_tool.AgentTool(agent=search_agent)],  
    output_key="learning_resources",
    after_agent_callback=suppress_output_callback,
)