from django.core.paginator import Paginator
from django.db.models import F
from django.shortcuts import render, get_object_or_404

# Create your views here.
from system.models import News
from utils import constants
from utils.verify import VerifyCode


def news_list(request, template_name='news_list.html'):
    """ news_list """
    # Current page number
    page = request.GET.get('page', 1)
    page_size = 20  # Put 20 data per page

    news = News.objects.filter(types=constants.NEWS_TYPE_NEW,
                               is_valid=True)
    paginator = Paginator(news, page_size)
    page_data = paginator.page(page)
    return render(request, template_name, {
        'page_data': page_data
    })


def news_detail(request, pk, template_name='news_info.html'):
    """ news detail """
    new_obj = get_object_or_404(News, pk=pk, is_valid=True)
    # +1 views per view
    new_obj.view_count = F('view_count') + 1
    new_obj.save()
    # Retrieve data from the database
    new_obj.refresh_from_db()
    return render(request, template_name, {
        'new_obj': new_obj
    })


def verify_code(request):
    """ Verification code display """
    client = VerifyCode(request)
    return client.gen_code()