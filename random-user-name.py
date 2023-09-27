import random
import subprocess

# List of words
word_list = [
    "lagoon", "breeze", "serenade", "cascade", "glimmer", "tundra", "quasar",
    "zephyr", "marvel", "wanderlust", "twilight", "delight", "ethereal",
    "lullaby", "velvet", "solitude", "meadow", "ponder", "bliss", "mirage",
    "silhouette", "whimsical", "saffron", "enigma", "reverie", "symphony",
    "pinnacle", "galore", "mystic", "tranquil", "essence", "inquisitive",
    "dazzle", "glisten", "harmony", "sonnet", "rapture", "serenity",
    "illuminate", "ethereal", "jubilee", "zest", "breathless", "enchant",
    "sonnet", "whisper", "kaleidoscope", "solace", "amethyst", "soothe",
    "opulent", "resplendent", "quintessence", "epiphany", "ponder", "vibrant",
    "melody", "lull", "radiance", "echo", "velvet", "mystic", "cascade",
    "captivate", "glimmer", "tranquil", "zephyr", "jubilant", "placid",
    "savor", "serenade", "ineffable", "solitude", "sincere", "whisper",
    "reflect", "enigma", "ethereal", "resonate", "wanderlust", "harmonious",
    "bliss", "symphony", "verdant", "rhapsody", "breathless", "twilight",
    "halcyon", "dazzle", "rapture", "mirage", "delight", "inquisitive",
    "effervescent", "marvel", "serenity", "tundra", "pinnacle", "mellifluous",
    "glisten", "solace", "radiant", "lagoon", "tranquil", "soothe", "sonnet",
    "zephyr", "reflect", "breeze", "enchant", "essence", "ponder", "ethereal",
    "reverie", "symphony", "opulent", "jubilee", "glimmer", "cascade",
    "resplendent", "whisper", "dazzle", "bliss", "marvel", "tranquil", "zephyr",
    "placid", "radiance", "serenity", "jubilant", "melody", "solitude",
    "verdant", "halcyon", "glisten", "enigma", "illuminate", "savor", "sincere",
    "captivate", "breathless", "ineffable", "rhapsody", "wanderlust", "harmony",
    "sonnet", "serenade", "lull", "solace", "resonate", "ponder", "mystic",
    "placid", "reflect", "effervescent", "essence", "enchant", "dazzle",
    "symphony", "radiant", "rapture", "tranquil", "verdant", "whisper",
    "glimmer", "marvel", "opulent", "reverie", "ethereal", "zephyr", "harmony",
    "serenity", "illuminate", "breeze", "lagoon", "dazzle", "solitude",
    "ineffable", "soothe", "essence", "glisten", "resplendent", "melody",
    "reflect", "placid", "whisper", "radiance", "serenade", "savor", "symphony",
    "bliss", "ponder", "verdant", "jubilee", "halcyon", "enchant", "mystic",
    "ethereal", "rapture", "glimmer", "illuminate", "marvel", "tranquil",
    "resonate", "essence", "radiant", "zephyr", "solitude", "whisper", "dazzle",
    "serenity", "lagoon", "symphony", "reverie", "reflect", "inquisitive",
    "verdant", "placid", "harmony", "glisten", "rhapsody", "jubilant", "breeze",
    "savor", "solace", "pinnacle", "glimmer", "enchant", "breathless", "halcyon",
    "mystic", "tranquil", "essence", "dazzle", "serenade", "marvel", "symphony",
    "whisper", "radiance", "bliss", "savor", "illuminate", "ineffable", "reflect",
    "ethereal", "placid", "ponder", "glisten", "resonate", "reverie", "solitude",
    "serenity", "verdant", "halcyon", "jubilant", "rhapsody", "symphony",
    "harmony", "essence", "illuminate", "marvel", "solace", "breathless",
    "glimmer", "dazzle", "tranquil", "radiant"
]

# Pick a random word
selected_word = random.choice(word_list)

# Print the selected word
print(selected_word)
