from django.shortcuts import render, HttpResponse



def triangle(request):
    cat1 = request.GET.get('cat1')
    cat2 = request.GET.get('cat2')
    return render(request, 'math/triangle.html', {cat1: 'cat1', cat2: 'cat2'})

