from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Workspace
from .forms import WorkspaceForm


# Create your views here.
@login_required
def index(request):
    workspace = Workspace.objects.order_by('-pk')
    form = WorkspaceForm()
    context = {
        'workspace': workspace,
        'form': form,
    }
    return render(request, 'workspaces/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create_workspace(request):
    if request.method == 'POST':
        form = WorkspaceForm(request.POST, request.FILES)
        if form.is_valid():
            workspace = form.save()
            # workspace.user = request.user
            workspace.save()
            return redirect('workspaces:index')
    else:
        form = WorkspaceForm()
    context = {
        'form' : form,
    }
    return redirect('workspaces:index')