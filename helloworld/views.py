from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
import random

def index(request):
	default_msg = "Images of BLACKBEAR <3"
	msgs = [default_msg for i in range(len(default_msg))]
	imgurl = ["https://images.genius.com/68159643d424fa1e7195d00dabe9acb9.800x800x1.jpg", "https://images.genius.com/" \
              "76a524efee9d89c46be36e8cab34aff5.1000x1000x1.jpg", "https://images.genius.com/feb0ee138ad6f569e283aab9" \
              "b18efdb7.600x600x1.jpg", "https://is2-ssl.mzstatic.com/image/thumb/Music18/v4/82/45/6e/82456e55-9a93-d" \
              "d70-8585-0d431a88c377/IMG_1503.jpg/600x600bf.png", "https://t2.genius.com/unsafe/300x300/https%3A%2F%2" \
              "Fimages.genius.com%2Fc2fb82133da8df2798d1b0ba33cffcea.600x600x1.jpg", "https://i.scdn.co/image/caa8a13" \
              "4bb7757aa56dd965aac02554861b6768c", "https://pbs.twimg.com/media/DOTjQsRV4AAt1wP.jpg:large"]
	return render(request, 'BLACKBEAR.html', locals())