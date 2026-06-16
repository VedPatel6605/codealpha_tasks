import random
import time


# ── Response rules ─────────────────────────────────────────────────────────────

RESPONSES = {
    # Greetings
    ("hello", "hi", "hey", "hiya", "howdy", "good morning", "good evening",
     "good afternoon"): [
        "Hey there! 👋 How can I help you today?",
        "Hi! Great to see you. What's on your mind?",
        "Hello! I'm here and ready to chat. 😊",
    ],

    # How are you
    ("how are you", "how are you doing", "how do you do", "how's it going",
     "what's up", "whats up", "how r u", "you okay", "are you okay"): [
        "I'm doing great, thanks for asking! 😄 How about you?",
        "Feeling fantastic! I'm an AI so I'm always ready to help. 🚀",
        "All systems running smoothly! What can I do for you?",
    ],

    # Name
    ("what is your name", "whats your name", "who are you",
     "what are you called", "your name"): [
        "I'm ChatBot 🤖 — your friendly Python-powered chatbot!",
        "Call me ChatBot! Built with Python for CodeAlpha internship. 🐍",
    ],

    # Creator / made by
    ("who made you", "who created you", "who built you",
     "who programmed you", "who is your creator"): [
        "I was built as part of the CodeAlpha Python Internship program! 🎓",
        "A Python developer created me for the CodeAlpha internship Task 4. 💻",
    ],

    # What can you do
    ("what can you do", "help", "how can you help", "what do you know",
     "capabilities", "features"): [
        "I can chat with you, answer questions, tell jokes, share quotes, and more! Just try me. 😄",
        "I'm a rule-based chatbot. Try asking me: my name, a joke, the time, or just say hello!",
    ],

    # Time
    ("what time is it", "current time", "tell me the time", "time"): [
        f"The current time is: {time.strftime('%I:%M %p')} 🕐",
    ],

    # Date
    ("what is today", "today's date", "what date is it",
     "current date", "date today"): [
        f"Today is {time.strftime('%A, %d %B %Y')} 📅",
    ],

    # Jokes
    ("tell me a joke", "joke", "make me laugh", "say something funny", "humor"): [
        "Why do Python programmers prefer dark mode? Because light attracts bugs! 🐛😂",
        "Why did the programmer quit his job? Because he didn't get arrays! 😄",
        "How many programmers does it take to change a light bulb? None — it's a hardware problem! 💡",
        "Why is Python the best language? Because it doesn't have to C anything! 🐍😂",
    ],

    # Quotes / Motivation
    ("motivate me", "inspire me", "give me a quote", "quote",
     "motivation", "inspiration"): [
        "\"Code is like humor. When you have to explain it, it's bad.\" — Cory House 💬",
        "\"The best way to predict the future is to create it.\" — Abraham Lincoln 🌟",
        "\"First, solve the problem. Then, write the code.\" — John Johnson 💡",
        "\"In the middle of every difficulty lies opportunity.\" — Albert Einstein ✨",
    ],

    # Python
    ("python", "tell me about python", "what is python", "i love python"): [
        "Python is awesome! 🐍 It's readable, powerful, and used everywhere — from AI to web dev.",
        "Python is one of the most popular languages in the world. Great choice! 🚀",
    ],

    # CodeAlpha
    ("codealpha", "code alpha", "internship", "about codealpha"): [
        "CodeAlpha is a leading software company offering amazing internship programs! 🎓",
        "CodeAlpha helps students gain real-world programming experience. Great place to learn! 💼",
    ],

    # Feelings
    ("i am sad", "i feel sad", "i'm sad", "i am not okay",
     "feeling low", "i'm upset"): [
        "I'm sorry to hear that. 💙 Remember: tough times don't last. You've got this!",
        "It's okay to feel sad sometimes. Take a deep breath — better days are coming. 🌈",
    ],

    ("i am happy", "i'm happy", "i feel great", "feeling good",
     "i am excited", "i'm excited"): [
        "That's wonderful to hear! 😄 Keep that positive energy going!",
        "Yay! Happiness is contagious! 🎉 What's the good news?",
    ],

    # Goodbye
    ("bye", "goodbye", "see you", "see ya", "take care", "quit", "exit",
     "cya", "later", "farewell"): [
        "Goodbye! 👋 It was great chatting with you!",
        "See you later! Keep coding! 🚀",
        "Bye! Have an amazing day! 😊",
    ],

    # Thanks
    ("thank you", "thanks", "thx", "thank u", "ty", "thanks a lot"): [
        "You're welcome! 😊 Happy to help!",
        "Anytime! That's what I'm here for. 🤖",
        "Glad I could help! 🌟",
    ],
}

# Fallback responses when no keyword matches
FALLBACK_RESPONSES = [
    "Hmm, I'm not sure I understand. Could you rephrase that? 🤔",
    "I'm still learning! Try asking me something else. 🌱",
    "Interesting! But that's a bit beyond my current knowledge. 😅",
    "I didn't quite catch that. Try: 'tell me a joke', 'what time is it', or 'help'. 💡",
]


# ── Core matching logic ─────────────────────────────────────────────────────────

def get_response(user_input: str) -> str:
    """Match user input to a response using keyword matching."""
    text = user_input.lower().strip().rstrip("!?.")

    for keywords, replies in RESPONSES.items():
        for keyword in keywords:
            if keyword in text:
                return random.choice(replies)

    return random.choice(FALLBACK_RESPONSES)


# ── Main loop ──────────────────────────────────────────────────────────────────

def main():
    print("\n" + "=" * 50)
    print("   🤖 CHATBOT — Rule-Based Chatbot")
    print("=" * 50)
    print("  Type 'help' to see what I can do.")
    print("  Type 'bye' or 'quit' to exit.")
    print("=" * 50 + "\n")

    while True:
        try:
            user_input = input("  You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\n  ChatBot: Goodbye! 👋\n")
            break

        if not user_input:
            print("  ChatBot: Say something! I'm listening. 👂\n")
            continue

        response = get_response(user_input)
        print(f"  ChatBot: {response}\n")

        # Exit if farewell detected
        farewell_words = ("bye", "goodbye", "quit", "exit", "see you",
                          "see ya", "cya", "later", "farewell")
        if any(word in user_input.lower() for word in farewell_words):
            break

    print("=" * 50 + "\n")


if __name__ == "__main__":
    main()
