# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class actionListen(Action):

    def name(self) -> Text:
        return "CustomAction"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        print('latest action:', tracker.latest_action_name)
        print("----------------------------------------------------")
        print(tracker.latest_message)
        print(entities)
        for e in entities:
            if e['entity'] == 'key':
                name = e['value']
                print(name)

        dispatcher.utter_message(
            text="Wow I would love to visit some day. {0} is one of the amazing places. How is {0}?.".format(name))
        return []


class actionListen(Action):

    def name(self) -> Text:
        return "custom_listen"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        print(tracker.latest_message)
        name = 'Speak'
        for e in entities:
            if e['entity'] == 'key':
                name = e['value']
                print('-------------------------------------------------------------')
                print(name)
        if name != 'Speak':
            dispatcher.utter_message(text="I need to shut up")
        else:
            dispatcher.utter_message(text='I may speak')
        return []


class actionNoResponse(Action):

    def name(self) -> Text:
        return "no_response"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        pass
        return []
