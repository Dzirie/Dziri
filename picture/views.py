
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404,redirect
from .models import Picture,Category
from .forms import NewPictureForm,EditPictureForm
# Create your views here.

def browse(request):
    categories=Category.objects.all()
    category_id=request.GET.get('category',0)
    query=request.GET.get('query','')
    pictures=Picture.objects.all()
    if category_id:
        pictures=pictures.filter(category_id=category_id)
    if query:
        pictures=pictures.filter(Q(name__icontains=query)|Q(description__icontains=query))
    return render(request,'picture/browse.html',{
'pictures':pictures,
'categories':categories,
'query':query,
'category_id':int(category_id),
})


def photos_view(request):
    pictures=Picture.objects.all()
    categories=Category.objects.all()
    return render(request,'picture/photos.html',{
'pictures':pictures,
'categories':categories,
})

def detail(request, pk):
    picture=get_object_or_404(Picture,pk=pk)
    related_pictures = Picture.objects.filter(category=picture.category,).exclude(pk=pk)[0:10]
    return render(request,'picture/detail.html',{
 'picture' : picture ,
 'related_pictures' : related_pictures,
})

@login_required
def new(request):
    if request.method == 'POST':
        form=NewPictureForm(request.POST, request.FILES)
        if form.is_valid():
            picture = form.save(commit=False)
            picture.created_by = request.user
            picture.save()
            return redirect('picture:detail',pk = picture.id)
    else:
        form = NewPictureForm()
    return render(request,'picture/form.html',{ 'form' : form })

@login_required
def delete(request,pk):
    picture=get_object_or_404(Picture,pk=pk,created_by=request.user)
    picture.delete()
    return redirect('my_files:index')





@login_required
def edit(request,pk):
    picture=get_object_or_404(Picture,pk=pk,created_by=request.user)
    if request.method=='POST':
        form=EditPictureForm(request.POST,request.FILES,instance=picture)
        if form.is_valid():
            picture.save()
            return redirect('picture:detail',pk=picture.id)
    else:
        form = EditPictureForm(instance=picture)
    return render(request,'picture/form.html',{'form':form})
