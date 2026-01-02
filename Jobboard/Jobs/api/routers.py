from rest_framework.routers import DefaultRouter
from jobs.views import JobViewSet
from users.views import UserViewSet  # Assuming users app has one

router = DefaultRouter()
router.register(r'jobs', JobViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [path('api/', include(router.urls))]
