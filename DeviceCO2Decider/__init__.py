import logging
import requests

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    # Get the current actual CO2 intensity of the uk nation grid electricity from this api - https://api.carbonintensity.org.uk/intensity
    # Use that co2 to decide to turn on or off a device
    # if the CO2 is over 150g then turn it off
    # if the CO2 is under 150g then turn it on
    # return the current CO2 intensity and the decision made

    # Get the current CO2 intensity using the requests library
    req = requests.get('https://api.carbonintensity.org.uk/intensity')
    # Convert the response to json
    req_json = req.json()
    # Get the current CO2 intensity
    current_co2_intensity = req_json['data'][0]['intensity']['actual']
    device_decision = 'off'

  
    if current_co2_intensity > 150:
        # Turn off the device
        device_decision = 'off'
    else:
        # Turn on the device
        device_decision = 'on'

    # Return the current CO2 intensity and the decision made
    return func.HttpResponse(f"The current CO2 intensity is {current_co2_intensity} and the decision made is to turn the device {device_decision}")