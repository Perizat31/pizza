from django.shortcuts import render
from django.http import HttpResponse
menu =[{'title':"Главная",'url_name':'home'},
       {'title':"Меню",'url_name':'index'},
       {'title':"Заказы",'url_name':'order'},
       {'title':"Войти",'url_name':'login'},
       {'title':"Корзина",'url_name':'cart'}
       ]

def pizza(request):
    pizza = pizza.objects.all()
    menues=menu.objects.all()
    context={
        'title': "Books",
        'menu': menues,
        'pizzas': pizzas,
        'genre_selected':0,
    }
    return render(request,'stobook/index.html',context=context )
       
def main(request):
    return render(request,'book/main.html',{'title':"Main",'menu':menu} )

def book(request):
    return render(request,'book/book.html',{'title':"Books",'menu':menu} )


def order(request):
    return render(request,'book/order.html',{'title':"Order",'menu':menu} )

def login(request):
    return render(request,'book/login.html',{'title':"Login",'menu':menu} )

def cart(request):
    return render(request,'book/cart.html',{'title':"Cart",'menu':menu} )