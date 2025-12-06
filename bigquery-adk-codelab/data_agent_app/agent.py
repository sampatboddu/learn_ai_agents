from google.adk.agents.llm_agent import Agent
from google.adk.tools.bigquery import BigQueryCredentialsConfig, BigQueryToolset
import google.auth
import dotenv

dotenv.load_dotenv()

credentials, _ = google.auth.default()
credentials_config = BigQueryCredentialsConfig(credentials=credentials)
bigquery_toolset = BigQueryToolset(
  credentials_config=credentials_config
)

root_agent = Agent(
 model="gemini-2.5-flash",
 name="bigquery_agent",
 description="Agent that answers questions about BigQuery data by executing SQL queries.",
 instruction=(
     """
     You are a data analysis agent with access to several BigQuery tools.
     Use the appropriate tools to fetch relevant BigQuery metadata and execute SQL queries.
     You must use these tools to answer the user's questions.
     Run these queries in the project-id: 'sam-ai-agents' on the `ecommerce` dataset.
    """
 ),
 tools=[bigquery_toolset]
)

def get_bigquery_agent():
 return root_agent
