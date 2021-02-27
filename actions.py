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
        return "action_CustomAction"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        print('latest action:', tracker.latest_action_name)
        print(tracker.latest_message)

        print(entities)
        countries_cities = {
            "Botswana": "Gaborone",
            "India": "Mumbai",

        }
        print('-----------------------------')
        print(tracker.events[-3].get('text'), "Kuda attempting something")
        print('-----------------------------')
        cs = tracker.get_slot('location')
        if cs == 'mumbai':
            dispatcher.utter_message(text="correct")
        else:
            dispatcher.utter_message(text='NOPE!')
            rasa_sdk.events.SlotSet(key="location", value="BOTLOC")
        print(cs, 'hereeeeeeeeeeeeeeeee')

        # for e in entities:
        #  if e['entity'] == 'key':
        #   name = e['value']
        #   print(name)


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


class QuizTime(Action):
    """Pay credit card."""

    def name(self) -> Text:
        """Unique identifier of the action"""
        return "action_Qiuz"

    async def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Executes the action"""

        city_answer = tracker.get_slot("city")
        if city_answer == "Gaborone":
            dispatcher.utter_message(text="Good!")  # template defined in the domain file
        else:
            dispatcher.utter_message(text="Oh, No!")  # template defined in the domain file
        return []
