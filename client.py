from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)