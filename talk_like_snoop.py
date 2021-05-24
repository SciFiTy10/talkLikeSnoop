#imports
from messages import welcome, reprompt
from custom_intents import talk_like_snoop_intent

##############################
# Program Entry
##############################

#lambda_handler (this is like main())
def lambda_handler(event, context):
    #event is a python dictionary
    #LaunchRequest is an object that means the user made a request to a skill, but didn't specify the intent
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event, context)
    elif event['request']['type'] == "IntentRequest":
        return intent_router(event, context)

##############################
# On Launch
##############################

#on_launch
def on_launch(event, context):

    #passing false on_launch
    shouldEndSession = False
    return statement("Welcome to the Talk Like Snoop Skill!", welcome(), shouldEndSession)

##############################
# Responses
##############################

#statement is a helper function that builds a response
#it takes a title and body to build the spoken response and card output
def statement(title, body, shouldEndSession):
    #speechlet is a dictionary that will be turned into a JSON object
    speechlet = {}
    #build_PlainSpeech builds the OutputSpeech object
    speechlet['outputSpeech'] = build_PlainSpeech(body)
    #builds a Card object
    speechlet['card'] = build_SimpleCard(title, body)
    #I think before here I need to build a reprompt
    speechlet['reprompt'] = build_Reprompt(reprompt())
    #set to False
    speechlet['shouldEndSession'] = shouldEndSession
    #builds the Response body
    return build_response(speechlet)


##############################
# Builders
##############################

#this builds the outputSpeech object
def build_PlainSpeech(body):
    speech = {}
    speech['type'] = 'PlainText'
    speech['text'] = body
    return speech

def build_Reprompt(body):
    reprompt = {}
    reprompt['outputSpeech'] = build_PlainSpeech(body)
    return reprompt

def build_SimpleCard(title, body):
    card = {}
    card['type'] = 'Simple'
    card['title'] = title
    card['content'] = body
    return card

#this is called at the end of the statement function
def build_response(message, session_attributes={}):
    response = {}
    response['version'] = '1.0'
    response['sessionAttributes'] = session_attributes
    response['response'] = message
    return response

##############################
# Routing
##############################

#if a specific intent is selected, this is where that logic is routed
def intent_router(event, context):
    intent = event['request']['intent']['name']

    # Custom Intents
    if intent == "talkLikeSnoop":
        return talk_like_snoop_intent(event, context)

    # Required Intents
    if intent == "AMAZON.CancelIntent" or intent == "AMAZON.StopIntent":
        #set shouldEndSession to true
        shouldEndSession = True
        return statement("Thanks for hanging nephew, uncle snoop will catch you on the flip side!", "Thanks for hanging nephew, uncle snoop will catch you on the flip side!", shouldEndSession)
    if intent == "AMAZON.HelpIntent" or intent == "AMAZON.NavigateHomeIntent":
        #set shouldEndSession to False
        shouldEndSession = False
        return statement("Make sure you use the word \"Say.\" or \"Translate.\" before your phrase to have snoop translizzle what you say", "Make sure you use the word \"Say.\" or \"Translate.\" before your phrase to have snoop translizzle what you say", shouldEndSession)