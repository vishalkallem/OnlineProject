from django.urls import path
from .views import *

app_name = 'OnlineApp'

# path('students/', StudentView.as_view(), name='all_students'),
# path('students/<int:student_id>/', backup_views.get_student_data, name='student'),
# path('students/scores/', backup_views.get_student_score, name='score'),
# path('test-session/', backup_views.get_session, name='session'),


urlpatterns = [
    path('login/', LoginController.as_view(), name='login'),
    path('signup/', SignUpController.as_view(), name='signup'),
    path('logout/', logout_user, name='logout'),
    path('colleges/', CollegeListView.as_view(), name='all_colleges'),
    path('colleges/<int:pk>/', CollegeDetailView.as_view(), name='college_details'),
    path('colleges/add/', CreateCollegeView.as_view(), name='add_college'),
    path('colleges/<str:acronym>/', CollegeDetailView.as_view(), name='college_details_acronym'),
    path('colleges/<int:college_id>/add/', CreateStudentView.as_view(), name='add_student'),
    path('colleges/<int:college_id>/edit/', UpdateCollegeView.as_view(), name='edit_college'),
    path('colleges/<int:college_id>/delete/', DeleteCollegeView.as_view(), name='delete_college'),
    path('colleges/<int:college_id>/<int:pk>/edit/', UpdateStudentView.as_view(), name='edit_student'),
    path('colleges/<int:college_id>/<int:pk>/delete/', DeleteStudentView.as_view(), name='delete_student'),
]
