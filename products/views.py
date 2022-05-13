from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView

from .models import Products, Cotegory
from .forms import ProductsForm, SearchForm
from django.contrib.postgres.search import SearchVector
from .helpers import product_list_filter_sort



def index(request):
    return render(request, 'products/index.html')


def about(request):
    return render(request, 'products/about.html')


class NewDetailView(DetailView):
    model = Products
    template_name = 'products/details_view.html'
    context_object_name = "article"


class NewUpdateView(UpdateView):
    model = Products
    template_name = 'products/adda.html'

    form_class = ProductsForm


def get_menu_list(request):
    menus = Products.objects.filter(id='0')
    menu = Products.objects.all()
    cotegory = Cotegory.objects.all()

    menu = product_list_filter_sort(
        request,
        menu
    )
    cots = []
    for c in cotegory:
        if c.products.all():
            cots.append(c)
    # all_dishes = ''

    if request.method == 'POST':
        form = SearchForm(request.POST)
        search = request.POST.get('search')

        if form.is_valid() and search:
            search_vector = SearchVector('name',
                                         'about',
                                         'price',
                                         'companys__name', )
            menus = Products.objects.annotate(search=search_vector).filter(search=search)
    else:
        form = SearchForm

    return render(request, 'products/menu_home.html',
                  {'menu':menu, 'menus': menus, "cotegory":cots, 'form': form, 'user': request.user})


def create_or_update_product(request):
    error = ''
    if request.method == 'POST':
        form = ProductsForm(request.POST, request.FILES)
        print(request.POST)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect('menu')
        else:
            error = 'Форма неверна'

    form = ProductsForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'products/adda.html', data)

def delete_products(request, id):
	Products.objects.get(id=id).delete()
	return redirect('menu')
