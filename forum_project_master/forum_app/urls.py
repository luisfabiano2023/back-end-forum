from django.urls import path
from . import views as v

urlpatterns = [
	path('postar/', v.postar, name='postar')
  path('create/user/', v.cadastrar_se,name='cadastrar_se')
]
