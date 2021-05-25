#imports
from routing_methods import on_launch, intent_router

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
