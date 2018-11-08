from django.shortcuts import render, redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from guestbook.models import TourDates
import random
from guestbook.models import TextMessage


def index(request):
    """
    default_msg = "Images of BLACKBEAR's Albums <3"
    msgs = [default_msg for i in range(len(default_msg))]
    """
    if request.user.is_authenticated:
        name = request.user.username

    imgurl = ["https://images.genius.com/68159643d424fa1e7195d00dabe9acb9.800x800x1.jpg", "https://images.genius.com/76a524efee9d89c46be36e8cab34aff5.1000x1000x1.jpg", "https://images.genius.com/feb0ee138ad6f569e283aab9b18efdb7.600x600x1.jpg", "https://is2-ssl.mzstatic.com/image/thumb/Music18/v4/82/45/6e/82456e55-9a93-dd70-8585-0d431a88c377/IMG_1503.jpg/600x600bf.png", "https://t2.genius.com/unsafe/300x300/https%3A%2F%2Fimages.genius.com%2Fc2fb82133da8df2798d1b0ba33cffcea.600x600x1.jpg",  "https://i.scdn.co/image/caa8a134bb7757aa56dd965aac02554861b6768c", "https://pbs.twimg.com/media/DOTjQsRV4AAt1wP.jpg:large", "https://images.genius.com/1e70431143ad8a020a261085aa669c35.1000x1000x1.jpg",
              "https://ssle.ulximg.com/image/750x750/cover/1535040738_8364df8534edf14351da4b0c7e4ace71.jpg/83a06e977d5753d198c5ef5e653b2a9e/1535040738_88e5919f5910a919333d33e5de8ab9c2.jpg", "https://pic.pimg.tw/nono8962/1515395585-2811022308_n.jpg",  "https://images.genius.com/d2a7d2a3652692c6b45c96c6bf3de89e.500x500x1.jpg", "https://i.scdn.co/image/8f947969df6981a5ed54948c4aec8f2604811e3b", "https://lastfm-img2.akamaized.net/i/u/770x0/cf089e6d438b59017c8b89f7facf5d0a.jpg", "https://t2.genius.com/unsafe/620x600/https%3A%2F%2Fimages.genius.com%2F3fd361d2fff4a062f9b4804c99862bcd.500x484x1.png"]

    randomlist = []

    while len(randomlist) < 7:
        randomindex = random.randint(0, len(imgurl) - 1)
        if randomindex not in randomlist:
            randomlist.append(randomindex)

    for i in range(len(randomlist)):
        randomlist[i] = imgurl[randomlist[i]]

    return render(request, 'BLACKBEAR.html', locals())


def tour(request):

    D1 = TourDates.objects.create(city="Morrison, CO", venue="Red Rocks Amphitheatre", date="2018-10-19")
    D2 = TourDates.objects.create(city="Las Vegas, NV", venue="JEWEL Nightclub", date="2018-10-29")
    D3 = TourDates.objects.create(city="Cullowhee, NC", venue="Western Carolina University", date="2018-11-01")
    D4 = TourDates.objects.create(city="Las Vegas, NV", venue="JEWEL Nightclub", date="2018-11-16")
    D5 = TourDates.objects.create(city="Los Angeles, CA", venue="Hollywod Palladium", date="2018-11-28")
    D6 = TourDates.objects.create(city="Honolulu, HI", venue="The Republik", date="2018-12-06")
    D7 = TourDates.objects.create(city="Honolulu, HI", venue="The Republik", date="2018-12-07")

    tourdates = TourDates.objects.distinct().all()

    return render(request, 'TOUR.html', locals())


def feed(request):

    if request.method == 'POST':
        _talker = request.POST.get('name')
        if request.user.is_authenticated:
            _talker = request.user.username
        _message = request.POST.get('msg')
        TextMessage.objects.create(talker=_talker, message=_message)

    msgs = TextMessage.objects.all()

    if request.method == 'GET':
        #if request.user.is_authenticated:
            if request.GET.get('search') is not None:
                msg_search = request.GET.get('search')
                msgs = TextMessage.objects.filter(message__icontains=msg_search)

    return render(request, 'FEED.html', locals())

def about(request):
    return render(request, 'ABOUT.html', locals())

def activity(request):
    if request.user.is_authenticated:
        user = request.user
        msgs = TextMessage.objects.filter(talker__exact=user)

        if request.method == 'GET':
            if request.GET.get('search') is not None:
                msg_search = request.GET.get('search')
                msgs = TextMessage.objects.filter(message__icontains=msg_search)

        if request.method == 'POST':
            if request.GET.get('msg') is not None:
                _message = request.GET.get('original')
                _edited_msg = request.GET.get('edit')

                if _edited_msg != "":
                    TextMessage.objects.get(message=_message).update(message=_edited_msg)

                else:
                    current_msg = TextMessage.objects.get(message=_message)
                    current_msg.delete()
    return render(request, 'ACTIVITY.html', locals())