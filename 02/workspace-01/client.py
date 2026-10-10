import json
from urllib.request import Request, urlopen


GRAPHQL_URL = "http://127.0.0.1:8000/graphql"

query = """
{
  books {
    title
    author
  }
}
"""

payload = json.dumps({"query": query}).encode("utf-8")

request = Request(
    GRAPHQL_URL,
    data=payload,
    headers={"Content-Type": "application/json"},
    method="POST",
)

with urlopen(request) as response:
    result = json.loads(response.read().decode("utf-8"))

print(json.dumps(result, indent=2))