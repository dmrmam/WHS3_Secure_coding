from django.http import HttpResponse

def product_home(request):
    return HttpResponse("이곳은 상품 페이지입니다.")