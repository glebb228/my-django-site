from django.shortcuts import render
from .models import QuestFeedBack
from django.http import HttpResponseRedirect
from .forms import QuestFeedBackForm
from django.views import View


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


def result_func(request):
    return render(
        request,
        'wedding_app/done.html'
    )
