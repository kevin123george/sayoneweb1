from django.shortcuts import render,redirect
from QandAboard.models import Post,Comment
from django.views.generic import UpdateView,DeleteView
from .forms import CommentForm,AskForm
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

@login_required
def QandA_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "QandA_index.html", context)
@login_required
def QandA_detail(request, pk):
    post = Post.objects.get(pk=pk)
    print(request.user.username)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        print ("valid")
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    aut=request.user.username
    context = {
        "post": post,
        "comments": comments,
        "form": form,
        
        
    }

    return render(request, "QandA_detail.html", context)

@login_required
def Ask_Form(request):
    aut=request.user.username
    if request.method == "POST":
        form = AskForm(request.POST,initial={'aut':aut})
        if form.is_valid():



            form.save()
            return redirect('QandA_index')
        

    else:
        form = AskForm(initial={'aut':aut})
    context = {
        'form':form
    }
    return render(request, 'Ask_form.html', context)




class post_update(UpdateView):

    model = Post
    form_class = AskForm
    template_name = 'Ask_form.html'
    success_url = '/QandA/'


class post_delete(DeleteView):
    model = Post
    template_name = 'board_element_confirm_delete.html'
    success_url = '/QandA/'
