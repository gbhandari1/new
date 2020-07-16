from django.urls import path
from ressys import views

app_name = 'ressys'

urlpatterns = [
    path('',views.HomeView, name = 'home'),
    path('create_applicant/', views.createApplicantView, name = 'capp'),
    path('applicant_detail/<int:pk>/', views.applicantDetailView, name = 'applicant_detail'),
    path('update_applicant/<int:pk>', views.applicantUpdateView, name = 'update_applicant'),
    path('delete_applicant/<int:pk>', views.applicantDeleteView, name = 'delete_applicant'),
    path('register/', views.registerView, name = 'register'),
    path('login/', views.loginView, name = 'login_user'),
    path('logout/', views.logoutView, name = 'logout_user'),
    path('user/', views.userView, name='user_page')

]
