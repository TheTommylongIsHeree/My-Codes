import openai

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Write a tagline for an ice cream shop."
)
