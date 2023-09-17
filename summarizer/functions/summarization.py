import json
import requests


headers = {"Authorization": f"Bearer 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"}
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

text = '''The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct.'''

def query(payload):
    data = json.dumps(payload)
    try:
        response = requests.request("POST", API_URL, headers=headers, data=data)
        return json.loads(response.content.decode("utf-8"))
    except:
        return None

def summarize(text=text, min_length=20, max_length=50):
    output = query({
                "inputs": text,
                "parameters": {
                    "do_sample": False,
                    'min_length': min_length,
                    'max_length': max_length},
                    })
    return output
