from django.urls import path, include
from rest_framework.routers import SimpleRouter
from Pedidos import views 


app_name = 'Pedidos'

router = SimpleRouter()
#router.register(r'register', views.RegisterView, basename="registro")




urlpatterns = [
    
    path('', include(router.urls)),
    path('crear/',views.CreateOrdersViews.as_view(),name= "Inreso Pedidos"),
    path('',views.ListPedidosView.as_view(),name= "Listar Pedido"),
    path('actualizar/(?<pk>/d+)/',views.UpdateOrderView.as_view(),name= "Editar Pedidos"),
   
]