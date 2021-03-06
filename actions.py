from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

import requests, json
from pprint import pprint

# these are the actions that chatbot will take according to the use intent

# the following action is taken when the message is out of scope of chatbot
class OutOfScopeMessage(Action):
	def name(self):
		return 'action_default'

	def run(self, dispatcher, tracker, domain):
		dispatcher.utter_message("I'm not sure I understand!!!")
		return []

# the following action will be taken when user requests some category products
class GetProductsOfCategory(Action):
	def name(self):
		return 'action_category_products'
		
	def run(self, dispatcher, tracker, domain):
		pprint("action_category_products")
		category = tracker.get_slot('category')
		pprint(category)
		if category:
			category = category.lower()
			try:
				url = 'http://localhost:8000/categoryProducts/'+category
				headers = {'Content-Type': 'application/json'}
				response = requests.get(url, headers=headers)
				pprint(response.text)
				if response.text == '[]':
					raise Exception
				dispatcher.utter_message(response.text)
			except Exception:
				dispatcher.utter_message("I couldn't find any products")
		else:
			dispatcher.utter_message("I couldn't find any products")
		return [SlotSet('category',category)]

# this action returns product rating
class GetUserRatingForProduct(Action):
	def name(self):
		return 'action_product_rating'

	def run(self, dispatcher, tracker, domain):
		pprint("action_product_rating")
		product = tracker.get_slot('prod1')
		pprint(product)
		if product:
			product = product.lower()
			try:
				url = 'http://localhost:8000/ratingOfProduct/'+product
				
				headers = {'Content-Type': 'application/json'}
				response = requests.get(url, headers=headers)
				data = response.json()
				rating = data[0]['rating']
				dispatcher.utter_message("Rating for this product is "+str(rating))
			except Exception as e:
				dispatcher.utter_message("I couldn't find this product")
		else:
			dispatcher.utter_message("I couldn't find this product")
		return [SlotSet('prod1', product)]

# this action returns details to compare products
class GetProductCompareDetails(Action):
	def name(self):
		return 'action_product_compare'

	def run(self, dispatcher, tracker, domain):
		pprint("action_product_compare")
		product1 = tracker.get_slot('prod1')
		product2 = tracker.get_slot('prod2')
		pprint(product1)
		pprint(product2)
		if product1 and product2:
			product1 = product1.lower()
			product2 = product2.lower()
			try:
				url = 'http://localhost:8000/compareProducts/'+product1+'/'+product2
				headers = {'Content-Type': 'application/json'}
				response = requests.get(url, headers=headers)
				pprint(response.text)
				if response.text == '[]':
						raise Exception
				dispatcher.utter_message(response.text)
			except Exception as e:
				dispatcher.utter_message("couldn't compare")
		else:
			dispatcher.utter_message("couldn't compare")
		return [SlotSet('prod1', product1)]

# this action will return product discount
class GetDiscountForProduct(Action):
	def name(self):
		return 'action_product_discount'

	def run(self, dispatcher, tracker, domain):
		pprint("action_product_discount")
		product = tracker.get_slot('prod1')
		pprint(product)
		if product:
			product = product.lower()
			try:
				url = 'http://localhost:8000/discountOfProduct/'+product
				headers = {'Content-Type': 'application/json'}
				response = requests.get(url, headers=headers)
				data = response.json()
				discount = data[0]['discount']
				dispatcher.utter_message("Discount on this product is "+str(discount))
			except Exception as e:
				dispatcher.utter_message("I could'nt find this product")
		else:
			dispatcher.utter_message("I could'nt find this product")
		return [SlotSet('prod1', product)]

# this will return "cart items" as string and will be handled in chatbot's UI javascript
class GetUserCartItems(Action):
	def name(self):
		return 'action_user_cart'

	def run(self, dispatcher, tracker, domain):
		pprint("action_user_cart")
		#user = tracker.get_slot('user')
		response = "cart items"
		dispatcher.utter_message(response)
		return []

# this will return "purchased items" as string and will be handled in chatbot's UI javascript
class GetUserPurchasedItems(Action):
	def name(self):
		return 'action_user_purchased'

	def run(self, dispatcher, tracker, domain):
		pprint("action_user_purchased")
		#user = tracker.get_slot('user')
		response = "purchased items"
		dispatcher.utter_message(response)
		return []

# this will return "profile" as string and will be handled in chatbot's UI javascript
class GetUserProfile(Action):
	def name(self):
		return 'action_user_profile'

	def run(self, dispatcher, tracker, domain):
		pprint("action_user_profile")
		#user = tracker.get_slot('user')
		response = "profile"
		dispatcher.utter_message(response)
		return []

# this action reutrns a particular product details
class GetProductDetails(Action):
	def name(self):
		return 'action_product_details'

	def run(self, dispatcher, tracker, domain):
		pprint("action_product_details")
		prod1 = tracker.get_slot('prod1')
		pprint(prod1)
		if prod1:
			prod1 = prod1.lower()
			try:
				url = 'http://localhost:8000/productDetails/'+prod1
				headers = {'Content-Type': 'application/json'}
				response = requests.get(url, headers=headers)
				pprint(response.text)
				if response.text == '[]':
					raise Exception
				dispatcher.utter_message(response.text)
			except Exception as e:
				dispatcher.utter_message("could'nt get the details")
		else:
			dispatcher.utter_message("could'nt get the details")
		return [SlotSet('prod1', prod1)]

# this action is used to empty slots
class Actionreset(Action):
	def name(self):
		return 'action_reset'

	def run(self, dispatcher, tracker, domain):
		return [AllSlotsReset()]