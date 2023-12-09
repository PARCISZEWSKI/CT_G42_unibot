"""
Main program file for the unibot project
Main dev: Anton Arciszewski
"""
#Variable initialization
topic: str = ""
counter_fail: int = 0
output: str = "What can I help you with? "

#Example Dataset
study_data = {
        "I asses that you are stuggling, is that correct?" :
                {
                        "yes" : { "Maybe sharing your problem with others could help you. Do you agree?" : 
                                        {
                                        "yes": "",
                                        "no" : "I suggest you take an appointment with your student advisor."
                                        }

                                },
                        "no" : "In that case you can visit the schools study page at this link: xxxxxxxxxxx"
                }
}
#Example topic detection sequence
topic_associations: dict[str, set[str]] = {
        "study": {"learn", "math", "science", "struggle"},
        "sport": {"endurance", "boxing", "running", "soccer", "football"},
        "social": {"community", "event", "christmas", "toghether"},
}

def topic_detector(user_input: str) -> str:
        """
        Select the topic that the largest quantity of words match to, returns it
        """
        input_refined: list[str] = (user_input.lower()).split()
        topic_counter: dict[str, int] = {
                "study": 0,
                "sport": 0,
                "social": 0,
        }

        for word in input_refined:
                if word in topic_associations["study"]:
                        topic_counter["study"] += 1
                if word in topic_associations["sport"]:
                        topic_counter["sport"] += 1
                if word in topic_associations["social"]:
                        topic_counter["social"] += 1
        #Sorts the dictionary keys as tuples by their values
        rank : [list[tuple[str, int]]] = sorted(topic_counter.items(), key=lambda counter: counter[1], reverse=True) 
        #print(rank, rank[0][1]) #Console info to check if it is working as expected
        if rank[0][1] != rank[1][1]:
                return rank[0][0] 
        return ""


def tree_parser(data:dict) -> None:
        """
        Jump through key -> answer 
        and recursivly sends next key to parse through
        """
        tree: dict = data
        for key in tree:
            print(key)
            user_choice = input(print("Please type yes or no ")).lower()
            if user_choice in tree[key]:
                if user_choice == "yes" and type(tree[key]["yes"]) == dict:
                    tree_parser(tree[key]["yes"])
                if user_choice == "no" and type(tree[key]["no"]) == dict:
                    tree_parser(tree[key]["no"])
                else:
                    print(tree[key][user_choice])
                    break

                
#Start of the main loop
while (counter_fail < 3):
        """
        Check if the detector function found a topic, 
        gives up to three chances otherwise the loop breaks 
        and we move into the manual user selection
        """
        topic = topic_detector(input(output))
        if topic:
                tree_parser(study_data)
                output = "Thank you for your chat"
                break
        else:
                counter_fail += 1
                output = "Please reword your message "

#In case the detector fails three times, needs to be reworked or rethinked
if counter_fail > 2:
        output = "Please select: sport, study, or social "
        give_up_input = input(output).lower

if output == "sport":
        tree_parser(study_data)
        output = "Thank you for your chat"
elif output == "study": 
        tree_parser(study_data)
        output = "Thank you for your chat"
elif output == "social": 
        tree_parser(study_data)
        output = "Thank you for your chat"
else:
        output = "Critical failure, rerun the unibot"

print(output)