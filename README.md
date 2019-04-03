# Assistive-Chatbot
An Assistive Chatbot for Shopping website

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
What things you need to install the software and how to install them

if you are in virtual environment
```
python -m pip -r install requirements.txt
```

if not in virtual environment
```
pip -r install requirements.txt
```

## Insights
* [actions.py] -> this file contains the actions that will be performed by chatbot
* [config_spacy.json] -> this file specifies spacy model of sklearn (spacy has english(en) model)
* [credentials.yml] -> this file is used to enable the API's
* [endpoints.yml] -> this file contains the webhook url
* [nlu_model.py] -> this python file is used to build the initial model with data.json file which is located in data folder
* [domain.yml] -> this file contains intents, entities that chatbot will remember and actions that will be performed by chatbot

We can write our own stories to train our chatbot by running interactive_training.py file
* [ineractive_training.py] -> this file helps to generate stories for chatbot
* [dialogue_management.py] -> this file will train our chatbot on generated stories and provide a interface to check the performance

## Running
1. First we need to start our API server in shopping-website repository
2. then we have to start actions server of chatbot, following is the way to do it
```
python -m rasa_core_sdk.endpoint --actions actions
```
3. then we have to enable API's through which chatbot will send it's answers, following is the way to do it
```
python -m rasa_core.run --enable_api -d models/dialogue -u models/nlu/default/shoppingnlu --port 5002 --credentials credentilas.yml --endpoints endpoints.yml
```
4. start postman app and check the response with the webhook url i.e., ``` http://localhost:5002/webhooks/rest/webhook ```
and set the body as
```
{
	"sender": "Rasa",
	"message": "show me some cloths"
}
```
and header as
```
Content-Type:application/json
```
