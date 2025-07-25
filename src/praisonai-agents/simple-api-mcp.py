from praisonaiagents import Agent, MCP

search_agent = Agent(
    instructions="""You are a Tweet.""",
    llm="openai/gpt-4o-mini",
    tools=MCP("http://localhost:8080/sse")
)
search_agent.launch(path="/tweet", port=3030)