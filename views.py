from django.shortcuts import render
from django.utils import timezone
from .models import Post, Comment
from django.http import HttpResponse
import json
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from .forms import CommentForm

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	print(posts)
	comments = Comment.objects.all()
	commentForm = CommentForm()
	return render(request, 'blog/post_list.html', {'posts': posts, 'comments':comments, 'commentform': commentForm })


def new_post(request):
	title = request.POST.get('title')
	text = request.POST.get('text')
	author = request.POST.get('author')
	new_post = Post(title=title,author = author,text = text,created_date = timezone.now(), published_date=timezone.now())
	new_post.save()
	post = {"title": title,"text": text,"author": author,"published_date": timezone.now()}
	html = render_to_string('blog/post.html', {'post': post})
	return HttpResponse(html)

def new_comment(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	dompost = request.POST.get("post")
	print(dompost)
	realpost = Post.objects.get(pk = dompost)
	print(realpost)
	commentForm = CommentForm(request.POST)
	if commentForm.is_valid():
			comment = commentForm.save(commit=False)
			comment.post =  realpost
			comment.save()
			comments = Comment.objects.all()
			commentForm = CommentForm()
			return render(request, 'blog/post_list.html', {'posts': posts, 'comments':comments, 'commentform': commentForm })

	else:
		commentForm = CommentForm()
		return HttpResponse("not valid")

	
# def new_comment(request):
	
# 	return redirect('post_list')