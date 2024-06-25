from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='Home-page'),
    path('about/', views.about, name='about-page'),
    path('course/', views.course, name='course-page'),
    path('blog/', views.blog, name='blog-page'),
    path('contact/', views.contact, name='contact-page'),
    path('predict/', views.predict, name='predict')

]
