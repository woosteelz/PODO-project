from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm, CommentForm
from workspaces.models import Workspace, Category
from .models import Board, Article, Comment, Image, File
# 아직 데코레이터는 완벽하게 첨가하지 않음!!


# Create your views here.
@require_safe
def index(request, workspace_pk, category_pk):
    # 보드와 사이드 캘린더를 보여준다.
    # 보드 안에 게시글은 우선순위와 제목을 작은 카드형식으로 보여준다.
    # 보드 안의 게시글은 내부 스크롤을 통해 볼 수 있다.
    workspace = get_object_or_404(Workspace, pk=workspace_pk)
    category = get_object_or_404(Category, pk=category_pk)
    todo_board = get_object_or_404(Board, pk=1)
    doing_board = get_object_or_404(Board, pk=2)
    issue_board = get_object_or_404(Board, pk=3)
    completed_board = get_object_or_404(Board, pk=4)
    todo_articles = Article.objects.filter(workspace_id=workspace_pk, category_id=category_pk, board_id=1)
    doing_articles = Article.objects.filter(workspace_id=workspace_pk, category_id=category_pk, board_id=2)
    issue_articles = Article.objects.filter(workspace_id=workspace_pk, category_id=category_pk, board_id=3)
    completed_articles = Article.objects.filter(workspace_id=workspace_pk, category_id=category_pk, board_id=4)
    form = ArticleForm()
    
    context = {
        'workspace': workspace,
        'category': category,
        'todo_board': todo_board,
        'doing_board': doing_board,
        'issue_board': issue_board,
        'completed_board': completed_board,
        'todo_articles': todo_articles,
        'doing_articles': doing_articles,
        'issue_articles': issue_articles,
        'completed_articles': completed_articles,
        'form': form,
    }
    return render(request, 'articles/index.html', context)


@require_http_methods(['GET', 'POST'])
def create_article(request, workspace_pk, category_pk, board_pk):
    # 각 보드의 '+' 버튼을 클릭하면 게시글 추가 오버레이를 보여준다.
    # 사용자가 작성을 마친 뒤, POST 요청을 보내면 유효성 검사를 한 후 저장한다.
    # 저장이 완료되면 다시 index 페이지로 리다이렉트 해준다.
    workspace = get_object_or_404(Workspace, pk=workspace_pk)
    category = get_object_or_404(Category, pk=category_pk)
    board = get_object_or_404(Board, pk=board_pk)
    print(request.POST)
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            print('통과함')
            article = form.save(commit=False)
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
            return redirect('articles:index', workspace.pk, category.pk)
    print('통과못함')
    print(form.errors)
    return redirect('articles:index', workspace.pk, category.pk)


@require_safe
def detail_article(request, article_pk):
    # 보드 안에 작은 카드형식의 게시글을 클릭하면 상세 페이지를 보여준다.
    # 상세 페이지 안에서 뒤로가기 버튼을 만들어 준다.
    # 상세 페이지 안에서 게시글을 수정 및 삭제가 가능하다.
    # 상세 페이지 안에서 댓글 작성이 가능하다.
    article = get_object_or_404(Article, pk=article_pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail_article.html', context)


@require_http_methods(['GET', 'POST'])
def update_article(request, article_pk):
    # 상세 페이지 안에서 게시글 수정을 클릭하면 게시글 수정 페이지를 보여준다.
    # 수정을 완료하면 다시 게시글을 상세 페이지를 보여준다.
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()

            file_list = request.FILES.getlist('file')
            for file in file_list:
                file = File.objects.create(file=file, article_id=article.pk)

            image_list = request.FILES.getlist('image')
            for image in image_list:
                image = Image.objects.create(image=image, article_id=article.pk)
            return redirect('articles:detail_article', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'article/update_article.html', context)


@require_POST
def delete_article(request, article_pk):
    # 상세 페이지 안에서 게시글 삭제를 클릭하면 게시글을 삭제여부를 다시 한번 물어보고 삭제한다.
    # 삭제를 완료하면 index로 리다이렉트 해준다
    article = get_object_or_404(Article, pk=article_pk)
    workspace = article.workspace
    category = article.category
    article.delete()
    return redirect('articles:index', workspace.pk, category.pk)


@require_POST
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
    comment.delete()
    return redirect('articles:detail_article', article.pk)