from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from polls.models import Question,Choice
# index page
def index(request):
    template = 'polls/index.html'
    return render(request,template)


def about(request):
    template = 'polls/about.html'
    return render(request,template)
#detail page
# def detail(request,question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     template = 'polls/detail.html'
#     context  = {'question':question}
#     return render(request,template,context)
#
# #results page
# def results(request,question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     template = 'polls/detail.html'
#     context  = {'question':question}
#     return render(request,template,context)
#
# #vote page
# from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse
# def vote(request,question_id):
#     p = get_object_or_404(Question,pk=question_id)
#     template = 'polls/detail.html'
#     context  = {'question':p,
#                 'error_message':"Your didnt select a choice"}
#     try:
#         selected_choice = p.choice_set.get(pk=request.POST['choice'])
#     except(KeyError,Choice.DoesNotExist):
#         return render(request,template,context)
#
#     else:
#         selected_choice.votes +=1
#         selected_choice.save();
#     return HttpResponseRedirect(reverse('polls:results',args=(p.id,)))