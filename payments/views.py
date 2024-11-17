from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from payments.models import Payment
from orders.models import Order
from django.http import JsonResponse
from cart.models import Cart


# Create your views here.

def verify_payment(request, ref):
    try:
        cart = Cart(request)
        payment = Payment.objects.get(ref=ref)
        verified = payment.verify_payment()
        
        if verified:
            last_order = Order.objects.latest('placed_at')
            
            if last_order:
                order = get_object_or_404(Order, pk=last_order.id)
                order.paid = True
                order.save()
                
                
                order_info = {
                    'id': order.id,
                    'total_amount': order.total_amount(),
                    'placed_at': order.placed_at
                }
                
                context = {
                    'order_info': order_info,
                    'cart': cart,
                    'payment': payment
                }
                
                cart.clear()
                return render(request, 'Thank you', context)
            
            else:
                messages.error(request, 'No order id found.')
                # return redirect('cart:view')
                return JsonResponse({'Error_message': 'Order id not found'})
            
        else:
            messages.error(request, 'Payment verification failed.')
            return redirect('cart:view')
            # return JsonResponse({'Error_message': 'Payment verification failed'})
            
    except Payment.DoesNotExist:
        messages.error(request, 'Payment not found.')
        # return redirect('cart:view')
        return JsonResponse({'Error_message': 'Payment not found'})
            
