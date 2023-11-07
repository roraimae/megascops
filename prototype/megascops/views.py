from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.utils.translation import activate

from .forms import UserRegistrationForm


def home(request):
    activate(request.LANGUAGE_CODE)
    return render(request, 'home.html')


class CustomLoginView(LoginView):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        # O cookie com nome 'sessionid' é apagado
        response = super().get(request, *args, **kwargs)
        response.delete_cookie('sessionid')
        return response


def registration_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        # Verifica se há informações do OAuth disponíveis na sessão
        oauth_info = request.session.get('oauth_info')

        if oauth_info:
            print(oauth_info)
            form = UserRegistrationForm(initial=oauth_info)
            # Limpa as informações do OAuth da sessão para que não sejam usadas novamente
            request.session.pop('oauth_info', None)
        else:
            form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})
