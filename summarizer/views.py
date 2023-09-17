from django.shortcuts import render
from .functions import helper

def home_func(request):
    text, summary, minlen, maxlen, language = '', '', 50, 200, 'english'
    options = [{'name':'English', 'value':'english'}, {'name':'Marathi', 'value':'marathi'}, {'name':'Hindi', 'value':'hindi'}]

    if request.method=='POST':
        text, summary, minlen, maxlen, language = helper.handle_home_func_post_request(request)
        
    context = {'text':text, 'summary':summary, 'minlen':minlen, 'maxlen':maxlen, 'options':options, 'language':language}
    return render(request, 'summarizer/home.html', context=context)
