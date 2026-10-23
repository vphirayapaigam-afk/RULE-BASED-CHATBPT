"""Rule-Based AI Chatbot - DecodeLabs AI Project 1.

Architecture (IPO model):
    Input    -> read and sanitize (lowercase, strip whitespace/punctuation)
    Process  -> dictionary lookup (O(1)) instead of a long if-elif ladder
    Output   -> matched reply, or a fallback when nothing matches
"""

import random
import string
from datetime import datetime

BOT_NAME = "LogicBot"

# Exit commands: typing any of these ends the loop cleanly.
EXIT_COMMANDS = {"exit", "quit", "bye", "goodbye", "see you", "stop"}

# Knowledge base: each key is a sanitized user input, each value is the reply.
RESPONSES = {
    # Greetings
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! Nice to meet you.",
    "hey": "Hey! What's on your mind?",
    "good morning": "Good morning! Hope you have a great day.",
    "good evening": "Good evening! How was your day?",
    # Small talk
    "how are you": "I'm just code, but I'm running perfectly. Thanks for asking!",
    "what is your name": f"I'm {BOT_NAME}, a rule-based chatbot.",
    "who are you": f"I'm {BOT_NAME}, built with pure if-else logic and a dictionary.",
    "thanks": "You're welcome!",
    "thank you": "Happy to help!",
    # About AI / the project
    "what can you do": "I can chat about basics, tell jokes, and tell you the time. Type 'help' to see more.",
    "what is ai": "AI is the science of making machines do tasks that normally need human intelligence.",
    "what is a rule based chatbot": "It's a bot that replies using predefined rules, with no learning involved.",
    "help": "Try: hello, how are you, what is ai, tell me a joke, what time is it, bye.",
}

JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "Why did the developer go broke? He used up all his cache.",
    "There are 10 types of people: those who understand binary and those who don't.",
]

FALLBACK = "Sorry, I do not understand. Type 'help' to see what I can answer."


def sanitize(raw: str) -> str:
    """Normalize input: lowercase, trim, drop punctuation, collapse spaces."""
    cleaned = raw.lower().strip().translate(str.maketrans("", "", string.punctuation))
    return " ".join(cleaned.split())


def get_reply(clean_input: str) -> str:
    """Return the bot's reply for an already-sanitized input."""
    # Dynamic intents (answers that change each time) are handled first.
    if clean_input in {"tell me a joke", "joke"}:
        return random.choice(JOKES)
    if clean_input in {"what time is it", "time"}:
        return "It's " + datetime.now().strftime("%I:%M %p") + "."
    if clean_input in {"what is the date", "date", "what is today"}:
        return "Today is " + datetime.now().strftime("%A, %d %B %Y") + "."
    # Static intents: one atomic lookup + fallback.
    return RESPONSES.get(clean_input, FALLBACK)


def main() -> None:
    print(f"{BOT_NAME}: Hello! I'm {BOT_NAME}. Type 'help' for ideas or 'exit' to quit.")
    while True:  # the "heartbeat": runs until the kill command
        try:
            raw_input_text = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print(f"\n{BOT_NAME}: Goodbye!")
            break

        clean_input = sanitize(raw_input_text)

        if not clean_input:
            print(f"{BOT_NAME}: Please type something.")
            continue

        if clean_input in EXIT_COMMANDS:
            print(f"{BOT_NAME}: Goodbye! Have a great day.")
            break

        print(f"{BOT_NAME}: {get_reply(clean_input)}")


if __name__ == "__main__":
    main()
