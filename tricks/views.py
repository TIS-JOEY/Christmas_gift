from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse

import zipfile
import os

# Create your views here.

def main(request):
	try:
		if request.POST['email']=='032687':
			return render(request,'challenge1.html',{'pass':'yes',})
		else:
			return render(request,'index.html',{'pass':'錯誤',})
	except:
		return render(request,'index.html',{'pass':'開啟時光隧道的大門'})

def normal_challenge(request):

	try:
		if request.POST['email']=='43333645633233622337332166':
			return render(request,'challenge3.html',{'pass':'yes',})
		else:
			return render(request,'challenge2.html',{'pass':'no',})
	except:
		return render(request,'challenge2.html',{'pass':''})

def last_challenge(request):
	return render(request,'challenge4.html')

