from django.contrib import admin
from django.urls import include, path
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(("task.urls", "task"), namespace='task')),
    path('docs/', include_docs_urls(title='Tasky API', public=True)),
]
