from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Workspace,Category
from .forms import CategoryForm, WorkspaceForm


# Create your views here.
@login_required
def index(request):
    workspaces = Workspace.objects.order_by('-pk')
    workspace_form = WorkspaceForm()
    context = {
        'workspace_form' : workspace_form,
        'workspaces': workspaces,
    }
    return render(request, 'workspaces/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create_workspace(request):
    if request.method == 'POST':
        workspace_form = WorkspaceForm(request.POST, request.FILES)
        if workspace_form.is_valid():
            workspace = workspace_form.save(commit=False)
            workspace.user = request.user
            workspace.save()
            return redirect('workspaces:index')
    else:
        workspace_form = WorkspaceForm()
    context = {
        'workspace_form' : workspace_form,
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
def index_category(request, workspace_pk):
    workspaces = Workspace.objects.order_by('-pk')
    workspace_indivisual = get_object_or_404(Workspace, pk=workspace_pk)
    category_form = CategoryForm()
    category = Category.objects.all()
    context = {
        'category_form' : category_form ,
        'workspaces': workspaces,
        'workspace_indivisual' : workspace_indivisual,
        'category': category,
    }
    return render(request, 'workspaces/category_index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create_category(request, workspace_pk):
    workspaces = Workspace.objects.order_by('-pk')
    workspace_indivisual = get_object_or_404(Workspace, pk=workspace_pk)
    category_form = CategoryForm(request.POST)  
    
    category = category_form.save(commit=False)
    category.workspace = workspace_indivisual
    category.user = request.user
    category.save()
    return redirect('articles:index_article', workspace_indivisual.pk, category.pk)

  
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