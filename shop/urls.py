from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, reverse_lazy
from django.views.generic.edit import CreateView

from users.forms import UserRegistrationForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path(
        'auth/registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=UserRegistrationForm,
            success_url=reverse_lazy('catalog:index'),
        ),
        name='registration',
    ),
    path('users/', include('users.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
