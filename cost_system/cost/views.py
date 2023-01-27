from django.shortcuts import render, get_object_or_404
from .models import Order, Requisition, WorkTicket

def order(request):
    list_orders = Order.objects.all()
    return render(request, 'order.html', {
        'list_orders': list_orders
    })

def order_detail(request, id):
    order = get_object_or_404(Order, pk=id)
    requisitions = order.requisition_set.all()
    requisition_cost = 0
    for requisition in requisitions:
        requisition_cost += requisition.total_cost()
    labor = 0
    workTickets = order.workticket_set.all()
    for workticket in workTickets:
        labor += workticket.labor_pay()    
    return render(request, 'detail.html', {
        'order': order,
        'requisition_cost': requisition_cost,
        'labor': labor,
        'worktickets': workTickets
    })

def home(request):
    return render(request, 'home.html')