from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),


    path('userSignUp', views.signup, name='UserSignUp'),
    path('users/login', views.login, name= 'login'),
    path('user/profile', views.userProfile, name = 'userProfile'),
    path('users/change_password', views.userChangePasswd, name='userChangePasswd'),
    path('users/logout', views.userLogout, name='logout'),


    path('users/trending_list', views.userTrendingList, name = "userTrendingList"),


    



    path('storeSignUp', views.storeSignUp, name = 'storeSignUp'),
    path('storeLogin',views.storeLogin, name= 'storeLogIn'),
    path('store/storeProfile', views.storeProfile, name = 'storeProfile'),
    path('store/edit_profie', views.storeEditProfile, name = 'storeEditProfile'),
    path('store/change_password', views.storeChangePasswd, name = "storeChangePasswd"),
    path('store/storeLogout', views.storeLogout, name = 'storeLogout'),
    

    path('store/addBook', views.storeBookAdd, name = 'storeAddBook'),
    
    path('store/book_list', views.storeBookView, name = "storeBookView"),
    path('store/delete_book/<int:book_id>/', views.storeBookDel, name = "storeBookDel"),
    path('store/update_book/<int:book_id>/', views.storeUpdateBook, name = "storeUpdateBook"),
    path('store/user_list', views.storeUserList, name = "storeUserList"),
    path('store/user_address/<str:user_id>/', views.storeUserAddress, name = "storeUserAddress"),
    
    path('store/order_list', views.storeOrderList, name = 'storeOrderList'),
    path('orderDelivered', views.deliveredOrder, name = 'deliveredOrder'),
    path('orderCancelled', views.cancelledOrder, name = 'cancelledOrder'),
    path('orderProcessing', views.inProcessOrder, name='inProcessOrder'),
    path('orderDetails/<slug:order_id>/', views.orderDetails, name = 'orderDetails'),

    path('setDelivered/<slug:order_id>/', views.setDelivered, name='setDelivered'),
    path('setExpectedDeliveryDate/<slug:order_id>/', views.setExpectedDeliveryDate, name='setExpectedDeliveryDate'), 
    path('setProcessing/<slug:order_id>/', views.setProcessing, name='setProcessing'),
    path('setCancelled/<slug:order_id>/', views.setCancelled, name='setCancelled'),   
    
    path('store/trending_list', views.storeTrendingList, name = "storeTrendingList"),

    # path('orderProcessing', views.inProcessOrder, name = 'inProcessOrder'),
    # path('orderCancelled', views.cancelledOrder, name = 'cancelledOrder')
]

