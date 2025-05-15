from django.shortcuts import render
from .models import QuestFeedBack
from django.http import HttpResponseRedirect
from .forms import QuestFeedBackForm
from .models import QuestFeedBack
from django.views import View
from django.views.generic import ListView


# Create your views here.

class QuestFeedBackView(View):
    def get(self, request):
        form = QuestFeedBackForm()
        return render(
            request,
            'wedding_app/first_form.html',
            context={
                'form': form
            }
        )

    def post(self, request):
        form = QuestFeedBackForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/done')
        return render(request,
                      'wedding_app/first_form.html',
                      context={
                          'form': form
                      })


class AuthView(View):
    def get(self, request):
        form = ...

    def post(self, request):
        form = ...


class ListQuests(ListView):
    template_name = 'wedding_app/show_info.html'
    model = QuestFeedBack
    context_object_name = 'feeds'


def result_func(request):
    return render(
        request,
        'wedding_app/done.html'
    )
