from django.shortcuts import render, redirect
from .admin import Watch

def watch_list(request):
    watchs = Watch.objects.all().order_by('-id')
    return render(request, 'watch_list.html', {'watchs':watchs})

def watch_detail(request, pk):
    watch = Watch.objects.get(id=pk)
    return render(request, 'watch_detail.html', {'watch':watch})

def create_watch(request):
    if request.method == 'POST':
        brand = request.POST['brand']
        desk = request.POST['desk']
        image = request.FILES.get('image')
        price = request.POST['price']

        Watch.objects.create(brand=brand, desk=desk, image=image, price=price)
        return redirect('watch')

    return render(request, 'create_watch.html')
