
from django.urls import path
from blog import views


urlpatterns = [
    
    path('' ,views.blog_home.as_view(),name="blog_home"),
    path('blog_detail/<str:slug>',views.blog_detail,name="blog_detail"),
    path('create_new_post/',views.CreateBlog.as_view(),name="create-blog"),
    path('contact-us/',views.contactUs.as_view(),name="contact_us"),
    path('update_blog/<int:pk>/',views.UpdateBlogView.as_view(),name="UpdateBlogView"),
    path('delete_blog/<int:pk>/',views.DeleteBlogView.as_view(),name="DeleteBlogView"),
]
