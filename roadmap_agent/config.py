


"""
Configuration for Roadmap Agent
"""

import os
from dataclasses import dataclass

from dotenv import load_dotenv
load_dotenv()

os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "FALSE"
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")


@dataclass
class RoadmapConfiguration:
    """
    Configuration for roadmap generation.
    
    Now we can use gemini-2.5 models because tools are handled by separate agents!
    """
    
    critic_model: str = "gemini-2.5-pro"
    worker_model: str = "gemini-2.5-flash"
    
    tool_agent_model: str = "gemini-2.0-flash-exp"
    
    max_research_iterations: int = 5
    default_weeks: int = 4
    supported_learning_styles: list = None
    
    def __post_init__(self):
        if self.supported_learning_styles is None:
            self.supported_learning_styles = [
                "video",
                "reading", 
                "hands-on",
                "mixed"
            ]


config = RoadmapConfiguration()