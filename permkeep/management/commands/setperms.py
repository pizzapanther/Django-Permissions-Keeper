from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group, Permission

def set_perms (groups, output=True):
  pmap = {'a': 'add_', 'c': 'change_', 'd': 'delete_'}
  
  for g in groups:
    query = Group.objects.filter(name=g['name'])
    if query.count() == 0:
      group = Group(name=g['name'])
      group.save()
      if output:
        print "Added Group: %s" % g['name']
      
    else:
      if output:
        print "Using Group: %s" % g['name']
        
      group = query[0]
      
    for c in g['codes']:
      for key, prefix in pmap.items():
        if key in c[1]:
          codename = prefix + c[0]
          
          q = group.permissions.filter(codename=codename)
          if q.count() == 0:
            pm = Permission.objects.get(codename=codename)
            group.permissions.add(pm)
            if output:
              print "  Added Permission: %s" % codename
              
          else:
            if output:
              print "  Skipping Permission: %s" % codename
              
    if output:
      print ""
      
  if output:
    print "Set Permissions Complete\n\n"
    
class Command (BaseCommand):
  help = 'Creates groups and sets permissions'

  def handle(self, *args, **options):
    set_perms(settings.GROUP_PERMISSIONS)
    