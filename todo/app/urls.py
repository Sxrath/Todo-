from django.urls import path
from .views import Add_Task, CustomLoginView, Delate_task, Logout, RegisterPage, Tasklist, Update_task


urlpatterns=[
    path('tasks/',Tasklist.as_view(), name='tasks'),
    path('add/',Add_Task.as_view(),name= 'add'),
    path('edit/<int:pk>/',Update_task.as_view(),name='edit'),
    path('delete/<int:pk>',Delate_task.as_view(),name='delete'),
    path('', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('logout/',Logout.as_view(), name='logout')
]