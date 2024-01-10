from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Notes

def notes(request):
  notes = Notes.objects.all().values()
  template = loader.get_template('notes.html')
  context = {
    'notes': notes,
  }
  return HttpResponse(template.render(context, request))