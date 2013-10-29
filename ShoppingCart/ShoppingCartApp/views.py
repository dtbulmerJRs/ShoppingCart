from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import *
from django.contrib.auth.models import *
from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from ShoppingCartApp.forms import *
from ShoppingCartApp.models import *
from django.template.context import RequestContext, Context
from django.views.generic.list import ListView


def index(request):
    return render(request, 'ShoppingCartApp/index.html')


def register_user(request):
    if request.method == 'POST':
        form = ShoppingCartUserForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = form.save()
            group = Group.objects.get(name=cleaned_data['user_type'])
            group.user_set.add(user)
            return HttpResponseRedirect('/ShoppingCartApp/register_success')
    args = {}
    args.update(csrf(request))
    args['form'] = ShoppingCartUserForm()
    return render_to_response('register.html', args)


def register_success(request):
    return render_to_response('register_success.html')


def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_page'))


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # CHECK IF Customer or Merchant to show different homes
                    return HttpResponseRedirect("/ShoppingCartApp/customer_home/")
            else:
                message = "Invalid username/password"
                form = LoginForm()
                return render(request, 'ShoppingCartApp/login.html',
                              {'message': message, 'form': form},
                              context_instance=RequestContext(request)
                )
    form = LoginForm()
    message = ""
    return render(request, 'ShoppingCartApp/login.html',
                  {'message': message, 'form': form},
                  context_instance=RequestContext(request)
    )


def customer_home(request):
    orders = Order.objects.filter(customer=request.user.id)
    cart = Cart.objects.get(customer=request.user.id)
    stores = Store.objects.all()
    return render(request, 'ShoppingCartApp/customer_home.html', {'orders': orders, 'cart': cart, 'stores': stores},)

"""
class CustomerListView(ListView):

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super(CustomerListView, self).get_context_data(**kwargs)
        return context
"""