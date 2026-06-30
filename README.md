# Weather MCP Server Demo

Simple Weather MCP Server that utilizes: open-meteo.com services.


To run it locally, just clone the git repository and execute the following:

```
# Create virtual environment
python3 -m venv .venv

# Activate it (macOS/Linux)
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the server
python server.py
```

To run it over OpenShift you can run the following commands:

```
# Create new OpenShift project
oc new-project weather-mcp

# Create the Weather MCP server application using S2I
oc new-app python:3.12-minimal-ubi10~https://github.com/osa-ora/weather-mcp-server --name=weather-mcp-server -n weather-mcp

# Expose it, if you want to access it from outside the cluster.
oc expose svc/weather-mcp-server -n weather-mcp

```
