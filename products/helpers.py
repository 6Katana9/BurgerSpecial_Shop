def product_list_filter_sort(request,
                             products,
                             ):
    is_sort_asc = request.GET.get('price')
    is_sort_desc = request.GET.get('-price')

    if is_sort_asc:
        products = products.order_by('price')
    elif is_sort_desc:
        products = products.order_by('-price')
    return products