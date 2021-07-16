import json

from pathlib import Path
from typing import Any, Text, Dict, List, Union


from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase
from rasa_sdk.forms import FormAction
from rasa_sdk.events import EventType, AllSlotsReset
from rasa_sdk.types import DomainDict

# class ActionCancelBooking(Action):

#      def name(self) -> Text:
#             return "action_cancel_booking"

#      def run(self, dispatcher: CollectingDispatcher,
#              tracker: Tracker,
#              domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#          dispatcher.utter_message("We've cancelled your booking")

#          return [AllSlotsReset()]



# class FormDataCollect(FormAction):
#     """
#     This form will collect the data from user about his/her booking
#     """
#     def name(self) -> Text:
#         return "form_info"

#     @staticmethod
#     def required_slots(tracker: "Tracker") -> List[Text]:
#         print("This is working - 1")
#         return ["name", "seatcount", "bookingtime", "category",]

#     def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict[Text, Any]]]]:
#         print("This is working - 2")
#         return {
#             "name": [self.from_text()],
#             "seatcount": [self.from_text()],
#             "bookingtime": [self.from_text()],
#             "category": [self.from_text()],
#             # "confirm_booking": [self.from_text()],
#             # "seatbooked": [self.from_text()]
#         }

#     def submit(
#         self,
#         dispatcher: "CollectingDispatcher",
#         tracker: "Tracker",
#         domain: Dict[Text, Any],
#     ) -> List[EventType]:

#         print("This is working - 3")
#         dispatcher.utter_message("Here are the information that you've entered. Do you want to book? \n\t Name: {0} \n\t Number of seats: {1} \n\t Booking Time: {2} \n\t AC/Non-AC: {3} \n\t ".format(
#             tracker.get_slot("name"),
#             tracker.get_slot("seatcount"),
#             tracker.get_slot("bookingtime"),
#             tracker.get_slot("category"),
#         ))
#         return []
