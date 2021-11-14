from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout as auth_logout, update_session_auth_hash
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm
from django.contrib.auth.forms import PasswordChangeForm

from invitations.utils import get_invitation_model


# Create your views here.
@login_required
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


@require_POST
def delete_image(request):
    user = request.user
    user.image = None
    user.save()
    return redirect('accounts:update')


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('/accounts/login/')


@require_POST
def logout(request):
    auth_logout(request)
    return redirect('/accounts/login/')


@login_required
@require_http_methods(['GET', 'POST'])
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/workspaces/')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/password_change.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def invitations_send_invite(request):
    if request.method == 'POST':
        Invitation = get_invitation_model()
        email = request.POST.get('email')
        invite = Invitation.create(email, inviter=request.user)
        invite.send_invitation(request)
        return redirect('/workspaces/')
    else:
        pass
    context = {}
    return render(request, 'accounts/invite.html', context)