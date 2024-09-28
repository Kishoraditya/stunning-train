import razorpay
from django.conf import settings
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import SubscriptionPlan

def checkout(request):
    plans = SubscriptionPlan.objects.all()
    return render(request, 'checkout.html', {'plans': plans})

def create_order(request):
    if request.method == 'POST':
        plan_id = request.POST.get('plan_id')
        plan = SubscriptionPlan.objects.get(id=plan_id)
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        order_amount = int(plan.price * 100)
        order_currency = 'INR'
        order_receipt = f'order_rcptid_{request.user.id}'
        order = client.order.create({
            'amount': order_amount,
            'currency': order_currency,
            'receipt': order_receipt,
            'payment_capture': '1'
        })
        return render(request, 'payment.html', {
            'order': order,
            'plan': plan,
            'key_id': settings.RAZORPAY_KEY_ID
        })


from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import UserSubscription, FeatureFlag
from django.utils import timezone

@login_required
def premium_feature(request):
    # Check if the feature is enabled
    feature = FeatureFlag.objects.get(name='Premium Feature')
    if not feature.enabled:
        return render(request, 'feature_disabled.html')

    # Check if user has an active subscription
    try:
        subscription = UserSubscription.objects.get(user=request.user, active=True)
        if subscription.end_date < timezone.now():
            subscription.active = False
            subscription.save()
            return redirect('renew_subscription')
    except UserSubscription.DoesNotExist:
        return redirect('subscribe')

    return render(request, 'premium_feature.html')

