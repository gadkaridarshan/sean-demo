# -*- coding: utf-8 -*-
import logging
import json
import requests
from datetime import datetime
from typing import Any, Dict, List, Text, Union, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import (
    SlotSet,
    UserUtteranceReverted,
    ConversationPaused,
    EventType,
    FollowupAction,
)

from actions import config
from actions.api import community_events
from actions.api.algolia import AlgoliaAPI
from actions.api.discourse import DiscourseAPI
from actions.api.gdrive_service import GDriveService
from actions.api.mailchimp import MailChimpAPI

logger = logging.getLogger(__name__)

INTENT_DESCRIPTION_MAPPING_PATH = "actions/intent_description_mapping.csv"



class ActionConnectToAdvisor(Action):
    """Returns the specific utterance"""

    def name(self) -> Text:
        return "action_advisor_callback"

    def run(self, dispatcher, tracker, domain) -> List[EventType]:
        logger.debug(tracker.current_slot_values())
        dispatcher.utter_message(template="utter_advisor_callback")

        return [UserUtteranceReverted()]


class ContactForm(FormAction):
    """Collects contact information and adds it to the spreadsheet"""

    def name(self):
        return "contact_form"

    @staticmethod
    def required_slots(tracker):
        return [
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "best_time_to_contact",
            "city",
            "county",
            "country",
            ]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
        ) -> List[Dict]:

        dispatcher.utter_message("Thanks for getting in touch, an advisor contact you soon")
        return []


