from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Workspace,Category
from .forms import CategoryForm, WorkspaceForm
from django.contrib import messages
from django.contrib.auth.models import Group
from articles.models import Article, Comment
from schedules.models import Schedule
from django.db.models import Q


# Create your views here.
@login_required
def index(request):
    # 이 부분이 사실상 워크 스페이시스
    # --------------------------------------------
    workspace = Workspace.objects.order_by('-pk')
    workspaces = []
    user = request.user
    for work in workspace:
        if user.groups.filter(name= work.name):
            workspaces.append(work)
    # --------------------------------------------
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
            user = request.user
            print(user)
            workspace.save()
            new_group = Group.objects.create(name= workspace.name)
            user.groups.add(new_group)
            return redirect('workspaces:index_category', workspace.pk)
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
    else:
        messages.warning(request, "권한이 없습니다.")
    return redirect('workspaces:index')


@login_required
def index_category(request, workspace_pk):
    workspace = Workspace.objects.order_by('-pk')
    workspaces = []
    user = request.user
    for work in workspace:
        if user.groups.filter(name= work.name):
            workspaces.append(work)
            
    workspace_form = WorkspaceForm()
    workspace_indivisual = get_object_or_404(Workspace, pk=workspace_pk)
    if not user.groups.filter(name= workspace_indivisual.name):
        return redirect('https://www.google.com/search?q=%EC%96%B4%EB%94%9C+%EA%B0%90%ED%9E%88&oq=%EC%96%B4%EB%94%9C+%EA%B0%90%ED%9E%88&aqs=chrome..69i57j0i433i512j0i131i433i512j46i199i433i465i512j0i433i512j69i61l3.1890j0j7&sourceid=chrome&ie=UTF-8')
    category_form = CategoryForm()
    category = Category.objects.all()
    context = {
        'workspace_pk': workspace_pk,
        'category_form' : category_form ,
        'workspaces': workspaces,
        'workspace_indivisual' : workspace_indivisual,
        'workspace_form' : workspace_form,
        'category': category,
    }
    return render(request, 'base.html', context)


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


@login_required
def search(request, workspace_pk):
    word = request.GET.get('word')
    articles = Article.objects.filter(workspace_id= workspace_pk).filter(Q(title__icontains=word) | Q(content__icontains=word)).distinct()
    # comments = Comment.objects.filter(workspace_id= workspace_pk).filter(content__icontains=word)
    schedules = Schedule.objects.filter(workspace_id= workspace_pk).filter(Q(title__icontains=word) | Q(content__icontains=word)).distinct()
    workspace = Workspace.objects.order_by('-pk')
    workspaces = []
    user = request.user
    for work in workspace:
        if user.groups.filter(name= work.name):
            workspaces.append(work)
    category_form = CategoryForm()
    category = Category.objects.all()
    workspace_indivisual = get_object_or_404(Workspace, pk=workspace_pk)

    context = {
        'articles': articles,
        # 'comments': comments,
        'schedules': schedules,
        'workspace_pk': workspace_pk,
        'workspaces': workspaces,
        'category_form': category_form,
        'category': category,
        'workspace_indivisual': workspace_indivisual,
        

    }
    return render(request, 'workspaces/search.html', context)

