from django.conf import settings
from django.shortcuts import render, redirect
from django.template import loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from office.models import Engineer, Team, Product, Advice

# Create your views here.

def my_render(request, template_path, context={}):
    temp = loader.get_template(template_path)
    context = RequestContext(request, context)
    res_html = temp.render(context)
    return HttpResponse(res_html)

def index(request):
    return render(request, 'office/index.html')

def engineers(request):
    engrs_num = Engineer.objects.all().count
    engrs = Engineer.objects.all() 
    return render(request, 'office/engineers.html', 
        context={'engrs_num': engrs_num, 'engrs': engrs})

def teams(request):
    teams = Team.objects.all()
    return render(request, 'office/teams.html', context={'teams': teams})

def products(request):
    products = Product.objects.all()
    return render(request, 'office/products.html', context={'products': products})

def techtalk(request):
    return render(request, 'office/techtalk.html')
    
def resource(request):
    return render(request, 'office/resource.html')

def advice(request):
    return render(request, 'office/advice.html')

def add(request):
    advice = request.POST['advice']
    new_advice = Advice.objects.create(name=advice)
    return HttpResponseRedirect('../')

from django.views import generic

class EngineerListView(generic.ListView):
    model = Engineer
    #context_object_name = 'engr_list'
    queryset = Engineer.objects.filter()
    #template_name = 'office/engineer_list.html'

class EngineerDetailView(generic.DetailView):
    model = Engineer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TeamListView(generic.ListView):
    model = Team

class TeamDetailView(generic.DetailView):
    model = Team

class ProductListView(generic.ListView):
    model = Product

class ProductDetailView(generic.DetailView):
    model = Product

#from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#Engineer
class EngineerCreate(CreateView):
    model = Engineer
    fields = '__all__'
    template_name = 'office/engineer_form.html'

class EngineerUpdate(UpdateView):
    model = Engineer
    fields = '__all__'
    template_name = 'office/engineer_form.html'

class EngineerDelete(DeleteView):
    model = Engineer
    template_name = 'office/engineer_confirm_delete.html'
    success_url = reverse_lazy('engineers')

#Team
class TeamCreate(CreateView):
    model = Team
    fields = '__all__'
    template_name = 'office/team_form.html'

class TeamUpdate(UpdateView):
    model = Team
    fields = '__all__'
    template_name = 'office/team_form.html'

class TeamDelete(DeleteView):
    model = Team
    template_name = 'office/team_confirm_delete.html'
    success_url = reverse_lazy('teams')

#Product
class ProductCreate(CreateView):
    model = Product
    fields = '__all__'
    template_name = 'office/product_form.html'

class ProductUpdate(UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'office/product_form.html'

class ProductDelete(DeleteView):
    model = Product
    template_name = 'office/product_confirm_delete.html'
    success_url = reverse_lazy('teams')