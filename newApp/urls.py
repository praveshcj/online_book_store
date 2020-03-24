from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name= 'login'),
    path('profile', views.userProfile, name = 'profile'),
    path('logout', views.userLogout, name='logout'),
    path('userSignUp', views.signup, name='UserSignUp'),
    path('storeSignUp', views.storeSignUp, name = 'storeSignUp'),
    path('storeLogin',views.storeLogin, name= 'storeLogIn'),
    path('storeProfile', views.storeProfile, name = 'storeProfile'),
    path('storeLogout', views.storeLogout, name = 'storeLogout'),
    path('addBook', views.storeBookAdd, name = "storeAddBook"),
    path('userBookList/', views.userBookList,  name = "userBooks"),
    path('removeBook/<int:book_id>/', views.userRemoveBook, name = 'removeBook'),
    path('viewBook/<int:book_id>/', views.viewBook, name= 'viewBook'),
    path('searchBooks', views.searchBooks, name = 'searchBooks')
]

