from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question
class IndexView(generic.ListView):
    """汎用 Index view
    """
    template_name  = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(set):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DatailView(generic.DetailView):
    """汎用 Detail view
    """
    model = Question
    template_name  = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
        
class ResultsView(generic.DetailView):
    """汎用 Detail view
    """
    model = Question
    template_name  = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice']) #IDを文字列で返す
    # POSTのKeyError検出
    except (KeyError, Choice.DoesNotExist):
        # 投票フォーム再表示
        return render(request, 'polls/detail.html',{
            'question': question,
            'error_message': "You didn't select a choice.",
         })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # POSTデータが成功したら常にHttpResponseRedirect()する必要がある。Web開発の常識らしい
        # reverse()はview関数中のURLハードコードを防げる。
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
