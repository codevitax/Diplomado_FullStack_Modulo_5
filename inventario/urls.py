from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"category", views.CategoriaViewSet)

urlpatterns = [
    path("contact/<str:name>", views.contact, name="contact"),
    path("categorias", views.categorias, name="categorias"),
    path("productos", views.productoFormView, name="productos"),
    # path("category", views.CategoriaCreateView.as_view()),
    # path("", views.index, name="index")
    path("categorias/contador", views.categoria_count, name="contador"),
    path("enviar/mensaje", views.enviar_mensaje, name="enviar"),
    path("productos/filtrar/unidades", views.productos_en_unidades),
    path("", include(router.urls)),
]