from django.urls import path,include
from . import views
from .views import ItemViewSet
from .views import postItem, getItem




urlpatterns = [
	#  path('', views.ApiOverview, name='home')
	 path('getData',getItem.as_view),
	# path('getData/', getItem.as_view()),
    # path('postData/', postItem.as_view()),
]