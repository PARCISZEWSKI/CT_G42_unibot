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
                "sport", "sports",
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
                "together",
                "person", "people",
                "friend", "friends",
                "association", "associations",
                "art", "arts",
                "paint", "painting", "paintings",
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
    "no" : {"That's completely understandable. Perhaps seeking guidance from the student advisor could be helpful. They are here to support you with your academic challenges: https://vu.nl/nl/student/contact-en-studentbegeleiding/studieadviseur": {}}
    }

        },
"no" : {"If you are looking for practical information or you have other questions. The Student Desk's contact form is a useful resource for specific inquiries, beyond academic challenges: https://vu.nl/en/education/more-about/student-desk-vrije-universiteit-amsterdam#": {}}
}
}# study_question

sport_questions = {
 "Are you interested in a specific sport already, or are you looking to explore and try something new?" :
 {
     "specific" : {"What specific sport are you interested in?":
                     {
                     "aikido": {"That's great, this sport is available at the University! Take a look at the university sport center page for more information: https://sportcentrumvu.nl/": {}},
                     "basketball" : {"That's great, this sport is available at the University! Take a look at the university sport center page for more information: https://sportcentrumvu.nl/": {}},
 	        "tennis": {"That's great, this sport is available at the University! Take a look at the university sport center page for more information: https://sportcentrumvu.nl/": {}},
                     "swimming" : {"That's great, this sport is available at the University! Take a look at the university sport center page for more information: https://sportcentrumvu.nl/": {}},
 	          "football": {"That's great, this sport is available at the University! Take a look at the university sport center page for more information: https://sportcentrumvu.nl/": {}},
                     "zumba" : {"That's great, this sport is available at the University! Take a look at the university sport center page for more information: https://sportcentrumvu.nl/": {}},
 	        "karate": {"That's great, this sport is available at the University! Take a look at the university sport center page for more information: https://sportcentrumvu.nl/": {}},
                     "yoga" : {"That's great, this sport is available at the University! Take a look at the university sport center page for more information: https://sportcentrumvu.nl/ ": {}},
 	        "waterpolo" : {"That's great, this sport is available at the University! Take a look at the university sport center page for more information: https://sportcentrumvu.nl/": {}},
 	       "None of the above" : {"Unfortunately, only these sports are currently available at the University.": {}}
                     }
 
             },
     "explore" : {"Exploring a new sport is exciting! To help narrow down the options, could you specify the type of sport you're inclined towards?":
      {
       "team sports with ball" : {
         "Do you prefer indoor or outdoor?": {
            "outdoor" : {
                "Do you prefer a small team of two or a bigger team?":
                {
                "two" : {"That’s great, I recommend you to take a look at tennis!": {}},
                "bigger" : {"That’s great, I recommend you to take a look at football!": {}},
                },
            },
            "indoor": {
                "Do you like water sports?":
                {
                    "yes" : {"That’s great, I recommend you to take a look at waterpolo!": {}},
                    "no" : { "That’s great, I recommend you to take a look at football!": {}}
                }
            }
        }},
       "dance sports" : { "That’s great! I recommend you to take a look at Zumba.": {}},
       "individual ball sports" : {"That’s great! I recommend you to take a look at tennis!":{}},
       "fight sports" : {
           "Do you like to grapple or do you like to strike?":
             {
            "grapple" : {"That’s great, I recommend you to take a look at aikido!": {}},
            "strike": {"That’s great, I recommend you to take a look at karate!":  {}},
             }
        },
       "anaerobic sports" : {"That’s great! I recommend you to take a look at Yoga.": {}},
       "water sports" : {"Do you prefer water sports with a ball or without?":
             {
             "without" : {"That’s great, I recommend you to take a look at swimming!": {}},
             "with" : {"That’s great, I recommend you to take a look at waterpolo!": {}}
             }
        },
 }}
 }
 }# sport question


social_questions = {
"Are you more interested in upcoming events happening around campus or joining a student association to engage in regular social activities?" :
{
    "events" : {
        "I recommend you these 3 options: New Year's Party (13 Jan 2024), Valentine's Dinner (14 Feb 2024), Carnival Night (1 March 2024). ":
        {}
    },

    "association" : {
        "Joining a new student association is exciting! To help narrow down the options, could you specify the type of activity you're inclined towards?":
        {
        "climate related groups": {"That's great! I recommend you to look at this student association: Students for Sustainability": {}},
        "debating" : {"That's great! I recommend you to look at this student association: Debate Club.": {}},
        "travel group" : {"That's great! I recommend you to look at this student association: Bunch of Backpackers.":{}},
        "volunteer opportunities" :{"That's great! I recommend you to look at this student association: Animal Shelter Volunteers":{}},
        "poetry related" :{"That's great! I recommend you to look at this student association: Poetry Pals.":{}},
        "international student group":{"That's great! I recommend you to look at this student association: International Students Society.":{}},
        "learning foreign languages":{"That's great! I recommend you to look at this student association: Language Club.":{}},
        "science related groups":{"That's great! I recommend you to look at this student association: Science Society.":{}},
        "making art":{"That's great! I recommend you to look at this student association: Painting and Pottery.":{}},
        }
    }
}
}#social_questions

