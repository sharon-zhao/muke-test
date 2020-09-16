# coding:utf-8

import datetime

from django.views.generic import View
from django.shortcuts import redirect, reverse
from django.http import JsonResponse
from app.libs.base_render import render_to_response
from app.model.auth import ClientUser
from app.utils.permission import client_auth
from app.utils.consts import COOKIE_NAME


class User(View):
    TEMPLATE = 'client/auth/user.html'

    def get(self, request):

        user = client_auth(request)
        data = {'user': user}
        return render_to_response(request, self.TEMPLATE, data=data)

    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        if not all([username, password]):
            error = 'Required fields are missing'
            return JsonResponse({'code': -1, 'msg': error})

        user = ClientUser.get_user(username, password)

        if not user:
            error = 'Username or password is wrong, the user was not found'
            return JsonResponse({'code': -1, 'msg': error})

        response = render_to_response(request, self.TEMPLATE)
        response.set_cookie(COOKIE_NAME, str(user.id))
        return response


class Regist(View):
    TEMPLATE = 'client/auth/user.html'

    def post(self, request):
        print('run this line')
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        if not all([username, password]):
            error = 'Required fields are missing'
            return JsonResponse({'code': -1, 'msg': error})

        exists = ClientUser.objects.filter(username=username).exists()

        if exists:
            error = 'The username already exists!'
            return JsonResponse({'code': -1, 'msg': error})

        ClientUser.add(username=username, password=password)
        return JsonResponse({'code': 0, 'msg': 'Registered successfully, please log in'})


class Logout(View):
    TEMPLATE = 'client/auth/user.html'

    def get(self, request):

        response = render_to_response(request, self.TEMPLATE)
        response.set_cookie(COOKIE_NAME, '')
        return response
