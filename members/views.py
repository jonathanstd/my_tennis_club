from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader
from .models import Court, Member

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
  
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))

def court_list(request):
    courts = Court.objects.all()  # Fetch all court instances
    template = loader.get_template('court_list.html')  # Your new template
    context = {
        'courts': courts,
    }
    return HttpResponse(template.render(context, request))

def court_detail(request, id):
    court = get_object_or_404(Court, id=id)  # Fetch a single court instance or 404
    template = loader.get_template('court_detail.html')  # Your new template for details
    context = {
        'court': court,
    }
    return HttpResponse(template.render(context, request))