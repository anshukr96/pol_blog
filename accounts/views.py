from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login as auth_login
# Create your views here.
def signup(request):
	if request.method=='POST': #if post button is clicked
		form = SignUpForm(request.POST) #create userform by giving request
		if form.is_valid():  #check for validation for form
			user = form.save() #save form in name of user
			auth_login(request,user) #login with the user
			return redirect('home') #redirect the page to home
	else:
		form = SignUpForm()
	return render(request,'signup.html', {'form':form})	

