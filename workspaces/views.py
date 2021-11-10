from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Workspace,Category
from .forms import CategoryForm, WorkspaceForm


# Create your views here.
@login_required
def index(request):
    workspace = Workspace.objects.order_by('-pk')
    form = WorkspaceForm()
    context = {
        'form' : form,
        'workspace': workspace,
    }
    return render(request, 'workspaces/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create_workspace(request):
    if request.method == 'POST':
        form = WorkspaceForm(request.POST, request.FILES)
        if form.is_valid():
            workspace = form.save(commit=False)
            workspace.user = request.user
            workspace.save()
            return redirect('workspaces:index')
    else:
        form = WorkspaceForm()
    context = {
        'form' : form,
    }
    return redirect('workspaces:index')

@login_required
@require_http_methods(['GET', 'POST'])
def delete_workspace(request, workspace_pk):
    workspace = get_object_or_404(Workspace, pk=workspace_pk)
    if request.user == workspace.user:
        workspace.delete()
    return redirect('workspaces:index')


@login_required
def index_category(request,workspace_pk):
    workspace = Workspace.objects.order_by('-pk')
    workspace_indivisual = get_object_or_404(Workspace, pk=workspace_pk)
    form = CategoryForm()
    category = Category.objects.all()
    context = {
        'form' : form,
        'workspace': workspace,
        'workspace_indivisual' : workspace_indivisual,
        'category': category,
    }
    return render(request, 'workspaces/category_index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create_category(request,workspace_pk):
    workspace = Workspace.objects.order_by('-pk')
    workspace_indivisual = get_object_or_404(Workspace, pk=workspace_pk)
    form = CategoryForm(request.POST)  
    
    category = form.save(commit=False)
    category.workspace = workspace_indivisual
    category.user = request.user
    category.save()
    return redirect('workspaces:index_category', workspace_pk)

@login_required
@require_POST
def delete_category(request, workspace_id, category_id):
    workspace = get_object_or_404(Workspace, pk=workspace_id)
    category = get_object_or_404(Category, pk=category_id)
    if request.user == category.user:
        category.delete()
    return redirect('workspaces:index')

@login_required
@require_POST
def like_category(request, workspace_pk, category_pk):
    category  = get_object_or_404(Category, pk=category_pk)
    workspace_indivisual = get_object_or_404(Workspace, pk=workspace_pk)

    if category.like_users.filter(pk=request.user.pk).exists():       
        category.like_users.remove(request.user)   
    else:       
        category.like_users.add(request.user)
    return redirect(request.META.get('HTTP_REFERER'))