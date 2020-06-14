
# User ID stored in session after login
LOGIN_SESSION_ID = 'user_id'

# System module-carousel configuration
SLIDER_TYPE_INDEX = 11
SLIDER_TYPES_CHOICES = (
    (SLIDER_TYPE_INDEX, 'home page'),
)

# System Module-News Notification
NEWS_TYPE_NEW = 11
NEWS_TYPE_NOTICE = 12
NEWS_TYPES_CHOICES = (
    (NEWS_TYPE_NEW, 'news'),
    (NEWS_TYPE_NOTICE, 'notification'),
)

# Types of goods
PRODUCT_TYPE_ACTUAL = 11
PRODUCT_TYPE_VIRTUAL = 12
PRODUCT_TYPES_CHOICES = (
    (PRODUCT_TYPE_ACTUAL, 'Physical goods'),
    (PRODUCT_TYPE_VIRTUAL, 'virtual merchandise'),
)


# Product status
PRODUCT_STATUS_SELL = 11
PRODUCT_STATUS_LOST = 12
PRODUCT_STATUS_OFF = 13
PRODUCT_STATUS_CHOICES = (
    (PRODUCT_STATUS_SELL, 'on sale'),
    (PRODUCT_STATUS_LOST, 'sold out'),
    (PRODUCT_STATUS_OFF, 'removed'),
)

# Order Status
ORDER_STATUS_INIT = 10
ORDER_STATUS_SUBMIT = 11
ORDER_STATUS_PAIED = 12
ORDER_STATUS_SENT = 13
ORDER_STATUS_DONE = 14
ORDER_STATUS_DELETED = 15
ORDER_STATUS_CHOICES = (
    (ORDER_STATUS_INIT, 'shopping cart'),
    (ORDER_STATUS_SUBMIT, 'submitted'),
    (ORDER_STATUS_PAIED, 'paid'),
    (ORDER_STATUS_SENT, 'shipped'),
    (ORDER_STATUS_DONE, 'finished'),
    (ORDER_STATUS_DELETED, 'deleted'),
)