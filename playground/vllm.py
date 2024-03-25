from openai import OpenAI
from helper import readfile
import time
# Modify OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8000/v1"
client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

t1 = time.time()
completion = client.completions.create(model="/home/ubuntu/models/llama-7b/",
                                      prompt=readfile(length=3000),
                                      max_tokens=1)
print("Completion result:", completion)
t2 = time.time()
print((t2-t1)*1000)