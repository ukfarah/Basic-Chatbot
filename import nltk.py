import nltk
from nltk.chat.util import Chat, reflections

# Pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey!"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by Farah.",]
    ],
    [
        r"how are you?",
        ["I'm just a bunch of code, but thanks for asking!",]
    ],
    [
        r"sorry (.*)",
        ["It's okay, no worries.",]
    ],
    [
        r"quit",
        ["Goodbye!", "It was nice talking to you. Goodbye!"]
    ],
    [
        r"(.*) weather (.*)",
        ["I can't check the weather, but you can ask a weather service!"]
    ],
    [
        r"(.*) (location|city) ?",
        ["I am just a virtual entity, so I don't have a physical location."]
    ],
    [
        r"(.*) created you?",
        ["I was created by Farah.",]
    ],
    [
        r"(.*) (help|support) (.*)",
        ["I can help with basic information. What do you need assistance with?"]
    ],
]

# Create Chatbot
def basic_chatbot():
    print("Hi! I am a chatbot created by Farah. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    basic_chatbot()
