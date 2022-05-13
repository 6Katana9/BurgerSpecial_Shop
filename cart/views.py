from django.shortcuts import render, redirect
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from .models import CartContent, Cart
from products.views import Products


class CartVi(View):

    def get_cart_records(self, cart=None, response=None):
        cart = self.get_cart() if cart is None else cart
        if cart is not None:
            cart_records = CartContent.objects.filter(cart_id=cart.id)
        else:
            cart_records = []

        if response:
            response.set_cookie('cart_count', len(cart_records))
            return response

        return cart_records

    def get_cart(self):
        if self.request.user.is_authenticated:
            user_id = self.request.user.id
            try:
                cart = Cart.objects.get(user_id=user_id)
            except ObjectDoesNotExist:
                cart = Cart(user_id=user_id,
                            total_cost=0)
                cart.save()
        else:
            session_key = self.request.session.session_key
            if not session_key:
                self.request.session.save()
                session_key = self.request.session.session_key
            try:
                cart = Cart.objects.get(session_key=session_key)
            except ObjectDoesNotExist:
                cart = Cart(session_key=session_key,
                            total_cost=0)
                cart.save()

        return cart


class CartView(CartVi):
    def get(self, request):
       

        cart = self.get_cart()
        cart_records = self.get_cart_records(cart)
        cart_total = cart.get_total if cart else 0

        context = {
            'cart_records': cart_records,
            'cart_total': cart_total,
        }
        return render(request, 'cart/cart.html', context)

    def post(self, request):
        dish = Products.objects.get(id=request.POST.get('dish_id'))
        cart = self.get_cart()
        quantity = request.POST.get('qty')
        # get_or_create - найдет обьект, если его нет в базе, то создаст
        # первый параметр - обьект, второй - булевое значение которое сообщает создан ли обьект
        # если обьект создан, то True, если он уже имеется в базе, то False
        cart_content, _ = CartContent.objects.get_or_create(cart=cart, product=dish)
        cart_content.qty = quantity
        if cart != 0:
            cart_content.save()
        response = self.get_cart_records(cart, redirect('/menu/#dish-{}'.format(dish.id)))
        return response

        # перенаправляем на главную страницу, с учетом якоря

    # def delete(self, request):
    #     cart = CartContent.product.objects.get(all=request.GET.get)
    #     CartContent.product.objects.get(cart=cart).delete()

    #     return render(request, 'base.html')
    
