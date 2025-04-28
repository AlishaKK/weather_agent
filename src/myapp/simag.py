from agents import Agent   ,Runner,AsyncOpenAI,OpenAIChatCompletionsModel,set_tracing_disabled,function_tool
from dotenv import load_dotenv
import os 

load_dotenv()
set_tracing_disabled(disabled=True)
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

BASE_URL = "https://openrouter.ai/api/v1"
MODEL = "mistralai/mistral-small-3.1-24b-instruct:free"

client = AsyncOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url=BASE_URL
)

@function_tool
def get_weather(city:str)->str:
    """
    get the current weather of the given city 
    """
    result = requests.get()
    return 
agent = Agent(
        name="Weather agent",
        instructions="You are a weather agent. You can provide weather information and  forecasts",
        model=OpenAIChatCompletionsModel(model=MODEL, openai_client=client),
        tools=[get_weather]
        
    )

result =  Runner.run_sync(
        agent,
        "What's the weather of the New york?",
    )
print(result.final_output)