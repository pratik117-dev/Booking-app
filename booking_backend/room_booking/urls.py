from django.urls import path
from room_booking import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.api_root, name='api-root'),

    # ✅ Rooms
    path('rooms/', views.RoomList.as_view(), name='room-list'),
    path('rooms/<int:pk>/', views.RoomDetail.as_view(), name='room-detail'),

    # ✅ OccupyData (Booking endpoints, renamed to match serializer)
    path('occupydata/', views.OccupyDatesList.as_view(), name='occupydata-list'),
    path('occupydata/<int:pk>/', views.OccupyDatesDetail.as_view(), name='occupydata-detail'),

    # ✅ Users (Fixed name to 'user-detail')
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),

    # ✅ Auth
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
