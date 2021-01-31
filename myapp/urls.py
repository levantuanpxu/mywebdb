from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
from.views import HomeDetailView, ListDetailView

urlpatterns = [
    # path("detail", views.post, name="detail"),
    path("", views.home, name="home"),
    path('detail/<int:pk>', HomeDetailView.as_view(), name="detail"),
    path('detaillist/<int:pk>', ListDetailView.as_view(), name="detaillist"),
    path('list', views.list, name="list"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
