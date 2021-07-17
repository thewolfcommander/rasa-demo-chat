import json
import dateutil
from typing import Any, Text, Dict, List

from datetime import datetime
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet



class ValidateReservationForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_reservation_form"

    def validate_time(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate booking time value."""
        time = tracker.get_slot('time')
        now = datetime.now()  # current time
        datetime_obj = dateutil.parser.parse(time[-1]) # parsing the time entered by user
        humanDate = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')  # normalising the time entered by user for comparison
        humanDate = datetime.strptime(humanDate,'%Y-%m-%d %H:%M:%S')  # normalising the time entered by user for comparison
        time_obj = datetime_obj.time()  # getting the time to show to user
        today19pm = now.replace(hour=19, minute=0, second=0, microsecond=0)   # getting the normalised time for 7 PM
        today22pm = now.replace(hour=22, minute=0, second=0, microsecond=0)  # getting the normalised time for 10 PM)
        print(time_obj)
        if (today19pm < humanDate) and (humanDate < today22pm):
            print(humanDate, today19pm, today22pm)
            return {"time": slot_value}
        else:
            return {"time": None}
            

class ActionReservationForm(FormAction):
    def name(self) -> Text:
        return 'reservation_form'

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["name","seatcount","time","category",]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {
            "name": self.from_text(),
            "seatcount": self.from_text(),
            "time": self.from_entity(entity="time", intent= ["inform_time",]),
            "category": self.from_text()
        }

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        time = tracker.get_slot('time')
        datetime_obj = dateutil.parser.parse(time[-1]) # parsing the time entered by user
        time_obj = datetime_obj.time()  # getting the time to show to user
        return [SlotSet(key = "time", value = str(time_obj))]