from datetime import datetime

from django.shortcuts import render

from accounts.models import User
from mall.models import Product
from system.models import Slider, News
from utils import constants


def index(request):
    """ home page """
    # Query carousel
    slider_list = Slider.objects.filter(types=constants.SLIDER_TYPE_INDEX)

    # Home News
    now_time = datetime.now()
    # Pinned, effective, within time
    news_list = News.objects.filter(types=constants.NEWS_TYPE_NEW,
                                    is_top=True,
                                    is_valid=True,
                                    start_time__lte=now_time,
                                    end_time__gte=now_time)

    # Lipstick recommendation
    js_list = Product.objects.filter(
        status=constants.PRODUCT_STATUS_SELL,
        is_valid=True,
        tags__code='jstj'
    )
    # Featured Recommended
    jx_list = Product.objects.filter(
        status=constants.PRODUCT_STATUS_SELL,
        is_valid=True,
        tags__code='jxtj'
    )
    # # Get user ID from session
    # user_id = request.session[constants.LOGIN_SESSION_ID]
    # print(user_id)
    # # Query the currently logged in user
    # user = User.objects.get(pk=user_id)
    # # if not user_id:
    # #     return 403
    return render(request, 'index.html', {
        'slider_list': slider_list,
        'news_list': news_list,
        'jx_list': jx_list,
        'js_list': js_list,
        # 'user': user
    })
