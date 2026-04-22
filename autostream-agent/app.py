from agent.intent import detect_intent
from agent.rag import load_knowledge, retrieve_answer
from agent.tools import mock_lead_capture

# Load knowledge base
db = load_knowledge()

# Global state
state = {
    "intent": None,
    "name": None,
    "email": None,
    "platform": None,
    "collecting": False
}


def reset_state():
    state["name"] = None
    state["email"] = None
    state["platform"] = None
    state["collecting"] = False


def chat(user_input):
    intent = detect_intent(user_input)

    # 🔥 Step 1: Detect high intent and start lead collection
    if intent == "high_intent" and not state["collecting"]:
        state["collecting"] = True
        return "Awesome! Let's get you started 🚀\nWhat's your name?"

    # 🔥 Step 2: Collect user details step-by-step
    if state["collecting"]:

        if not state["name"]:
            state["name"] = user_input
            return "Great! What's your email?"

        elif not state["email"]:
            if "@" not in user_input:
                return "Please enter a valid email."
            state["email"] = user_input
            return "Nice! Which platform do you create content on? (YouTube, Instagram, etc.)"

        elif not state["platform"]:
            state["platform"] = user_input

            # 🔥 Step 3: Call tool ONLY after all data collected
            mock_lead_capture(
                state["name"],
                state["email"],
                state["platform"]
            )

            reset_state()

            return "🎉 You're all set! Our team will reach out soon."

    # 🔥 Step 4: Normal conversation
    if intent == "greeting":
        return "Hey! 👋 Welcome to AutoStream. How can I help?\nYou can ask about pricing or plans."

    elif intent == "pricing":
        answer = retrieve_answer(user_input, db)
        return f"Here are our plans:\n{answer}\n\nWould you like to try one?"

    return "I can help with pricing, features, or getting started. What would you like to do?"


# 🔥 Chat loop
if __name__ == "__main__":
    print("🤖 AutoStream AI Assistant (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye! 👋")
            break

        response = chat(user_input)
        print("Bot:", response)