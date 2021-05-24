#imports
from stop_words import stop_words   
from messages import welcome, reprompt
from insert_methods import forward_insert, backward_insert   


def convertToSnoop(words):

    #loop through words and get each individual word
    for i in range(len(words)):
        #get the word from the words list
        word = words[i]

        #check to see if the word is a stop word
        if word in stop_words:
            #skip to the next word
            continue

        #check to see if the first letter is a vowel
        if word[0] in vowels:
            #skip to the next word
            continue
        #check if word is "sure"
        if word == 'sure':
            word = 'shizzle'
            continue
        #else the word begins with a consonant
        else:
            #get the length of the word
            lengthOfWord = len(word)

            #check if the length is < 7 letters
            if lengthOfWord < 7:
                #add izz into the word
                word = forward_insert(word)
                #insert that word back into it's proper place
                words[i] = word
                #skip to the next word
                continue
            #otherwise the word is 7 or more letters
            else:
                #add izz into the word
                word = backward_insert(word)
                #insert that word back into it's proper place
                words[i] = word
                #skip to the next word
                continue
    #return the words split by a string
    return " ".join(words)           


##############################
# Program Entry
##############################

#lambda_handler - this is like main()
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
    return statement("Welcome to the TalkLikeSnoop Skill!", welcome(), shouldEndSession)

##############################
# Responses
##############################

#statement is a helper function that builds a response
#it takes a title and body to build the spoken and card output
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
        return talkLikeSnoop_intent(event, context)


##############################
# Required Intents
##############################
    # Required Intents
    if intent == "AMAZON.CancelIntent" or intent == "AMAZON.StopIntent":
        #set shouldEndSession to true
        shouldEndSession = True
        return statement("Thanks for hanging nephew, uncle snoop will catch you on the flip side!", "Thanks for hanging nephew, uncle snoop will catch you on the flip side!", shouldEndSession)
    if intent == "AMAZON.HelpIntent" or intent == "AMAZON.NavigateHomeIntent":
        #set shouldEndSession to False
        shouldEndSession = False
        return statement("Make sure you use the word \"Say.\" or \"Translate.\" before your phrase to have snoop translizzle what you say", "Make sure you use the word \"Say.\" or \"Translate.\" before your phrase to have snoop translizzle what you say", shouldEndSession)


##############################
# Custom Intents
##############################

def talkLikeSnoop_intent(event, context):
    #get the user's input
    words = event['request']['intent']['slots']['customerQuery']['value']

    #get all of the individual words from the user's input
    words = words.split(" ")

    #set a variable to catch convertedString after passing words through convertToSnoop
    convertedString = convertToSnoop(words)
    
    #loop application until user quits
    shouldEndSession = False
    
    #print response to the user
    return statement("Snoop says", convertedString + "\n\n " + reprompt(), shouldEndSession)