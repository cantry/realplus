from django.http import HttpResponse
from django.shortcuts import render
from .models import Shapes, Scene
# Create your views here.
def aframe(request, sceneid):
    try:
        scene = Scene.objects.get(pk=sceneid)
    except Scene.DoesNotExist:
        raise Http404("Scene does not exist")
    s = [int(s) for s in (scene.shapes.split(','))]
    shapes = []
    for i in s:
        shape = Shapes.objects.get(pk=i)
        s1 = dict({"name" : shape.name, "attributes" : shape.attributes})
        shapes.append(s1)
    context = {"shapes" : shapes}
    return render(request, 'xrframework/aframe.html', context)
