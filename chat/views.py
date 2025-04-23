from django.shortcuts import render, redirect
from .models import Message
from django.contrib.auth.decorators import login_required

@login_required
def chat_room(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(user=request.user, content=content)
            return redirect('/chat/')
    messages = Message.objects.order_by('-timestamp')[:50][::-1]  # 최근 50개만
    return render(request, 'chat/chat_room.html', {'messages': messages})