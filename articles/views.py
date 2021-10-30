from django.shortcuts import render, redirect, get_object_or_404
from .models import Board, Article, Comment, Image, File

# Create your views here.
def index(request):
    # 보드와 사이드 캘린더를 보여준다.
    # 보드 안에 게시글은 우선순위와 제목을 작은 카드형식으로 보여준다.
    # 보드 안의 게시글은 내부 스크롤을 통해 볼 수 있다.
    pass


def create_article(request):
    # 각 보드의 '+' 버튼을 클릭하면 게시글 추가 오버레이를 보여준다.
    # 사용자가 작성을 마친 뒤, POST 요청을 보내면 유효성 검사를 한 후 저장한다.
    # 저장이 완료되면 다시 index 페이지로 리다이렉트 해준다.
    pass


def detail_article(request, article_pk):
    # 보드 안에 작은 카드형식의 게시글을 클릭하면 상세 페이지를 보여준다.
    # 상세 페이지 안에서 뒤로가기 버튼을 만들어 준다.
    # 상세 페이지 안에서 게시글을 수정 및 삭제가 가능하다.
    # 상세 페이지 안에서 댓글 작성이 가능하다.
    pass


def update_article(request, article_pk):
    # 상세 페이지 안에서 게시글 수정을 클릭하면 게시글 수정 페이지를 보여준다.
    # 수정을 완료하면 다시 게시글을 상세 페이지를 보여준다.
    pass


def delete_article(request, article_pk):
    # 상세 페이지 안에서 게시글 삭제를 클릭하면 게시글을 삭제여부를 다시 한번 물어보고 삭제한다.
    # 삭제를 완료하면 index로 리다이렉트 해준다
    pass


def create_comment(request, article_pk):
    # 상세 페이지 안에서 댓글을 작성한다.
    # 댓글을 작성하면, 작성자와 댓글 내용, 수정 및 삭제 버튼을 보여준다.
    pass


def update_comment(request, article_pk, comment_pk):
    # 댓글 수정을 누르면, 사용자가 댓글을 수정할 수 있는 form을 다시 한번 보여준다.
    # 수정을 완료하면, 수정된 댓글 내용을 보여준다.
    pass


def delete_comment(request, article_pk, comment_pk):
    # 댓글 삭제를 누르면, 사용자에게 댓글 삭제여부를 다시 한번 물어보고 삭제한다.
    # 삭제를 완료하면, 게시글 상세 페이지를 리다이렉트 해준다.
    pass