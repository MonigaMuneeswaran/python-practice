
from openai import OpenAI

client = OpenAI()

conversations = {}

def chatbot(user_message, user_id):

    if user_id not in conversations:
        conversations[user_id] = []

    history = conversations[user_id]

    history.append({
        "role": "user",
        "content": user_message
    })

    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=history
        )

        bot_reply = response.output_text

        history.append({
            "role": "assistant",
            "content": bot_reply
        })

        return bot_reply

    except Exception:
        history.pop()
        raise


if __name__ == "__main__":

    while True:
        user_id = input("\nEnter User ID (or exit): ")

        if user_id.lower() == "exit":
            print("Goodbye!")
            break

        message = input("You: ")

        reply = chatbot(message, user_id)

        print("Chatbot:", reply)
