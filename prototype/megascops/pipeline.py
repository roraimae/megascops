from django.shortcuts import redirect

from .models import User


def check_if_user_exists(request, strategy, details, user=None, *args, **kwargs):
    if not user:
        # Verifica se o usuário com o endereço de email informado existe no modelo User
        email = details.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            # Se o usuário não existir no modelo User, armazena as informações do OAuth na sessão
            request = strategy.request
            request.session['oauth_info'] = {
                'email': email,
                'first_name': details.get('first_name'),
                'last_name': details.get('last_name'),
                'date_of_birth': details.get('date_of_birth'),
            }
            return redirect('register')

    return None
