from django.urls import path
from authors import views

urlpatterns = [
    
    path('create-new-account/' ,views.signUp,name="register"),
    path('user-profile/<str:user_name>/' ,views.profile,name="profile"),
    path('login/' ,views.logIn,name="login"),
    path('logout/' ,views.logOut,name="logout"),
    path('change_password',views.PasswordChangeView.as_view(template_name="authors/password_change.html"),name="change_password"),
    path('password_success',views.password_success,name="password_success"),
    path(('edit_profile/'),views.UpdateUserView.as_view(),name="edit_user"),
    path('delete_user/<int:pk>/',views.DeleteUser.as_view(),name="delete_user"),   
    path('update_public_details/',views.UpdatePublicDetails.as_view(),name="user_public_details"),
    path('dashboard/',views.Dashboard.as_view(),name="dashboard")
]
