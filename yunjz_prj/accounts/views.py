#coding=utf-8
#django package
#copyright by Vincent

from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User  
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login ,logout as auth_logout
from django.core.urlresolvers import reverse
from django.template.loader import get_template
from django.template import Context
from django.template.context import RequestContext
from django.http import HttpResponseRedire

def index(request):
	username = "vincent"
	return render(request, "accounts/index.html", {"username": username})

def register(request):
	'''注册视图'''
	if request.method == "POST":
		#注册完毕，直接登录
		return HttpResponseRedirect("/accounts/index")
	return render(request, "accounts/register.html")

def login(request):
	'''登录视图'''
	template_var = {}
	if request.method == "POST":
		username = request.POST.get("username")
		template_var = {"error": "must first regitster", "username": username}
	return render(request, "accounts/login.html", template_var)

def logout(request):
	return render(request, "accounts/logout.html")


