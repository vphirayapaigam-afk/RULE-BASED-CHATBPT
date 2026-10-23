# Rule-Based AI Chatbot

A simple chatbot built with pure control flow and a dictionary (DecodeLabs AI Project 1).

## Features
- Continuous `while True` input loop
- Input sanitization (lowercase, trim, remove punctuation)
- Dictionary knowledge base with 10+ intents and a `.get()` fallback
- Dynamic replies: jokes, time, date
- Clean exit with `exit`, `quit`, `bye`, or Ctrl+C

## Run
```bash
python chatbot.py
```
Requires Python 3.8+. No external packages.

## Test
```bash
python -m unittest -v
```

## Example
```
You: Hello!
LogicBot: Hi there! How can I help you today?
You: what is AI?
LogicBot: AI is the science of making machines do tasks that normally need human intelligence.
You: bye
LogicBot: Goodbye! Have a great day.
```

## Extend it
Add new entries to the `RESPONSES` dictionary in `chatbot.py`.
