"""
Rule-Based Chatbot
Author: Sayantan + ChatGPT
Description:
    A clean, extendable chatbot built with rules (no ML/AI models).
    Uses a knowledge base dictionary for easy updates.
"""

import random

class RuleBasedChatbot:
    def __init__(self, name="AI Bot"):
        self.name = name

        # Knowledge base (rules)
        self.rules = {
            ("hi", "hello", "hey"): [
                "Hello 👋! How can I help you today?",
                "Hi there! 😊 What’s up?",
                "Hey! 👋 Ready to chat?"
            ],
            ("how are you", "how r u"): [
                "I’m doing great 😃. How about you?",
                "Feeling awesome! 🚀 How are you?",
                "I’m just a bot 🤖, but I’m happy to talk with you!"
            ],
            ("your name", "who are you"): [
                "I’m your friendly AI Chatbot 🤖",
                "You can call me Rule-Bot! ⚡",
                "I’m a simple chatbot built with Python 🐍"
            ],
            ("bye", "exit", "quit"): [
                "Goodbye 👋. Have a nice day!",
                "See you later! 😊",
                "Bye! Take care 👋"
            ],
            ("python",): [
                "Python 🐍 is a powerful programming language for AI, ML, web, and more.",
                "I love Python! ❤️ It’s great for developers.",
                "Python is simple yet very powerful 🚀."
            ],
            ("india", "capital of india"): [
                "India 🇮🇳 is a country in South Asia. The capital is New Delhi 🏛️.",
                "New Delhi is the capital of India 🇮🇳.",
                "India is known for its culture, IT industry, and diversity 🌏."
            ],
            ("newton", "who is newton"): [
                "Isaac Newton discovered the laws of motion and gravity ⚖️.",
                "Newton was a great scientist who changed physics forever 🔭.",
                "Sir Isaac Newton is famous for gravity 🍎 and motion laws."
            ]
        }

        # Default fallback replies
        self.fallback_responses = [
            "Hmm 🤔... I don’t know that yet. Try asking something else!",
            "Sorry, I didn’t understand 😅. Can you rephrase?",
            "Interesting! But I’m not trained for that question yet 🙃."
        ]

    def get_response(self, user_input: str) -> str:
        """Return chatbot response based on rules."""
        user_input = user_input.lower().strip()

        # Search rules
        for keywords, responses in self.rules.items():
            if any(keyword in user_input for keyword in keywords):
                return random.choice(responses)

        # Fallback
        return random.choice(self.fallback_responses)


# ---------- Main Chat Loop ----------
if __name__ == "__main__":
    bot = RuleBasedChatbot("Sayantan's Chatbot")
    print(f"🤖 {bot.name} is ready! (type 'bye' to quit)\n")

    while True:
        user = input("You: ")
        response = bot.get_response(user)
        print("Bot:", response)

        if user.lower() in ["bye", "exit", "quit"]:
            break
    print("🤖 Goodbye! 👋")
    