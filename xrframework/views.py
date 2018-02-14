from django.http import HttpResponse
from django.shortcuts import render
from .models import Shape, Scene
# Create your views here.
def aframe(request, sceneid):
    try:
        scene = Scene.objects.get(pk=sceneid)
    except Scene.DoesNotExist:
        raise Http404("Scene does not exist")
    shapes = scene.shapes.all()
    context = {"shapes" : shapes}
    return render(request, 'xrframework/aframe.html', context)
