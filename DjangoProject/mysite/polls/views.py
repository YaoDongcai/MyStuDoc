from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from polls.models import Question,Choice
# 首页 page
def index(request):
    template = 'polls/index.html'
    return render(request,template)

# 关于我们 page关于cj 和 办公
def about(request):
    template = 'polls/about.html'
    return render(request,template)

#   联系我们 page ------》
def contact(request):
    template = 'polls/contact.html'
    return render(request,template)

#   需求订单------>学员；教员
def order(request):
    template='polls/order.html'
    return render(request,template)

def getOrder(request,strKey):
    pass
#     和数据库做post提交后的数据
#     将数据写进数据库中






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