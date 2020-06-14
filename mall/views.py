from django.db.models import Q
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView

from mall.models import Product
from utils import constants


def product_list(request, template_name='product_list.html'):
    """ Product list """
    prod_list = Product.objects.filter(
        status=constants.PRODUCT_STATUS_SELL,
        is_valid=True)
    # Search by name
    name = request.GET.get('name', '')
    if name:
        prod_list = prod_list.filter(name__icontains=name)
    return render(request, template_name, {
        'prod_list': prod_list
    })


def product_detail(request, pk, template_name='product_detail.html'):
    """ product details """
    prod_obj = get_object_or_404(Product, uid=pk, is_valid=True)
    # User's default address
    user = request.user
    default_addr = None
    if user.is_authenticated:
        default_addr = user.default_addr
    return render(request, template_name, {
        'prod_obj': prod_obj,
        'default_addr': default_addr
    })


class ProductList(ListView):
    """" Product list """
    # How many pieces of data to put on each page
    paginate_by = 6
    # Template location
    template_name = 'product_list.html'

    def get_queryset(self):
        query = Q(status=constants.PRODUCT_STATUS_SELL,
                  is_valid=True)
        # Search by name
        name = self.request.GET.get('name', '')
        if name:
            query = query & Q(name__icontains=name)

        # Search by label
        tag = self.request.GET.get('tag', '')
        if tag:
            query = query & Q(tags__code=tag)

        # Search by category
        cls = self.request.GET.get('cls', '')
        if cls:
            query = query & Q(classes__code=cls)
        return Product.objects.filter(query)

    def get_context_data(self, **kwargs):
        """ Add variables to the context """
        context = super().get_context_data(**kwargs)
        context['params'] = self.request.GET.dict()
        return context


def prod_classify(request):
    """ Categories """
    return render(request, 'prod_classify.html', {

    })
