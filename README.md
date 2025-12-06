# learn_ai_agents
Repository folder to keep learnings on Vertex AI Agents & ADK



## first_ai_agent:

This is the first sample agent deployed using Google Vertex AI ADK. It used gemini-2.5-flash model and acts as an agent and can interact with it via web using adk web.

gcloud config set project <your-project-id>

gcloud services enable aiplatform.googleapis.com

mkdir ai-agents-adk
cd ai-agents-adk

uv venv --python 3.12
source .venv/bin/activate

uv pip install google-adk

adk create personal_assistant

Choose a model for the root agent:
1. gemini-2.5-flash
2. Other models (fill later)
Choose model (1, 2): 1

1. Google AI
2. Vertex AI
Choose a backend (1, 2): 2

Enter Google Cloud project ID [your-project-id]:
Enter Google Cloud region [us-central1]:

You should see a similar output in your terminal.


Agent created in /home/<your-username>/ai-agent-adk/personal_assistant:
- .env
- __init__.py
- agent.py

adk run personal_assistant



## bigquery-adk-codelab:

This agent interacts with BQ dataset ecommerce and responds to your questions



### References:
https://codelabs.developers.google.com/devsite/codelabs/build-agents-with-adk-foundation#0

https://codelabs.developers.google.com/bigquery-adk-eval?hl=en#0