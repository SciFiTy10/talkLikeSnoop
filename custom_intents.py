from utility_methods import convert_to_snoop
from messages import reprompt

def talk_like_snoop_intent(event, context):
    #get the user's input
    words = event['request']['intent']['slots']['customerQuery']['value']

    #get all of the individual words from the user's input
    words = words.split(" ")

    #set a variable to catch convertedString after passing words through convertToSnoop
    convertedString = convert_to_snoop(words)
    
    #loop application until user quits
    shouldEndSession = False
    
    #print response to the user
    return statement("Snoop says", convertedString + "\n\n " + reprompt(), shouldEndSession)