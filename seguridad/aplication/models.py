from django.db import models

class usuario(models.Model):
    nombre_usuario = models.CharField(max_length=200)
    cedula = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre_usuario


class alerta(models.Model):
    fecha_reporte = models.DateField(blank=True, null=True)
    usuario = models.ForeignKey(usuario, on_delete = models.CASCADE) 
    coordenadas_alerta = models.CharField(max_length=200)   
    descripcion_alerta = models.CharField(max_length=200)
    def __str__(self):
        return str(self.fecha_reporte)#convertir entero a string (str)

class cai(models.Model):
    nombre_cai = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    coordenadas_cai = models.CharField(max_length=200)
    descripcion_cai = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre_cai