from django.shortcuts import render

posts = [
    {
        'author': 'author1',
        'title': 'title1',
        'content': 'content1',
        'date_posted': 'date_posted1'
    },
    {
        'author': 'author2',
        'title': 'title2',
        'content': 'content2',
        'date_posted': 'date_posted2'
    },
]


def home(request):
    context = {'posts': posts}
    return render(request, 'blog/home.html', context=context)


def about(request):
    return render(request, 'blog/about.html', context={'title': 'About'})
