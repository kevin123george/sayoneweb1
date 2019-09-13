from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from board.models import Board_element
from django.views.generic import UpdateView,DeleteView
from .forms import Board_elementForm
from django.contrib.auth.decorators import login_required


@login_required
def board_index(request):
    projects = Board_element.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'board_index.html', context)

@login_required
def board_detail(request, pk):
    project = Board_element.objects.get(pk=pk)

    is_liked = False
    if project.likes.filter(id=request.user.id).exists():
        is_liked = True
    context = {
        'project': project,
        'total_likes':project.likes.count(),
        'is_liked' : is_liked,
    }
    return render(request, 'board_detail.html', context)



@login_required
def board_Form(request):
    if request.method == "POST":
        form = Board_elementForm(request.POST)
        if form.is_valid():
            print("valid")
            form.save()
            return redirect('board_index')

    else:
        form = Board_elementForm(request.POST)
    context = {
        'form':form
    }
    return render(request, 'board_form.html', context)
    


@login_required
def like_post(request):
    post = get_object_or_404(Board_element,id=request.POST.get('board_element_id'))
    is_liked = False
    
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else :
        post.likes.add(request.user)
        is_liked = True
    return redirect('board_index')




"""def post_update(request,pk):
    instance = get_object_or_404(Board_element,id=request.POST.get('board_element_id'))
    print("dfgdfgd")
    form = Board_elementForm(request.POST or None,instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {
        'project': project,
        'total_likes':project.likes.count(),
        'is_liked' : is_liked,
        'form' : form
    }
    print("dfgdfgd")
    return render(request, 'board_form.html', context)
"""

class post_update(UpdateView):

    model = Board_element
    form_class = Board_elementForm
    template_name = 'board_form.html'
    success_url = '/board/'


class post_delete(DeleteView):
    model = Board_element
    template_name = 'board_element_confirm_delete.html'
    success_url = '/board/'
