import os
from dotenv import load_dotenv
load_dotenv()


DEBUG = os.getenv("DEBUG", "false").lower() == "true"

MCP_HOST = os.getenv("MCP_HOST", "0.0.0.0")
WEATHER_MCP_PORT = int(os.getenv("WEATHER_MCP_PORT", "8060"))
MCP_TRANSPORT = os.getenv("MCP_TRANSPORT", "http")


GEOCODING_URL = os.getenv("GEOCODING_URL","https://geocoding-api.open-meteo.com/v1/search")
WEATHER_URL = os.getenv("WEATHER_URL","https://api.open-meteo.com/v1/forecast")
