from django.shortcuts import render
from django.http import HttpResponse

from .forms import UserdetailsForm
from .models import Userdetails

# Create your views here.
def index(request):
	return render(request, 'index.html')

def create_user(request):
	if request.method == 'POST':
		form = UserdetailsForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("User Created!!!")
	else:
		form = UserdetailsForm()
		return render(request, 'create_user.html', {'form': form})


