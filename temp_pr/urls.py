from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Online Market"
admin.site.index_title = "Hush kelibsiz !..."

urlpatterns = ([
                   path('admin/', admin.site.urls),
                    path('blogs/', include('blogs.urls', namespace='blogs')),
                    path('products/', include('products.urls', namespace='products')),
                    path('users/', include('users.urls', namespace='users')),
                   path('', include('pages.urls', namespace='pages')),
               ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                            document_root=settings.
                                                                                            MEDIA_ROOT))
