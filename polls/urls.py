from django.urls import path
from . import views

"""We are able to call a view by mapping it to a url and that's what we do here,we just call the view as in our view
(view.index) create in the views.py file and in such a way we map it to a URL. In this way we are calling a view so that it will be selected
and it is the one that produces and delivers a response to the web browser
 """
urlpatterns = [
    #we have called a view by mapping it to a URL config
    #we called our view here 'index' by mapping it to our urlconfig
    path('', views.index, name='index'),
]