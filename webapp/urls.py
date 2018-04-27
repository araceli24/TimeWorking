from django.conf import settings
from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin


urlpatterns = [
       
    path('admin/',admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('core.urls')),
    path('api/',include('api.urls')),

]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [ 
        path('__debug__/', include(debug_toolbar.urls)),
    ]
