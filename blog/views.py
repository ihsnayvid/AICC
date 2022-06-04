from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,comment
from django.template import RequestContext
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.db.models import Q
from .forms import CommentForm,textForm
from django.contrib import messages
#from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.models import User
def home(request):
		
	context={
	'posts':Post.objects.all(),	
	}
	
	return render(request,'blog/blog.html',context)

class PostListView(ListView):#class based view
	model=Post
	template_name='blog/blog.html'
	context_object_name='posts'
	ordering=['-Date']
	paginate_by =2 # max no. of posts on a web page
	 #naming convention for template name is <app>/<model>_<viewtype>.html
	

class UserListView(ListView):#class based view
	model=Post
	template_name='blog/user_post.html'
	context_object_name='posts'
	ordering=['-Date']
	paginate_by =2

	def get_queryset(self):
		user=get_object_or_404(User,username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-Date')

def add_comment(request):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        #comment.Post=request.Post
        comment.User_Id = request.user
        comment.save()
        return redirect('/')
    return render(request,'blog/comment.html', { 'form': form})
                          

class PostDetailView(DetailView):#class based view
	model=Post
	
class PostCreateView(LoginRequiredMixin,CreateView):#class based view
	model=Post
	fields=['title','content','image']

	def form_valid(self,form):
		form.instance.author=self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model=Post
	fields=['title','content','image']

	def form_valid(self,form):
		form.instance.author=self.request.user
		return super().form_valid(form)

	def test_func(self):
		post=self.get_object()	#returns the post we are trying to update
		if self.request.user==post.author: # checks if the logged in user is the autohr of the post trying to update
			return True
		return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):#class based view
	model=Post
	success_url='/'
	def test_func(self):
		post=self.get_object()	#returns the post we are trying to update
		if self.request.user==post.author: # checks if the logged in user is the autohr of the post trying to update
			return True
		return False


def about(request):
	return render(request,'blog/about.html')

def searchblog(request):
	if request.method=='POST':
		srch=request.POST['textbox']
		if srch:
			match=Post.objects.filter(Q(title__icontains=srch))

			if match:
				return render(request,'blog/search.html',{'sr':match})
			else:
				messages.error(request,"no result found")
		else:
			return HttpResponseRedirect('/search/')
	return render(request,'blog/search.html')


