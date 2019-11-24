from django.db import models

# Create your models here.
class Project(models.Model): #hereda la clase models para usar el ORM de django
    title = models.CharField(max_length=200, verbose_name = "Título")
    description = models.TextField(verbose_name = "Descripción")
    image = models.ImageField(verbose_name = "Imágen", upload_to = "projects")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True, verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        #por defecto Django ordena del mas viejo al mas nuevo. nosotros debemos cambiar eso:
        ordering = ["-created"]
    
    def __str__(self):
        return self.title