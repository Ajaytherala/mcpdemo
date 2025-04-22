import asyncio
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from mcp_use import MCPAgent, MCPClient
import os


async def run_memory_chat():
    load_dotenv()
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

    config_file = "browser_mcp.json"

    print("Initializing the chat .....")

    client = MCPClient.from_config_file(config_file)

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.7,
        max_tokens=1000
    )

    agent = MCPAgent(
        llm=llm,
        client=client,
        max_steps=15,
        memory_enabled=True,
        
    )

    print("\n === Interactive MCP Chat ===\n")
    print("Type 'exit' to end the conversation.\n")
    print("Type 'clear' to clear the memory.\n")
    print("================================\n")

    try:
        while True:
            user_input = input("\n You: ")

            if user_input.lower() in ["exit", "quit"]:
                print("Exiting the chat .....")
                break
            
            if user_input.lower() == "clear":
                agent.clear_conversation_history()
                print("Conversation history cleared.")
                continue
            
            print("\n Assistant: ", end="", flush=True)

            try:
                response = await agent.run(user_input)
                print(response)

            except Exception as e:
                print(f"\n Error: {e}")


    finally:
        if client and client.sessions:
            await client.close_all_sessions()


if __name__ == "__main__":
    asyncio.run(run_memory_chat())





  
            
        



