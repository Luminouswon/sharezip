from django.shortcuts import render, redirect
from .models import Room


# Create your views here.

def hosting1(request):
    return render(request,'hosting1.html')
   
def create1(request):
    room = Room()
    room.addr_gu = request.POST.get('addr_gu', False)
    room.addr_gu = request.POST.get('addr_dong', False)
    room.address = request.POST.get('address', False)
    room.rent_type = request.POST.get('rent_type', False)
    room.roommate_num = request.POST.get('roommate_num', False)
    room.building_type = request.POST.get('building_type', False)
    #room.room_num = request.POST.get('room_num', False)
    room.save()
    return render(request,'hosting2.html',{'current_room':room.id})
    #return redirect('/hosting2/')

def create2(request):
    room_id = request.POST.get('room_obj', False)    # 룸 객체 아이디
    room = Room.objects.get(id=room_id)
    room.image1 = request.POST.get('thumb1', False)
    room.image2 = request.POST.get('thumb2', False)
    room.image3 = request.POST.get('thumb3', False)
    room.detail = request.POST.get('details', False)
    room.cost = request.POST.get('cost', False)
    room.start_date = request.POST.get('start_date', False)
    room.end_date = request.POST.get('end_date', False)
    #room.room_num = request.POST.get('room_num', False)
    room.save()
    return redirect('/')

def checkbox(request): 
    filter = "" 
    option_items =["wifi", "air_conditioner", "tv", "doorlock"] 
    for i in option_items: 
        if i in request.GET:
            filter += i
            
    return render(request,{'filter':filter})

def hosting2(request):
    return render(request, 'hosting2.html')