from .views import AllUser, AddUser, ChangeUser, DeleteUser

from django.urls import path

app_name = 'users'

urlpatterns = [
    path('index', AllUser.as_view(), name="index"),
    path('add', AddUser.as_view(), name='add'),
    path('change/<int:user_id>', ChangeUser.as_view(), name='change'),
    path('delete/<int:user_id>', DeleteUser.as_view(), name='delete')
]
