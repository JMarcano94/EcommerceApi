from django.urls import path, include
from rest_framework.routers import SimpleRouter
from Products import views 


app_name = 'Products'

router = SimpleRouter()
#router.register(r'register', views.RegisterView, basename="registro")




urlpatterns = [
    
    path('', include(router.urls)),
    path('Ingresos/',views.RegisterProductsView.as_view(),name= "Inreso Products"),
   

   
   
]