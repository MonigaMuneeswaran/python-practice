
from openai import OpenAI

client = OpenAI()
history = []

def chatbot(user_input):

    history.append({
        "role": "user",
        "content": user_input
    })

    print(history)

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=history
    )

    bot_response = response.output_text

    print("Bot:", bot_response)

    history.append({
        "role": "assistant",
        "content": bot_response
    })

    return bot_response

