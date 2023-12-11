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

# Structure:
# { "Question/Prompt" : { "answer1" : {...}, "answer2": {...}}
# {...} is the recurvice structure
# answer always in lowercase
# "Prompt" : { } is a leaf

study_questions = {
"For students like you, sometimes there are specific areas that can be challenging. Is there anything in your studies you are struggling with?" :
{
    "yes" : {"Would you like to share your struggles with other students who might be facing similar challenges?":
                    {
                    "yes": {"That's great! Perhaps forming a study group could be beneficial. It's a wonderful way to collaborate and tackle these challenges together.": {}},
                    "no" : {"That's completely understandable. Perhaps seeking guidance from the student advisor could be helpful. They are here to support you with your academic challenges.": {}}
                    }

            },
    "no" : {"If you are looking for practical information or you have other questions? The Student Desk's contact form is a useful resource for specific inquiries, beyond academic challenges.": {}}
}
}# study_question

sport_questions = {}
social_questions = {}
