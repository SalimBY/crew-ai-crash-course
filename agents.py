from crewai import Agent
from crewai.tools.base_tool import Tool
from textwrap import dedent
from crewai.llm import LLM
from tools.search_tools import SearchTools
from tools.calculator_tools import CalculatorTools

"""
Creating Agents Cheat Sheet:
- Think like a boss. Work backwards from the goal and think which employee 
    you need to hire to get the job done.
- Define the Captain of the crew who orient the other agents towards the goal. 
- Define which experts the captain needs to communicate with and delegate tasks to.
    Build a top down structure of the crew.

Goal:
- Create a 7-day travel itinerary with detailed per-day plans,
    including budget, packing suggestions, and safety tips.

Captain/Manager/Boss:
- Expert Travel Agent

Employees/Experts to hire:
- City Selection Expert 
- Local Tour Guide


Notes:
- Agents should be results driven and have a clear goal in mind
- Role is their job title
- Goals should actionable
- Backstory should be their resume
"""


class TravelAgents:
    def __init__(self, llm):
        self.llm = llm

        # Create tool instances
        search_tools = SearchTools()
        calculator_tools = CalculatorTools()
        
        # Fix the tool wrapping to handle arguments correctly
        self.search_tool = Tool(
            name="Search Tool",
            description="Useful to search the internet about a given topic and return relevant results",
            func=lambda query: search_tools.search_internet(query)
        )
        
        self.calculator_tool = Tool(
            name="Calculator Tool",
            description="Useful to perform mathematical calculations like sum, minus, multiplication, division, etc.",
            func=lambda operation: calculator_tools.calculate(operation)
        )

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(
                f"""Expert in travel planning and logistics. 
                I have decades of expereince making travel iteneraries."""),
            goal=dedent(f"""
                        Create a 7-day travel itinerary with detailed per-day plans,
                        include budget, packing suggestions, and safety tips.
                        """),
            tools=[
                self.search_tool,
                self.calculator_tool
            ],
            verbose=True,
            llm=self.llm
        )

    def city_selection_expert(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent(
                f"""Expert at analyzing travel data to pick ideal destinations"""),
            goal=dedent(
                f"""Select the best cities based on weather, season, prices, and traveler interests"""),
            tools=[self.search_tool],
            verbose=True,
            llm=self.llm
        )

    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent(f"""Knowledgeable local guide with extensive information
        about the city, it's attractions and customs"""),
            goal=dedent(
                f"""Provide the BEST insights about the selected city"""),
            tools=[self.search_tool],
            verbose=True,
            llm=self.llm
        )
