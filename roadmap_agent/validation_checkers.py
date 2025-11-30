"""
Validation Checker Agents
Ensure quality of generated roadmaps and resources
"""

from typing import AsyncGenerator

from google.adk.agents import BaseAgent
from google.adk.agents.invocation_context import InvocationContext
from google.adk.events import Event, EventActions


class RoadmapValidationChecker(BaseAgent):
    """Validates that a roadmap outline meets quality standards."""
    
    async def _run_async_impl(
        self, context: InvocationContext
    ) -> AsyncGenerator[Event, None]:
        roadmap = context.session.state.get("roadmap_outline")
        
        if not roadmap:
            yield Event(author=self.name)
            return
        
        # Validation checks
        is_valid = True
        issues = []
        
        # Check length (should be substantial)
        if len(roadmap) < 500:
            is_valid = False
            issues.append("Roadmap too short")
        
        # Check for week structure
        week_count = roadmap.lower().count("week")
        if week_count < 4:
            is_valid = False
            issues.append(f"Expected 4 weeks, found {week_count}")
        
        # Check for daily breakdown
        day_mentions = roadmap.lower().count("day")
        if day_mentions < 15:  # At least 4-5 days per week
            is_valid = False
            issues.append("Insufficient daily breakdown")
        
        # Check for key components
        required_terms = ["objective", "learning", "practice"]
        missing_terms = [term for term in required_terms if term not in roadmap.lower()]
        if missing_terms:
            is_valid = False
            issues.append(f"Missing key terms: {', '.join(missing_terms)}")
        
        if is_valid:
            # Roadmap is valid, escalate to continue workflow
            yield Event(
                author=self.name,
                actions=EventActions(escalate=True),
            )
        else:
            # Roadmap is invalid, don't escalate (will trigger retry)
            print(f"Roadmap validation failed: {', '.join(issues)}")
            yield Event(author=self.name)


class ResourceValidationChecker(BaseAgent):
    """Validates that learning resources are properly curated."""
    
    async def _run_async_impl(
        self, context: InvocationContext
    ) -> AsyncGenerator[Event, None]:
        resources = context.session.state.get("learning_resources")
        
        if not resources:
            yield Event(author=self.name)
            return
        
        # Basic validation
        is_valid = True
        issues = []
        
        # Check for substantial content
        if len(resources) < 300:
            is_valid = False
            issues.append("Resources too brief")
        
        # Check for links (should contain URLs)
        if "http" not in resources:
            is_valid = False
            issues.append("No resource links found")
        
        # Check for resource types
        has_variety = (
            "video" in resources.lower() or 
            "article" in resources.lower() or 
            "course" in resources.lower()
        )
        if not has_variety:
            is_valid = False
            issues.append("Insufficient resource variety")
        
        if is_valid:
            yield Event(
                author=self.name,
                actions=EventActions(escalate=True),
            )
        else:
            print(f"Resource validation failed: {', '.join(issues)}")
            yield Event(author=self.name)


class DomainAnalysisChecker(BaseAgent):
    """Validates that domain research is comprehensive."""
    
    async def _run_async_impl(
        self, context: InvocationContext
    ) -> AsyncGenerator[Event, None]:
        analysis = context.session.state.get("domain_analysis")
        
        if not analysis:
            yield Event(author=self.name)
            return
        
        is_valid = True
        issues = []
        
        # Check for key sections
        required_sections = [
            "skills",
            "concepts", 
            "interview",
            "requirements"
        ]
        
        missing_sections = [
            section for section in required_sections 
            if section not in analysis.lower()
        ]
        
        if missing_sections:
            is_valid = False
            issues.append(f"Missing sections: {', '.join(missing_sections)}")
        
        # Check for substantial content
        if len(analysis) < 400:
            is_valid = False
            issues.append("Analysis too brief")
        
        if is_valid:
            yield Event(
                author=self.name,
                actions=EventActions(escalate=True),
            )
        else:
            print(f"Domain analysis validation failed: {', '.join(issues)}")
            yield Event(author=self.name)