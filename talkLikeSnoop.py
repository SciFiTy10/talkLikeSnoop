#imports
from random import randint

#set of stop words that will be applied
stop_words = ['i', 'I', 'me', 'much', 'my', 'many', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself','yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that','these','those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of','at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below','to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then','once', 'here','there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such','no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will','just', 'don', 'should','now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma','mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn']

vowels = ["a", "e", "i", "o", "u", "y"]

#loop to go through a string
def locateVowelsInWord(word):
    #start a counter for vowels in a word
    vowelCount = 0

    #create a variable for the location of the vowel we will edit on
    indexOfVowel = 0

    #loop through each word from the end to the beginning
    for e in range(len(word) - 1, -1, -1):
        #if it has a vowel, increment the vowelCount
        if word[e] in vowels:
            #increment the vowelCount
            vowelCount += 1

            #if the count is 1, then we insert izzle on the vowel and cut out everything after
            if vowelCount == 1:
                #set the indexOfVowel to the place where the single vowel is
                indexOfVowel = e
            #if the count is 2, then we insert the izzle on the 2nd to last vowel and cut everything after
            elif vowelCount == 2:
                #set the indexOfVowel to the place where the single vowel is
                indexOfVowel = e
    #pass the word and it's indexOfVowel to the insertIzzle function
    newString = insertIzzle(word, indexOfVowel)
    #return the string to the previous function
    return newString


#function for editing the word for izzle
def insertIzzle(word, indexOfVowel):
    #get the letters at the second to last and the last index
    lastIndex = len(word)-1
    secondToLastIndex = len(word)-2
    thirdToLastIndex = len(word)-3
    #if those combined are "ed" then we want to put "izzled"
    if word[secondToLastIndex] + word[lastIndex] == "ed":
        newString = word[0:indexOfVowel] + "izzled"
    #if the word is sure, make it shizzle
    elif word == "sure":
        newString = word[0:indexOfVowel] + "hizzle"
    #if the word ends with 's' then make it izzles
    elif word[lastIndex] == "s":
        newString = word[0:indexOfVowel] + "izzles"

    #if the word ends with 'ing' then make it izzling
    elif word[thirdToLastIndex] + word[secondToLastIndex] + word[lastIndex] == "ing":
        newString = word[0:indexOfVowel] + "izzling"

    else:
        newString = word[0:indexOfVowel] + "izzle"

    # if word[len(word)] == "d":
    #     print("this word ends with d")
    #create a variable for the newString
    #newString = word[0:indexOfVowel] + "izzle"
    #return newString to the previous function
    return newString


def convertToSnoop(words):
    #create a variable to hold the new sentence
    convertedString = ""

    # #loop through words and get each individual word
    for i in range(len(words)):
        #get the word from the words list
        word = words[i]



        #check to see if the word is a stop word
        if word in stop_words:
            #append to the convertedString
            convertedString = convertedString + " " + word

        #check to see if the first letter is a vowel
        elif word[0] in vowels:
            #append to the convertedString
            convertedString = convertedString + " " + word

        #else the word begins with a consonant
        else:
            #pass a word to the wordVowels function
            newString = locateVowelsInWord(word)

            #append to the convertedString
            convertedString = convertedString + " " + newString

    #return this string to the talkLikeSnoop_intent
    return convertedString


##############################
# Welcome Messages
##############################

#random welcome
def welcomeToTalkLikeSnoop():
    #create an array of welcome messages
    welcomeMessages = ["What up nephew? It's the dogfather himself big Snoop Dogg. Start your response with either \"Say\" or \"Translate\" followed by a few words and I'll translizzle them for you", \
    "You already know its the S., N., double O. P., D O double G big snoop dogg! Respond with either \"Say\" or \"Translate\" followed by a phrase and I'll show you how to talk like Snoop", \
    "What up cuzz, it's uncle snoop dizzle. Use the word \"Say\" or \"Translate\" followed by a phrase and I'll translizzle it for you"]
    #get the length of the array
    arrayLength = len(welcomeMessages)
    #create a randomIndex number for our array of welcome messages
    randomIndex = randint(0, arrayLength - 1)
    #choose the welcome message at random
    welcome = welcomeMessages[randomIndex]

    #return this value to the welcome body
    return welcome

#function for reprompt phrases
def repromptTalkLikeSnoop():
    #create an array of welcome messages
    repromptMessages = ["Speak the word \"Say\" or \"Translate\" followed by your phrase and I'll drop a translizzle like it's hizzle", \
    "Word to Pharrell, if you respond with \"Say\" or \"Translate\" before you say your phrase, I'll tell you how Big Snoop would say it"]
    #get the length of the array
    arrayLength = len(repromptMessages)
    #create a randomIndex number for our array of welcome messages
    randomIndex = randint(0, arrayLength - 1)
    #choose the welcome message at random
    reprompt = repromptMessages[randomIndex]

    #return this value to the welcome body
    return reprompt


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
#should make a call to a customer welcome title and speech in the second parameter
def on_launch(event, context):

    #change this title to reflect the skill
    #call another function to work with the welcome portion of the skill
    #for the 2nd parameter

    #passing false on_launch
    shouldEndSession = False
    return statement("Welcome to the TalkLikeSnoop Skill!", welcomeToTalkLikeSnoop(), shouldEndSession)

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
    speechlet['reprompt'] = build_Reprompt(repromptTalkLikeSnoop())
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

#will need to create an array for possible stuff to say
#may need to erase body as a caught parameter
#may need to handle multiple different calls depending on whether this follows open or intent
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
    # if intent == "AMAZON.StopIntent":
    #     return stop_intent()


##############################
# Custom Intents
##############################

def talkLikeSnoop_intent(event, context):
    #here is where we get the user's input
    #words = event['request']['intent']['name']['slots']['customerQuery']['value']
    words = event['request']['intent']['slots']['customerQuery']['value']
    print(words)
    #get all of the individual words from the example_text
    words = words.split(" ")

    #set a variable to catch convertedString after passing words through convertToSnoop
    convertedString = convertToSnoop(words)

    #make sure this loops
    shouldEndSession = False

    #print this to the user
    return statement("Snoop says", convertedString + "\n\n " + repromptTalkLikeSnoop(), shouldEndSession)
