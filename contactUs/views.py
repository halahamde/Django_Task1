from django.shortcuts import render
# Create your views here.
def contactUs(req):
    return render(req,'contact/contact.html')

def thank(req):
    context={}
    context['name']=req.GET['name']
    context['email']=req.GET['email']
    return render(req,'contact/thank.html',context)
