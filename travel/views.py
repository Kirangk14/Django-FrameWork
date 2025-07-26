from django.shortcuts import render
from .models import Destination


# Create your views here.
def index(request):
    '''dest1=Destination()  
    dest2=Destination()
    dest3=Destination()

    dest1.name='Mumbai' 
    dest1.price=700
    dest1.desc='City that wont sleep'
    dest1.img='destination_4.jpg'
    dest1.offer=False

    dest2.name='Bangalore'
    dest2.price=1000
    dest2.desc='IT Hub of India'
    dest2.img='destination_5.jpg'
    dest2.offer=True

    dest3.name='Delhi'
    dest3.price=500
    dest3.desc='Polluted City'
    dest3.img='destination_6.jpg'
    dest3.offer=False'''

    dests=Destination.objects.all()
    
    return render(request,'index.html',{'dests':dests})