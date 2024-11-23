from django.shortcuts import render

posts = [
    {
        'id': 0,
        'location': 'Остров отчаянья',
        'date': '30 сентября 1659 года',
        'category': 'travel',
        'text': '''Наш корабль, застигнутый в открытом море
                  страшным штормом, потерпел крушение...
                  ''',
    },
    {
        'id': 1,
        'location': 'Остров отчаянья',
        'date': '1 октября 1659 года',
        'category': 'not-my-day',
        'text': '''Проснувшись поутру, я увидел, что наш корабль сняло
                  с мели приливом и пригнало гораздо ближе к берегу...
                  ''',
    },
]


def index(request):
    return render(request, 'index.html', {'posts': posts})


def post_detail(request, id):
    post = next(post for post in posts if post['id'] == id)
    return render(request, 'detail.html', {'post': post})


def category_posts(request, category_slug):
    return render(request, 'category.html', {'category_slug': category_slug})
