from django.http.response import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from workspaces.forms import WorkspaceForm, CategoryForm
from .forms import ArticleForm, CommentForm
from workspaces.models import Workspace, Category
from .models import Board, Article, Comment, Image, File
from schedules.calendar import MiniCalendar
import datetime
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
# 아직 데코레이터는 완벽하게 첨가하지 않음!!
# 게시글 만들기랑 댓글 작성 워크스페이스 멤버만 가능하도록 하는 것 아직 안 함


# Create your views here.
@require_safe
def index_article(request, workspace_pk, category_pk):
    # 보드와 사이드 캘린더를 보여준다.
    # 보드 안에 게시글은 우선순위와 제목을 작은 카드형식으로 보여준다.
    # 보드 안의 게시글은 내부 스크롤을 통해 볼 수 있다.
    workspace_b = get_object_or_404(Workspace, pk=workspace_pk)
    category = get_object_or_404(Category, pk=category_pk)
    todo_board = get_object_or_404(Board, pk=1)
    doing_board = get_object_or_404(Board, pk=2)
    issue_board = get_object_or_404(Board, pk=3)
    completed_board = get_object_or_404(Board, pk=4)
    todo_articles = Article.objects.filter(workspace_id=workspace_pk, category_id=category_pk, board_id=1).order_by('priority')
    doing_articles = Article.objects.filter(workspace_id=workspace_pk, category_id=category_pk, board_id=2).order_by('priority')
    issue_articles = Article.objects.filter(workspace_id=workspace_pk, category_id=category_pk, board_id=3).order_by('priority')
    completed_articles = Article.objects.filter(workspace_id=workspace_pk, category_id=category_pk, board_id=4).order_by('priority')
    article_form = ArticleForm()
    workspace_form = WorkspaceForm()
    category_form = CategoryForm()
    workspace_list = Workspace.objects.order_by('-pk')
    workspaces = []
    user = request.user
    for work in workspace_list:
        if user.groups.filter(name=work.id):
            workspaces.append(work)
    workspace_indivisual = get_object_or_404(Workspace, pk=workspace_pk)
    today = datetime.datetime.today()

    minicalendar = MiniCalendar(today.year, today.month)
    html_calendar = minicalendar.formatmonth(workspace_pk, withyear=True)
    html_coming_schedules = minicalendar.coming_schedules(workspace_pk, withyear=True)

    context = {
        'workspace_pk': workspace_pk,
        'minicalendar': mark_safe(html_calendar),
        'coming_schedules': mark_safe(html_coming_schedules),
        'workspace_indivisual':workspace_indivisual,
        'workspace_b': workspace_b,
        'category': category,
        'todo_board': todo_board,
        'doing_board': doing_board,
        'issue_board': issue_board,
        'completed_board': completed_board,
        'todo_articles': todo_articles,
        'doing_articles': doing_articles,
        'issue_articles': issue_articles,
        'completed_articles': completed_articles,
        'article_form': article_form,
        'workspace_form': workspace_form,
        'category_form': category_form,
        'workspaces': workspaces,
        'category_name': category.name,
    }
    return render(request, 'articles/index_article.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create_article(request, workspace_pk, category_pk, board_pk):
    # 각 보드의 '+' 버튼을 클릭하면 게시글 추가 오버레이를 보여준다.
    # 사용자가 작성을 마친 뒤, POST 요청을 보내면 유효성 검사를 한 후 저장한다.
    # 저장이 완료되면 다시 index 페이지로 리다이렉트 해준다.
    workspace = get_object_or_404(Workspace, pk=workspace_pk)
    category = get_object_or_404(Category, pk=category_pk)
    board = get_object_or_404(Board, pk=board_pk)
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article =  article_form.save(commit=False)
            article.user = request.user
            article.workspace = workspace
            article.category = category
            article.board = board
            article.save()

            file_list = request.FILES.getlist('file')
            for file in file_list:
                file = File.objects.create(file=file, article_id=article.pk)

            image_list = request.FILES.getlist('image')
            for image in image_list:
                image = Image.objects.create(image=image, article_id=article.pk)
            return redirect('articles:index_article', workspace.pk, category.pk)
    return redirect('articles:index_article', workspace.pk, category.pk)


def modify_article_board(request, article_pk, board_pk):
    article = get_object_or_404(Article, pk=article_pk)
    to_board = get_object_or_404(Board, pk=board_pk)
    article.board = to_board
    article.save()
    context = {
        'workspace_b': article.workspace.pk,
        'category': article.category.pk,
    }
    return JsonResponse(context)


@require_safe
def detail_article(request, article_pk):
    # 보드 안에 작은 카드형식의 게시글을 클릭하면 상세 페이지를 보여준다.
    # 상세 페이지 안에서 뒤로가기 버튼을 만들어 준다.
    # 상세 페이지 안에서 게시글을 수정 및 삭제가 가능하다.
    # 상세 페이지 안에서 댓글 작성이 가능하다.
    article = get_object_or_404(Article, pk=article_pk)
    article_form = ArticleForm(instance=article)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    workspace_form = WorkspaceForm()
    category_form = CategoryForm()
    workspace = Workspace.objects.order_by('-pk')
    workspaces = []
    user = request.user
    for work in workspace:
        if user.groups.filter(name= work.name):
            workspaces.append(work)
    workspace_indivisual = get_object_or_404(Workspace, pk=article.workspace.pk)
    context = {
        'article': article,
        'article_form': article_form,
        'comment_form': comment_form,
        'comments': comments,
        'workspace_form': workspace_form,
        'category_form': category_form,
        'workspaces': workspaces,
        'workspace_indivisual': workspace_indivisual,
    }
    return render(request, 'articles/detail_article.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def update_article(request, article_pk):
    # 상세 페이지 안에서 게시글 수정을 클릭하면 게시글 수정 페이지를 보여준다.
    # 수정을 완료하면 다시 게시글을 상세 페이지를 보여준다.
    article = get_object_or_404(Article, pk=article_pk)
    if request.user == article.user:
        if request.method == 'POST':
            article_form = ArticleForm(request.POST, instance=article)
            if article_form.is_valid():
                article_form.save()

                file_list = request.FILES.getlist('file')
                for file in file_list:
                    file = File.objects.create(file=file, article_id=article.pk)

                image_list = request.FILES.getlist('image')
                for image in image_list:
                    image = Image.objects.create(image=image, article_id=article.pk)
                return redirect('articles:detail_article', article.pk)
    return redirect('articles:detail_article'. article.pk)


@require_POST
def delete_article(request, article_pk):
    # 상세 페이지 안에서 게시글 삭제를 클릭하면 게시글을 삭제여부를 다시 한번 물어보고 삭제한다.
    # 삭제를 완료하면 index로 리다이렉트 해준다
    article = get_object_or_404(Article, pk=article_pk)
    if request.user == article.user:
        workspace = article.workspace
        category = article.category
        article.delete()
    return redirect('articles:index_article', workspace.pk, category.pk)


@login_required
@require_http_methods(['GET', 'POST'])
def create_comment(request, article_pk):
    # 상세 페이지 안에서 댓글을 작성한다.
    # 댓글을 작성하면, 작성자와 댓글 내용, 수정 및 삭제 버튼을 보여준다.
    article = get_object_or_404(Article, pk=article_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
        return redirect('articles:detail_article', article.pk)
    context = {
        'comment_form': comment_form,
        'article': article,
        'comments': article.comment_set.all(),
    }
    return render(request, 'articles/detail_article.html', context)


@require_POST
def delete_comment(request, article_pk, comment_pk):
    # 댓글 삭제를 누르면, 사용자에게 댓글 삭제여부를 다시 한번 물어보고 삭제한다.
    # 삭제를 완료하면, 게시글 상세 페이지를 리다이렉트 해준다.
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('articles:detail_article', article.pk)


@require_POST
def delete_image(request, article_pk, image_pk):
    article = get_object_or_404(Article, pk=article_pk)
    image = get_object_or_404(Image, pk=image_pk)
    if request.user == article.user:
        image.delete()
    return redirect('articles:detail_article', article.pk)


@require_POST
def delete_file(request, article_pk, file_pk):
    article = get_object_or_404(Article, pk=article_pk)
    file = get_object_or_404(File, pk=file_pk)
    if request.user == article.user:
        file.delete()
    return redirect('articles:detail_article', article.pk)