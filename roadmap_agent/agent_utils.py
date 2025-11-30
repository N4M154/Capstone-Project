"""
Utility functions for agents
"""

from google.adk.agents.callback_context import CallbackContext
from google.genai.types import Content


def suppress_output_callback(callback_context: CallbackContext) -> Content:
    """
    Suppresses the output of sub-agents to avoid redundant responses.
    The main agent will present the final results to the user.
    
    Args:
        callback_context: Context from the agent callback
    
    Returns:
        Empty Content object to suppress output
    """
    return Content()