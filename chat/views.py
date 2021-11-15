from django.shortcuts import render
from workspaces.models import Workspace
from .models import Message


def index(request):
    workspace = Workspace.objects.order_by('-pk')
    workspaces = []
    user = request.user
    for work in workspace:
        if user.groups.filter(name=work.name):
            workspaces.append(work)
    print(workspaces)
    context = {
        'username': user,
        'workspaces': workspaces
    }
    return render(request, 'chat/index.html', context)


def room(request, room_name):
    username = request.GET.get('username', 'Anonymous')
    messages = Message.objects.filter(room=room_name)

    return render(request, 'chat/room.html', {'room_name': room_name, 'username': username, 'messages': messages})
