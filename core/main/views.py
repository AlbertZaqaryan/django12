from asyncio.log import logger
from django.dispatch import receiver
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View, FormView, TemplateView
from .models import Category, Shoos, Firm, Cart
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from paypal.standard.forms import PayPalPaymentsForm
from django.urls import reverse
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

class HomeView(ListView):
    model = Shoos
    template_name = 'home.html'
    ordering = ['-id']
    def get(self, request):
        categ = Category.objects.all()
        return render(request, self.template_name, {'categ':categ})

class CategoryView(ListView):
    template_name = 'home_detail.html'
    def get(self, request, cats):
        categorys = Shoos.objects.filter(category=cats)
        return render(request, self.template_name,  {'cats':cats, 'categorys':categorys})

class CategoryDetail(DetailView):
	template_name = 'home_detail_detail.html'

	def get(self, request, id):
		ca = Firm.objects.get(pk=id)
		return render(request, self.template_name, {'ca':ca})

class PaypalFormView(FormView):
    template_name = 'paypal_form.html'
    form_class = PayPalPaymentsForm

    def get_initial(self):
	    return {
			"business": 'your-paypal-business-address@example.com',
            "amount": 20,
            "currency_code": "EUR",
            "item_name": "Example item",
            "inovice": 1234,
            "notify_url": self.request.build_absolute_uri(reverse('paypal-ipn')),
            "return_url": self.request.build_absolute_uri(reverse('paypal-return')),
            "cancel_return": self.request.build_absolute_uri(reverse('paypal-cancel')),
            "lc": 'EN',
            "no_shipping": '1',
		}


class PaypalReturnView(TemplateView):
    template_name = 'paypal_success.html'


class PaypalCancelView(TemplateView):
    template_name = 'paypal_cancel.html'


@receiver(valid_ipn_received)
def paypal_payment_received(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        if ipn_obj.receiver_email != 'your-paypal-business-address@example.com':
            return
        try:
            my_pk = ipn_obj.invoice
            mytransaction = Cart.objects.get(pk=my_pk)
            assert ipn_obj.mc_gross == mytransaction.amount and ipn_obj.mc_currency == 'EUR'
        except Exception:
            logger.exception('Paypal ipn_obj data not valid!')
        else:
            mytransaction.paid = True
            mytransaction.save()
    else:
        logger.debug('Paypal payment status not completed: %s' % ipn_obj.payment_status)

