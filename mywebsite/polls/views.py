from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404, reverse
from django.views import generic

from .models import Question, Choice

def redirect_polls(request):
    return redirect('index', permanent=True)


class IndexView(generic.ListView):
    model = Question
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_query_set(self):
        # Returns the last five published questions
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
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
        return HttpResponseRedirect(reverse('polls:results_url', args=(question.id,)))

def votes_amount(request, question_id, choice_text):
    question = Question.objects.get(pk=question_id)
    votes_amount = question.choice_set.get(choice_text=choice_text).votes
    return render(request, 'polls/votes_amount.html', context={'question':question, 'votes_amount':votes_amount})
