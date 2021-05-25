from response_methods import statement
from custom_intents import talk_like_snoop_intent
from messages import welcome

#on_launch
def on_launch(event, context):

    #passing false on_launch
    shouldEndSession = False
    return statement("Welcome to the Talk Like Snoop Skill!", welcome(), shouldEndSession)

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