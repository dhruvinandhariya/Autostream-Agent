def detect_intent(user_input):
    text = user_input.lower()

    # High intent (priority)
    if any(x in text for x in ["buy", "subscribe", "start", "try", "want"]):
        return "high_intent"

    # Pricing
    if any(x in text for x in ["price", "pricing", "plan", "cost", "features"]):
        return "pricing"

    # Greeting (lowest priority)
    if any(x in text for x in ["hi", "hello", "hey"]):
        return "greeting"

    return "general"