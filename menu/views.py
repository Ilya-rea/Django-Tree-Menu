from django.shortcuts import render

def test_view(request, slug=None):
    return render(request, 'test.html', {'slug': slug})
