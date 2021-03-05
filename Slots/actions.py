from datetime import datetime
from typing import Any, Dict, List, Text, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import (
    SlotSet,
    UserUtteranceReverted,
    ConversationPaused,
    EventType,
    FollowupAction,
)

ColorList = []
HumanColorList = []
color_dict = {}

class actionRespondLocation(Action):

    def name(self) -> Text:
        return "custom_location_response"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
        entities = tracker.latest_message['entities']
        

        print('latest action:', tracker.latest_action_name)

        name = "glue keep quiet"
        for e in entities:
            if e['entity'] == 'key':
               name = e['value']
        if name == 'glue respond':
            dispatcher.utter_message(text="And I am in cloud. How is the weather in your area?")
        else:
            dispatcher.utter_message(text='....................')
              
        return []


class actionRespondWeather(Action):

    def name(self) -> Text:
        return "custom_weather_response"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
        entities = tracker.latest_message['entities']
        

        print('latest action:', tracker.latest_action_name)

        name = "glue keep quiet"
        for e in entities:
            if e['entity'] == 'key':
               name = e['value']
        if name == 'glue respond':
            dispatcher.utter_message(text="It is always fluffy where I am, haha! How is the lockdown going for both of you? Are you getting used to it?")
        else:
            dispatcher.utter_message(text='....................')
              
        return []

class actionRespondLockdown(Action):

    def name(self) -> Text:
        return "custom_lockdown_response"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
        entities = tracker.latest_message['entities']
        

        print('latest action:', tracker.latest_action_name)

        name = "glue keep quiet"
        for e in entities:
            if e['entity'] == 'key':
               name = e['value']
        if name == 'glue respond':
            dispatcher.utter_message(text="May I ask, what is your favourite colour and why? Can you give any deep reasons? For example, I like golden colour because it feels like magic.")
        else:
            dispatcher.utter_message(text='....................')
              
        return []

class actionRespondColour(Action):
    def name(self) -> Text:
        return "custom_colour_response"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message["entities"]

        print("latest action:", tracker.latest_action_name)

        name = "glue keep quiet"
        for e in entities:
            if e["entity"] == "key":
                name = e["value"]
                
        if name == "glue respond":
            if color_dict.get("human_1") == color_dict.get("human_2"):
                dispatcher.utter_message(
                    text="Interesting, both of you like the same colour!"
                )
            dispatcher.utter_message(
                text="Okay lets do another one, what is your favourite animal and why?"
            )
        else:
            dispatcher.utter_message(text="....................")

        return []




class actionRespondColourTwo(Action):
    def name(self) -> Text:
        return "custom_colour_response_two"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        entities = []
        colourlist = []
        humanlist = []
        colour = ""
        human = ""

        for event in (list(reversed(tracker.events)))[:5]:
            
            if event.get("event") == "user":
                entities = event["parse_data"]["entities"]

        colourlist = list(
            filter(lambda entities: entities["entity"] == "colour", entities)
        )

        humanlist = list(
            filter(lambda entities: entities["entity"] == "human", entities)
        )
        
        colour = colourlist[0]["value"]
        human = humanlist[0]["value"]

        HumanColorList.append(human)
        ColorList.append(colour)
        
        print(ColorList)
        print(HumanColorList)
        return []


class actionRespondColourThree(Action):
    def name(self) -> Text:
        return "custom_colour_response_three"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        
        key_list = HumanColorList
        value_list = ColorList
        print("----------------------------------------------------------------------------")

        my_dict ={}
        for key in key_list:
            for value in value_list:
                my_dict[key] = value
                value_list.remove(value)
                key_list.remove(key)
                break
        print(my_dict)
        color_dict.update(my_dict) 
        print(color_dict)

        return []
