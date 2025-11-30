"""
Integration test for Roadmap Agent
Tests the complete workflow from domain selection to roadmap export
"""

import asyncio
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from roadmap_agent.agent import root_agent
from google.genai import types as genai_types


async def main():
    """Runs the roadmap agent with a sample conversation flow."""
    
    # Initialize session
    session_service = InMemorySessionService()
    await session_service.create_session(
        app_name="roadmap_app",
        user_id="test_user",
        session_id="test_session"
    )
    
    # Create runner
    runner = Runner(
        agent=root_agent,
        app_name="roadmap_app",
        session_service=session_service
    )
    
    # Simulate a complete conversation
    queries = [
        # Initial request
        "I want to prepare for a Frontend Developer job",
        
        # Respond to information gathering
        "I'm a complete beginner with programming. I prefer a mixed learning approach with videos and hands-on practice. I can dedicate 3 hours per day.",
        
        # Approve initial roadmap
        "This looks great! Please proceed with finding resources.",
        
        # Review resources
        "The resources look good. Can you add more hands-on projects?",
        
        # Final approval
        "Perfect! I'm ready to save this roadmap.",
        
        # Provide filename
        "frontend_developer_roadmap.md",
    ]
    
    print("=" * 80)
    print("ROADMAP AGENT INTEGRATION TEST")
    print("=" * 80)
    print()
    
    for i, query in enumerate(queries, 1):
        print(f"\n{'─' * 80}")
        print(f"Query {i}: {query}")
        print(f"{'─' * 80}\n")
        
        async for event in runner.run_async(
            user_id="test_user",
            session_id="test_session",
            new_message=genai_types.Content(
                role="user",
                parts=[genai_types.Part.from_text(text=query)]
            ),
        ):
            if event.is_final_response() and event.content and event.content.parts:
                response = event.content.parts[0].text
                print(f"Agent Response:\n{response}\n")
        
        # Small delay between queries
        await asyncio.sleep(1)
    
    print("\n" + "=" * 80)
    print("TEST COMPLETED")
    print("=" * 80)


async def test_single_query():
    """Quick test with a single query."""
    
    session_service = InMemorySessionService()
    await session_service.create_session(
        app_name="roadmap_app",
        user_id="quick_test",
        session_id="quick_session"
    )
    
    runner = Runner(
        agent=root_agent,
        app_name="roadmap_app",
        session_service=session_service
    )
    
    query = "I want to become a Data Analyst. Can you help me create a study plan?"
    
    print(f"Query: {query}\n")
    
    async for event in runner.run_async(
        user_id="quick_test",
        session_id="quick_session",
        new_message=genai_types.Content(
            role="user",
            parts=[genai_types.Part.from_text(text=query)]
        ),
    ):
        if event.is_final_response() and event.content and event.content.parts:
            print(f"Response:\n{event.content.parts[0].text}")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--quick":
        # Quick single-query test
        asyncio.run(test_single_query())
    else:
        # Full integration test
        asyncio.run(main())