from django.shortcuts import redirect, render
from.models import TimFerrissPodcast
from.forms import TimFerrissForm

# Create your views here.
def home(request):
    return render(request,'index.html')

def form_page(request):
    form = TimFerrissForm()
    if request.method == 'POST':
       form = TimFerrissForm(request.POST)
       if form.is_valid():
           form.save(commit=True)
           return redirect('home')
    else:
        print("ERROR FORM IS INVALID")
    return render(request,'forms.html',{'form': form})