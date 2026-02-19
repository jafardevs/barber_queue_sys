from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Customer


def register_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        if name and phone:
            Customer.objects.create(name=name, phone=phone)
            return redirect('queue_list')
    return render(request, 'queue_app/register.html')


def queue_list_view(request):
    customers = list(reversed(list(Customer.objects.order_by('-created_at')[:25])))
    return render(request, 'queue_app/list.html', {'customers': customers})


@login_required(login_url='barber_login')
def finish_customer_view(request, customer_id):
    if request.method == 'POST':
        customer = get_object_or_404(Customer, id=customer_id)
        customer.is_finished = True
        customer.save()
    return redirect('queue_list')
