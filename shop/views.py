from django.http import HttpResponse

def home(request):
    return HttpResponse("""
    <h1>Главная страница магазина термосов.</h1>
    
    Перейти:
    <p><a href = "/about/">Страница об авторе</a></p>
    <p><a href = "/store/">Страница магазина</a></p>
    """)

def about(request):
    return HttpResponse("""
    <h1>Страница об авторе.</h1>

    <p>Лабораторную работу выполнил: Ковалёв Станислав 87ТП.</p>
    """)

def store(request):
    return HttpResponse("""
    <h1>Страница магазина.</h1>
    
    <p>Тема лабораторной: Интернет-магазин термосов.</p>

    <p>Ассортимент:</p>
    <p>- Термос для чая</p>
    <p>- Термос для кофе</p>
    <p>- Термокружка</p>
    """)