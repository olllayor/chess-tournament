from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tournaments.views import PlayerViewSet, TournamentViewSet, MatchViewSet, LeaderboardViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register(r'players', PlayerViewSet)
router.register(r'tournaments', TournamentViewSet)
router.register(r'matches', MatchViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Chess Tournament API",
      default_version='v1',
      description="API documentation for the Chess Tournament Management system",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@chess.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
