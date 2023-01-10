# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# Global variables
# Dict for mapping intents to a question
intent_question_dictionary = {
    "linear_regression": "What is linear regression?",
    "logistic_regression": "What is logistic regression?",
    "mean_square_error": "What is mean square error?",
    "mean_absolute_error": "What is mean absolute error?",
}

class ActionML(Action):

    def name(self) -> Text:
        return "action_ml"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text=f"intent: {tracker.get_intent_of_latest_message()}")

        print("*"*20)
        # list for buttons to send to the user
        buttons = []
        for intent_ranking in tracker.latest_message['intent_ranking'][1:]:
            print(f"Intent Name is: {intent_ranking['name']} \nConfidence: {intent_ranking['confidence']*100}")
            if intent_question_dictionary.get(intent_ranking['name']):
                #append the response in the form of title and payload
                buttons.append({
                    "title": intent_question_dictionary.get(intent_ranking['name']),
                    "payload": intent_question_dictionary.get(intent_ranking['name'])
                    })
            # making sure that at max 'N' buttons are added to the list
            if len(buttons) > 4:
                break
        print("*"*20)
        # print(buttons)
        dispatcher.utter_message(text="You may also find these interesting", buttons=buttons)
        return []
