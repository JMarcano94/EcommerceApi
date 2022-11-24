from django.urls import path, include
from rest_framework.routers import SimpleRouter
from User import views


app_name = 'User'

router = SimpleRouter()
router.register(r'register', views.RegisterView, basename="registro")




urlpatterns = [
    
    path('', include(router.urls)),
    path('reset/',views.ResetPasswordView.as_view(),name= "password_reset_confirm"),
    path('reset/<token>/',views.ChangepasswordView.as_view(),name= "password_reset_confirm"),
   
   
]