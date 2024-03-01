from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from api.api_dashboard.viewsets import DashboardViewSet
from api.api_produtor_rural.viewsets import ProdutorRuralViewSet


schema_view = get_schema_view(
   openapi.Info(
      title="Brain Agriculture API",
      default_version='v1',
      description="Teste do Processo Seletivo vaga de Dev Python Senior",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


router = routers.DefaultRouter()
router.register('produtores-rurais', ProdutorRuralViewSet, basename='produtor_rural')
router.register('dashboard', DashboardViewSet, basename='fazendas_totais')

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/v1/', include(router.urls)),

   re_path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
