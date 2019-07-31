
from django.contrib import admin
from django.urls import path
import penapp.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',penapp.views.home, name="home"),
    path('pen/<int:pen_id>',penapp.views.detail, name="detail"),
    path('pen/new/', penapp.views.new, name="new"),
    path('pen/create', penapp.views.create, name="create")

]
