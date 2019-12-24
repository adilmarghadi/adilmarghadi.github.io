from django.shortcuts import render, redirect
from .forms import ContactForm


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
def home(request):
	return render(request,'home.html')
def about(request):
	return render(request,'about.html')


def contact(request):
    contact_form = ContactForm(request.POST or None)
    if contact_form.is_valid():
        contact_form.save()
        return redirect('contact')
    context = {
        "form": contact_form
    }
    return render(request, "contact.html",context)

def register(request):

	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login_url')

	else:
		form = UserCreationForm()


	return	render(request,'registration/register_url.html',{'form':form})

@login_required

def logout_request(request):
    logout(request)
    return redirect("/")