from django.http import HttpResponse

def report_home(request):
    return HttpResponse("이곳은 신고 페이지입니다.")