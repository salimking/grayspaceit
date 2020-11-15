from django.urls import path
from posts.views import posts, post_details
app_name="auth"
urlpatterns = [
    path('', posts),
    path('<int:post_id>', post_details)
]
