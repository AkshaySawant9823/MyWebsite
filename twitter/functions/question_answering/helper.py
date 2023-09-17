# ---------------------------------USING THREADING----------------------------------

import requests
import threading
import re
import time
import traceback
from .scrape_google import search
import wikipedia

API_URL = "https://api-inference.huggingface.co/models/distilbert-base-cased-distilled-squad"
headers = {"Authorization": "Bearer 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"}
NUM_RESULTS = 5
SCORE_THRESH = 0

def get_answer(question, context, responses):
    # model used is "distilbert-base-cased-distilled-squad"
    payload = {'inputs': {
    'question': question,
    'context' : context
    }
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    output = response.json()
    score, answer = output.get('score'), output.get('answer')
    if score != None:
        score = round(score, 4)
    responses.append([score, answer])

def get_context(question, num_results=NUM_RESULTS):
    try:
        contexts = []
        data = search(question, advanced=True, num_results=num_results)
        for i in data:
            if 'wikipedia' in i.url:
                title = i.url.split('/')[-1].replace('_',' ').replace('%',"'")
                context = wikipedia.summary(title, auto_suggest=False)
                if context:
                    contexts.append(context)
            else:
                desc = re.sub(r'\([^)]*\)', '', i.description).replace(')','')
                contexts.append(desc)
        return contexts
    except:
        traceback.print_exc()
    return None

def filter_responses(response):
    score, answer = response
    if score == None:
        return False
    if score <= SCORE_THRESH:
        return False
    if re.search('\d{2}-\w{3}-\d{4}', answer):
        return False
    return True

def get_all_answers(question):
    try:
        t1 = time.perf_counter()
        question = question.strip()
        question = question if question.endswith('?') else question + '?'
        contexts = get_context(question)
        responses = []
        threads = []
        for context in contexts:
            t = threading.Thread(target=get_answer, args=(question, context, responses))
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
        responses = list(filter(filter_responses, responses))
        responses = sorted(responses, key=lambda x:x[0], reverse=True)
        time_taken = round(time.perf_counter()-t1, 2)
    except:
        traceback.print_exc()
        responses = [[None, None]]
        time_taken = ''
    return responses, time_taken


if __name__=='__main__':
    question = "Which cricketer won Bharatratna?"
    print(question)
    responses, time_taken = get_all_answers(question)
    print(time_taken)
    print(responses)