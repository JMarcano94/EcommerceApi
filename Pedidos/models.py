from django.db import models
from User.models import Usuarios






class Pedidos(models.Model):

    STATUS_CHOICES = (
            (1,'Pendiente'),
            (2,'Asignado'),
            (5,'Enviado'),
            (6,'No Entregado'), 
            (7,'Entregado'), # Estado marcado por comprador para solicitar devolución de pago
            (8,'Completado'),
    )
    numero=models.AutoField(primary_key=True, editable=False,unique=True)
    fecha_creado=models.DateTimeField(auto_now_add=True,)
    mensajero=models.ForeignKey(Usuarios, on_delete=models.SET_NULL,null=True,)
    direccion_pedido= models.CharField(max_length=100,default='')
    estado_pedido=models.IntegerField(choices=STATUS_CHOICES,default=1)
    fecha_actualizado=models.DateTimeField(auto_now_add=True,)
    
    def __str__(self):
        return 'El pedido %s ha salido el dia %s, y la confirmacion de entrega es %s' %(self.numero,self.fecha,self.entregado)


class logs(models.Model):
    log=models.DateTimeField(auto_now_add=True)
    pedido_asociado=models.ForeignKey(Pedidos, on_delete=models.PROTECT)
    user_encargado=models.ForeignKey(Usuarios, on_delete=models.PROTECT)
    comentario=models.CharField(max_length=200, blank=True, default='')

    def __str__(self):
        return (self.log, self.user_encargado, self.pedido_asociado)