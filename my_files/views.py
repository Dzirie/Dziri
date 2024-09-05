from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from picture.models import Picture

@login_required
def index(request):
    pictures=Picture.objects.filter(created_by=request.user)
    return render(request,'my_files/index.html',{
'pictures':pictures
})
