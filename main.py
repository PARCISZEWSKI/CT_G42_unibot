"""
Main program file for the unibot project
Main dev: Anton Arciszewski
"""
from collections import namedtuple


#Example Dataset
# Structure:
# { "Question/Prompt" : { "answer1" : {...}, "answer2": {...}}
# {...} is the recurvice structure
# answer always in lowercase
# "Prompt" : { } is a leaf
study_questions = {
        "I asses that you are stuggling, is that correct?" :
                {
                        "yes" : {"Maybe sharing your problem with others could help you. Do you agree?":
                                        {
                                        "yes": {"TODO": {}},
                                        "no" : {"I suggest you take an appointment with your student advisor.": {}}
                                        }

                                },
                        "no" : {"In that case you can visit the schools study page at this link: xxxxxxxxxxx": {}}
                }
}

sport_questions = {}
social_questions = {}

questions_tree = {
    "study": study_questions,
    "sport": sport_questions,
    "social": social_questions,
} # questions_tree


#Example topic detection sequence
topic_associations: dict[str, set[str]] = {
        "study": {"study", "learn", "math", "science", "struggle", "lesson", "lecture"},
        "sport": {"sport", "endurance", "boxing", "running", "soccer", "football"},
        "social": {"social", "community", "event", "christmas", "toghether"},
}

def prompt(msg: str, choices=[], reply=True) -> str:
        """
        Format the prompt.
        """
        print(f"UNIBOT: {msg}")
        for c in choices:
                print(f"> {c}")
        if len(choices) > 0:
                print(f"UNIBOT: Select one option: ")
        if reply:
                return input("YOU: ")

def topic_detector(user_input: str) -> str:
        """
        Select the topic that the largest quantity of words match to, returns it
        """
        global topic_associations

        topic_counter: dict[str, int] = {topic: 0 for topic in topic_associations}

        input_refined: list[str] = (user_input.lower()).split()
        for word in input_refined:
                for topic in topic_associations:
                        if word in topic_associations[topic]:
                                topic_counter[topic] += 1

        #Sorts the dictionary keys as tuples by their values
        rank : [list[tuple[str, int]]] = sorted(topic_counter.items(), key=lambda counter: counter[1], reverse=True)
        if rank[0][1] != rank[1][1]:
                return rank[0][0]
        return ""


def tree_parser(tree:dict) -> None:
        """
        Jump through key -> answer
        and recursivly sends next key to parse through
        """

        for question in tree: # should be always one
                choices: dict = tree[question]

                # Final answer
                if len(choices) == 0:
                        prompt(question, reply=False)
                        return

                # Ask details
                repeat: bool = True
                while repeat:
                        user_choice = prompt(question, choices)
                        repeat = (user_choice not in choices)

                        if repeat:
                                prompt("I'm sorry, I don't understand your answer", reply=False)

                # while
                tree_parser(choices[user_choice])
# tree_parser

def main() -> None:
        """
        Main loop
        """

        counter_fail: int = 0
        question: str = "What can I help you with? "
        # Check if the detector function found a topic,
        # gives up to three chances otherwise the loop breaks
        # and we move into the manual user selection
        while (counter_fail < 3):
                user_reply: str = prompt(question)
                topic: str = topic_detector(user_reply)
                if topic:
                        tree = questions_tree[topic]
                        tree_parser(tree)
                        question = "Thank you for your chat."
                        break
                else:
                        counter_fail += 1
                        question = "Please reword your message: "

        #In case the detector fails three times, needs to be reworked or rethinked
        if counter_fail > 2:
                give_up_input = prompt("I'm sorry, I don't understand. Choose one topic, please.",
                       questions_tree.keys())

                if give_up_input in questions_tree:
                        tree = questions_tree[give_up_input]
                        tree_parser(tree)
                else:
                        prompt("I'm sorry, I cannot help you.", reply=False)

        prompt("Thank you for your chat.", reply=False)

if __name__ == '__main__':
        main()
