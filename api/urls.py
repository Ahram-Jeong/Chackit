from django.urls import path
from .views import *

app_name = "api"

# domain.com/api/
urlpatterns = [
    # 계정
    path("login/", ApiLoginView.as_view(), name = "login"),
    path("logout/", ApiLogoutView.as_view(), name = "logout"),
    path("me/", ApiMeView.as_view(), name = "me"),
    path("account/create/", ApiRegisterView.as_view(), name = "register"),

    # 도서
    path("book/search/", ApiSearchListView.as_view(), name = "search_book"),
    path("book/<int:pk>/", ApiBookDetailView.as_view(), name = "detail_book"),
    
    # 리뷰
    path("review/create/", ApiReviewCreateView.as_view(), name = "create_review"),
]