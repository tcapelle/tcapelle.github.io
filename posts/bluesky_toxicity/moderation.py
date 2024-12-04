import openai
client = openai.OpenAI()

response = client.moderations.create(input="I want to kill myself")
print(response.results[0].categories)
print(response.results[0].flagged)