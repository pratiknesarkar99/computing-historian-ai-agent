# Before running the sample:
#    pip install azure-ai-projects>=2.1.0

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

endpoint = "https://pratiknesarkar-2338-dem-resource.services.ai.azure.com/api/projects/pratiknesarkar-2338-demo1"

project_client = AIProjectClient(
    endpoint=endpoint,
    credential=DefaultAzureCredential(),
)

my_agent = "computing-historian"
my_version = "1"

openai_client = project_client.get_openai_client()

# Iteratively prompt the user and get responses from the agent
while True:
    user_input = input("Enter a prompt for the agent (or 'quit' to exit): ").strip()
    
    if user_input.lower() == "quit":
        print("Goodbye!")
        break
    
    if not user_input:
        print("Please enter a prompt.\n")
        continue
    
    # Reference the agent to get a response
    response = openai_client.responses.create(
        input=[{"role": "user", "content": user_input}],
        extra_body={"agent_reference": {"name": my_agent, "version": my_version, "type": "agent_reference"}},
    )
    
    print(f"Agent response: {response.output_text}\n")



