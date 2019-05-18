from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Question, Choice

# Create your views here.

def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_questions])
    # return HttpResponse(output)
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_questions': latest_questions
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(id=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")

    question = get_object_or_404(Question, id=question_id)
    choices = question.choice_set.all()
    context = {
        'question': question,
        'choices': choices
    }
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choice_set.all()
    context = {
        'question': question,
        'choices': choices
    }
    return render(request, 'polls/results.html', context)

def vote(request, question_id):
    # return HttpResponse("You are voting on the question %s" %question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        print("request.POST['choice'] == " + request.POST['choice'])
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {
            'question': question,
            'error_message': "You did not select a choice."
        }
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

