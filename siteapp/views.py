from django.shortcuts import render
from django.template import loader
from .models import contactResponse, Album, Video, Photo, photoAlbum
from django.core.mail import send_mail

# Create your views here.
def index(request):
    lastpage = request.META.get('HTTP_REFERER')
    context = {'up': False}

    if lastpage:
        print(lastpage)
        if len(str(lastpage).split('//')[1].split('/')[1]) > 0:
            context = {'up': True}

    return render(request, 'siteapp/home.html', context)


def load_page(request):
    lastpage = request.META.get('HTTP_REFERER')
    insert = 'siteapp/{}.html'.format(request.path.strip('/'))
    context = {'down': False}

    if lastpage:
        lastpage = str(lastpage).split('//')[1].split('/')[1]
        if len(lastpage) == 0:
            context = {'down': True}
    print(insert)

    return render(request, insert, context)


def media(request):
    lastpage = request.META.get('HTTP_REFERER')
    context = {'down': False}

    if lastpage:
        lastpage = str(lastpage).split('//')[1].split('/')[1]
        if len(lastpage) == 0:
            context = {'down': True}

    context['media'] = "video"
    context['video'] = Video.objects.get(id=1)
    numobj = int(Video.objects.count())
    if numobj > 0:
        context['next'] = 2
    else:
        context['next'] = 0
    if numobj > 1:
        context['prev'] = numobj
    else:
        context['next'] = 0

    return render(request, 'siteapp/view.html', context)


def video(request, idnum):
    context = {'media': 'video'}
    idint = int(idnum)
    if Video.objects.count() > 0:
        if Video.objects.count() > 1:
            if idint == Video.objects.count():
                context['prev'] = Video.objects.count() - 1
                context['next'] = 1
            elif idint == 1:
                context['prev'] = Video.objects.count()
                context['next'] = 2
            else:
                context['prev'] = idint - 1
                context['next'] = idint + 1
        else:
            context['prev'] = None
            context['next'] = None
        context['video'] = Video.objects.get(id=idint)
    else:
        context['not_found'] = True

    return render(request, 'siteapp/view.html', context)


def photo(request, idnum):
    context = {'media': 'photo'}
    idint = int(idnum)
    if Photo.objects.count() > 0:
        if idint == Photo.objects.count():
            context['prev'] = Photo.objects.count() - 1
            context['next'] = 1
        elif idint == 1:
            context['prev'] = Photo.objects.count()
            context['next'] = 2
        else:
            context['prev'] = idint - 1
            context['next'] = idint + 1
        context['photo'] = Photo.objects.get(id=idint)
    else:
        context['not_found'] = True

    return render(request, 'siteapp/view.html', context)


def music(request):
    lastpage = request.META.get('HTTP_REFERER')
    context = {'down': False,
               'curr_album': Album.objects.all()[0],
               'albums': Album.objects.all()}

    if lastpage:
        lastpage = str(lastpage).split('//')[1].split('/')[1]
        if len(lastpage) == 0:
            context['down'] = True

    return render(request, 'siteapp/music.html', context)


def new_album(request, album_title):
    context = {}
    context['curr_album'] = Album.objects.get(title=album_title)
    context['albums'] = Album.objects.all()

    return render(request, 'siteapp/music.html', context)


def thanks(request):
    data = request.POST

    context = {
        'form_name': data.get('form_name'),
        'form_email': data.get('form_email'),
        'form_color': data.get('form_color'),
        'form_hero': data.get('form_hero'),
        'form_simpsons': data.get('form_simpsons'),
        'form_book': data.get('form_book'),
        'form_message': data.get('form_message')
    }

    email_body = "Hello there {name}!\nyou wanted your responses:\n\n".format(name=data.get('form_name'))
    for key in data:
        if "form" in str(key) and "email" not in str(key) and "name" not in str(key):
            email_body += "~~~\n{key}: {value}\n".format(key=str(key).split("_")[1], value=str(data.get(key)))
    email_body += "~~~~~~~~~~\n\nxoxo,\nJane (Stay In School) (band) (you saw)\nwww.juststayinschool.com | stayinschool.bandcamp.com"

    if data.get('email_response'):
        send_mail('your form responses from juststayinschool.com', email_body, 'noreply@juststayinschool.com', [str(data.get('form_email'))])

    send_mail('someone hit you up from juststayinschool.com!', "Here's a nice JSON: {}".format(context), 'noreply@juststayinschool.com', ['jane@juststayinschool.com'])

    contactResponse.objects.create(name=data.get('form_name'), email=data.get('form_email'), favorite_color=data.get('form_color'),
                              hero=data.get('form_hero'), simpsons=data.get('form_simpsons'), book=data.get('form_book'),
                              message=data.get('form_message'))

    return render(request, 'siteapp/thanks.html', context)