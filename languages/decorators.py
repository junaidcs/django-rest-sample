from django.http import HttpResponse
from django.shortcuts import redirect
# from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import get_authorization_header, get_user_model


def check_group_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        print(request.user.is_authenticated)
        print(request.user)
        header = get_authorization_header(request)
        print(get_user_model())
        # header = request.headers
        # print(header)
        # token = request.get_raw_token(header)
        # print(token)
        return view_func(request, *args, **kwargs)

    return wrapper_func
