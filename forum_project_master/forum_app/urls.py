from django.urls import path
from . import views as v

urlpatterns = [
	path('postar/', v.postar, name='postar')
  path('sign_up/', v.cadastrar_se,name='cadastrar_se')
]
