from django.shortcuts import render
from .models import QuestFeedBack
from django.http import HttpResponseRedirect
from .forms import QuestFeedBackForm, AuthForm
from .models import QuestFeedBack, AuthModel
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


from django.views import View
from django.views.generic import ListView
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages


class AuthView(View):
    def get(self, request):
        if request.session.get('authenticated'):
            return HttpResponseRedirect('/show_info')
        form = AuthForm()
        return render(
            request,
            'wedding_app/auth.html',
            context={'form': form}
        )

    def post(self, request):
        form = AuthForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['field'] == form._meta.model.SECRET_QUEST_PASSWORD:
                request.session['authenticated'] = True
                request.session.set_expiry(3600)
                return HttpResponseRedirect('/show_info')
            else:
                messages.error(request, 'Неверный пароль')
        return render(
            request,
            'wedding_app/auth.html',
            context={'form': form}
        )


class ListQuests(ListView):
    template_name = 'wedding_app/show_info.html'
    model = QuestFeedBack
    context_object_name = 'feeds'

    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('authenticated'):
            return HttpResponseRedirect('/secret')
        return super().dispatch(request, *args, **kwargs)


def result_func(request):
    return render(
        request,
        'wedding_app/done.html'
    )
