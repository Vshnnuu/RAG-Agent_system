import os
from dotenv import load_dotenv
import vertexai

# Load .env file
load_dotenv()

PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION")

if not PROJECT_ID or not LOCATION:
    raise ValueError(
        "GOOGLE_CLOUD_PROJECT and GOOGLE_CLOUD_LOCATION must be set in the .env file."
    )

# Initialize Vertex AI SDK
vertexai.init(project=PROJECT_ID, location=LOCATION)

# Import the root agent so ADK knows this is the entrypoint
from .agent import root_agent

__all__ = ["root_agent"]
