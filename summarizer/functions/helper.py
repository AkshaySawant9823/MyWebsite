import traceback
import requests
from .translation import translate, manage_long_text
from .summarization import summarize


def handle_home_func_post_request(request):
    try:
        text = request.POST.get('text')
        minlen = int(request.POST.get('min_length'))
        maxlen = int(request.POST.get('max_length'))
        language = request.POST.get('language')
        if minlen>=maxlen:
            minlen=maxlen-1
        result = summarize(text=text, min_length=minlen, max_length=maxlen)
        if result != None:
            summary = result[0].get('summary_text')
        else:
            summary = 'There is issue with server side internet. Stay tuned.'
            language = 'english'
        if language!='english':
            if len(summary)>999:
                summary = manage_long_text(long_text=summary, target=language)
            else:
                summary = translate(text=summary, target=language)
                
    except requests.exceptions.HTTPError as err:
        if err.response.status_code == 429:
            summary = 'Server is busy. You can try later or continue with summarization in english only.'
        else:
            traceback.print_exc()
            summary = "Sorry for inconvenience, we'll be back shortly."
    return text, summary, minlen, maxlen, language