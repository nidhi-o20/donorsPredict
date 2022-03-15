
import urllib.request
import json

data = {
    "Inputs": {
        "input1":
        [
            {
                'Donor ID': "237db43817f34988f9d543ca518be4ee",
            }
        ],
    },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/4f672456bbcc47adba68f83bdc1997cb/services/ffb15db29e4c472b8e3b0f446d367ff0/execute?api-version=2.0&format=swagger'
# Replace this with the API key for the web service
api_key = 'ntfTszi9h9+egR2KrITB1FIH529wlN1hBtdDIQPoA/Lz4RKr70Bud0auiu0sjm5+4y3/jw+brBtG3PSAj59qGQ=='
headers = {'Content-Type': 'application/json',
           'Authorization': ('Bearer ' + api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))
