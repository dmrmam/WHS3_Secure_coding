from django.http import HttpResponse

def account_home(request):
    return HttpResponse("이곳은 계정 페이지입니다.")