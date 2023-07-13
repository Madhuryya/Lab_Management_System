from django.urls import path

from .views import getItem





urlpatterns = [
	#  path('', views.ApiOverview, name='home')
	 path('getData',getItem.as_view()),
    
	# path('getData/', getItem.as_view()),
    # path('postData/', postItem.as_view()),
]