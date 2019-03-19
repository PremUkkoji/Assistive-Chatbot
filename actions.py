from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class GetProductsOfCategory(Action):
	def name(self):
		return 'action_category_products'
		
	def run(self, dispatcher, tracker, domain):
		category = tracker.get_slot('category')
		response = 	"category_products"					
		dispatcher.utter_message(response)
		return [SlotSet('category',category)]

class GetUserRatingForProduct(Action):
	def name(self):
		return 'action_product_rating'

	def run(self, dispatcher, tracker, domain):
		product = tracker.get_slot('prod1')
		response = "product_rating"
		dispatcher.utter_message(response)
		return [SlotSet('prod1', product)]

class GetProductCompareDetails(Action):
	def name(self):
		return 'action_product_compare'

	def run(self, dispatcher, tracker, domain):
		product1 = tracker.get_slot('prod1')
		product2 = tracker.get_slot('prod2')
		response = "product_compare"
		dispatcher.utter_message(response)
		return [SlotSet('prod1', product1)]

class GetDiscountForProduct(Action):
	def name(self):
		return 'action_product_discount'

	def run(self, dispatcher, tracker, domain):
		product = tracker.get_slot('prod1')
		response = "product_discount"
		dispatcher.utter_message(response)
		return [SlotSet('prod1', product)]

class GetUserCartItems(Action): #trained 2 times
	def name(self):
		return 'action_user_cart'

	def run(self, dispatcher, tracker, domain):
		#user = tracker.get_slot('user')
		response = "user_cart"
		dispatcher.utter_message(response)
		return []

class GetUserPurchasedItems(Action): #trained 2 times
	def name(self):
		return 'action_user_purchased'

	def run(self, dispatcher, tracker, domain):
		#user = tracker.get_slot('user')
		response = "user_purchased"
		dispatcher.utter_message(response)
		return []

class GetUserProfile(Action):
	def name(self):
		return 'action_user_profile'

	def run(self, dispatcher, tracker, domain):
		#user = tracker.get_slot('user')
		response = "user_profile"
		dispatcher.utter_message(response)
		return []

class GetProductDetails(Action):
	def name(self):
		return 'action_product_details'

	def run(self, dispatcher, tracker, domain):
		prod1 = tracker.get_slot('prod1')
		response = "product_details"
		dispatcher.utter_message(response)
		return [SlotSet('prod1', prod1)]

class Actionreset(Action):
	def name(self):
		return 'action_reset'

	def run(self, dispatcher, tracker, domain):
		return [AllSlotsReset()]