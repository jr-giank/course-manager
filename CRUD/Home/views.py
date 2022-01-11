from django.shortcuts import redirect, render

from Home.forms import SignUpForm

# Create your views here.
def SignUp(request):

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()


    return render(request, 'SignUp.html', {'form': form})

def Login(request):

    return render(request, 'login.html')