"""
UniBot Topics Data.
"""

# For each topic give a set of extact matched words (lowercase) that represent it.
topic_words: dict[str, set[str]] = {
        "study": {
                "study", "studying", "studied",
                "learn", "learnt", "learned",
                "struggle", "struggling",
                "lesson", "lessons",
                "lecture", "lectures",
                "class", "classes",
                "assignment", "assignments",
                "math", "science"
        },
        "sport": {
                "sport", "spots",
                "play", "playing",
                "workout", "workouts",
                "endurance",
                "boxing",
                "running",
                "soccer",
                "football",
                "aikido",
                "basketball",
                "tennis",
                "swimming",
                "zumba",
                "karate",
                "yoga",
                "waterpolo",
        },
        "social": {
                "social",
                "community", "communities",
                "event", "events",
                "christmas",
                "toghether",
                "person", "people",
                "friend", "friends",
                "association", "associations",
                "art", "arts",
                "paint", "painting", "paitings",
                "music", "musics",
                "listen", "listening",
                "society", "societies",
        },
}
