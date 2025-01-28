from django.shortcuts import redirect, render
from .models import Blog, BlogCommment,Contact
from .forms import ContactForm,CreateBlogForm,UpdateBlogForm,CommmentBlogForm
from django.contrib import messages
from django.views  import generic
from django.contrib.messages.views import  SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin



class blog_home(generic.ListView):
    model=Blog
    paginate_by=10
    template_name="main/blog_home.html" 



def blog_detail(request,slug):
    blog=Blog.objects.get(slug=slug)
    all_comments=BlogCommment.objects.filter(blog=blog.id)
    all_blogs=Blog.objects.all().order_by('-post_date')[:10]
    


    form=CommmentBlogForm()
    if request.method=="POST":
        form=CommmentBlogForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your comment on this blog has been posted")
            return redirect("/blog_detail/"+blog.slug)
    else:
          form=CommmentBlogForm()

    context={
       'blog':blog,
       'all_blogs':all_blogs,
       'form':form,
       'all_comments':all_comments
    }
    return render(request,"main/blog_detail.html",context)


class contactUs(SuccessMessageMixin,generic.CreateView):
    form_class=ContactForm
    template_name="main/contact_us.html"
    success_url="/"
    success_message="your query has been  submited sucessgully,we will contact you soon"


class CreateBlog(LoginRequiredMixin,SuccessMessageMixin,generic.CreateView):
    form_class=CreateBlogForm
    template_name="main/create_blog.html"
    login_url='login'
    success_url="/"
    success_message="Your blog has been created"

class UpdateBlogView(LoginRequiredMixin,SuccessMessageMixin,generic.UpdateView):
    form_class=UpdateBlogForm
    model=Blog
    template_name="main/update_blog.html"
    login_url='login'
    success_url="/"
    success_message="Your blog has been updated"

class DeleteBlogView(LoginRequiredMixin,SuccessMessageMixin,generic.DeleteView):
    model=Blog
    template_name="main/delete_blog.html"
    login_url='login'
    success_url="/"
    success_message="Your blog has been deleted"
