from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404, reverse

from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def redirect_polls(request):
    return redirect('index', permanent=True)

def detail(request, question_text):
    question = get_object_or_404(Question, question_text=question_text)
    return render(request, 'polls/detail.html', context={'question':question})

def results(request, question_text):
    question = get_object_or_404(Question, question_text=question_text)
    return render(request, 'polls/results.html', context={'question':question})

def vote(request, question_text):
    question = get_object_or_404(Question, question_text=question_text)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', context={
        'question':question,
        'error_message':error_message,
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results_url', args=(question.question_text,)))

def votes_amount(request, question_text, choice_text):
    question = Question.objects.get(question_text=question_text)
    votes_amount = question.choice_set.get(choice_text=choice_text).votes
    return render(request, 'polls/votes_amount.html', context={'question':question, 'votes_amount':votes_amount})
