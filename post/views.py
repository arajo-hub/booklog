from django.shortcuts import render

def save(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        publisher=request.POST.get('publisher')
        pubdate=request.POST.get('pubdate')
        review=request.POST.get('review')
        context = {
            'title' : title,
            'author' : author,
            'publisher' : publisher,
            'pubdate' : pubdate,
            'review' : review,
        }
        print(context)
        return render(request, 'home.html', context=context)
