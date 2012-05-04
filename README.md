Django-Permissions-Keeper
=========================

An easy way to keep group permissions in sync between Development and Production environments.

## Installation
1. Install "pip install permkeep"
2. Add permkeep to your installed apps in settings.py.

```python
INSTALLED_APPS = (
    ...
    'permkeep',
    ...
)
```

3. Define your group permissions in settings.py.

a = Add, c = Change, d = Delete

```python
GROUP_PERMISSIONS = (
  {
    'name': 'Editor',
    'codes': (
      ('event', 'acd'),
      ('newsitem','acd'),
      ('tag','acd'),
      ('category','ac'),
      ('peopletag','acd'),
    )
  },
  
  {
    'name': 'Contributor',
    'codes': (
      ('event', 'ac'),
      ('newsitem','ac'),
      ('tag','a'),
      ('peopletag','a'),
    )
  }
)
```

4. Run "./manage.py setperms"

This will add any groups and permissions that currently don't exist. It does not delete permissions.

You can run the command several times to add permissions in the future.  If the permission already exists it will skip over it.
