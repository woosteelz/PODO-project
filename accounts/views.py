from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST
from .forms import CustomUserChangeForm


# Create your views here.
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/workspaces/')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('/accounts/login/')


@require_POST
def logout(request):
    auth_logout(request)
    return redirect('/accounts/login/')