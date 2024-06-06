import json
import os

def load_responses(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File {filename} not found.")
    with open(filename, 'r') as file:
        try:
            responses = json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error reading JSON from file {filename}: {e}")
    return responses

def get_response(user_input, user_role, responses):
    user_input = user_input.lower()
    for entry in responses:
        if entry["user_role"] == user_role and entry["user_input"].lower() == user_input:
            return entry["bot_response"]
    for entry in responses:
        if entry["user_role"] == user_role and entry["user_input"] == "default":
            return entry["bot_response"]
    return "Sorry, I don't understand."

def main():
    try:
        responses = load_responses('dialog_responses.json')
    except (FileNotFoundError, ValueError) as e:
        print(e)
        return

    print("Chatbot: Hi! I'm the developer. (Type 'bye' to exit)")

    while True:
        user_input = input("Client: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = get_response(user_input, "client", responses)
        print(f"Developer: {response}")

if __name__ == "__main__":
    main()
