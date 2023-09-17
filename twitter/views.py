from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import StudentInfo
from .functions.question_answering import helper

# Create your views here.
def home_func(request):
    question = responses = time_taken = ''
    if request.method=='POST':
        question = request.POST.get('question')
        print('\nQUESTION:', question, end='\n\n')
        if len(question.strip()) > 5:
            responses, time_taken = helper.get_all_answers(question)
    post_data = StudentInfo.objects.all()
    context={'posts': post_data, 'question':question, 'responses':responses, 'time_taken':time_taken}
    return render(request, 'twitter/home.html', context=context)

def notification_func(request):
    return render(request, 'twitter/notification.html')

def profile_func(request):
    question = ''
    if request.method=='POST':
        print('came in post')
        question = request.POST.get('question')
        print(question)
    post_data = StudentInfo.objects.filter(userid='Die_Epping')
    tweets = len(post_data)
    return render(request, 'twitter/profile.html', context={'posts': post_data, 'question':question, 'tweets':tweets})

def language_func(request):
    return render(request, 'twitter/language.html')

if __name__=='__main__':
    pass