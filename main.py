from ollama import Client

client = Client("http://localhost:11434")

response = client.chat(
  model="qwen2.5",
  messages=[
    {
      "role": "user",
      "content": "Tell me a joke",
    }
  ]
)

print(response["message"]["content"])