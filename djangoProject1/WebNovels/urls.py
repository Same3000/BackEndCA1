from django.urls import include, path


from . import views
app_name = 'WebNovels'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('form', views.create_webnovels, name='Form'),
    path('<id>', views.detail_view, name='detail'),
    path('<id>/update', views.update_view, name='update'),
    path('<id>/delete', views.delete_view, name='delete')
]