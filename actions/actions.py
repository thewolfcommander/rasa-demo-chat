from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

class reservationform(FormAction):

    def name(self) -> Text:
        return "form_info"
    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
         required_slots = ["seatcount", "section", "time"]

         for slot_name in required_slots:
             if tracker.slots.get(slot_name) is None:
                 return [SlotSet("requested_slot", slot_name)]
                 
         return [SlotSet("requested_slot", None)]

class ActionSubmit(Action):
    def name(self)  -> Text:
        return "action_submit"

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict"
        ) -> List[Dict[Text, Any]]:

            dispatcher.utter_message("Thanks, great job!")
            return []