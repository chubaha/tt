from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from empoyees import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.employees, name='employees'),
    path('all-list/', views.all_employees, name='all-list'),
    path('all-list-ajax/', views.all_employees_ajax, name='all-list-ajax'),
    path('search/', views.search_list, name='search-list'),
    path('search-ajax/', views.search_ajax, name='search-list-ajax'),
    path('search-ajax-edit/', views.search_ajax_edit, name='search-list-ajax'),
    path('sorter-ajax/', views.sorter_ajax, name='sorter-list-ajax'),
    path('privat-page/', views.privat_page, name='privat-page'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('create/', views.create, name='create'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)