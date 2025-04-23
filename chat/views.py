from django.http import HttpResponse

def chat_home(request):
    return HttpResponse("이곳은 채팅 페이지입니다.")