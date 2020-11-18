from django.contrib import admin
from .models import Group
from .models import Label
from .models import Location
from .models import Record
from .models import Source
from .models import Unit

admin.site.register(Group)
admin.site.register(Label)
admin.site.register(Location)
admin.site.register(Record)
admin.site.register(Source)
admin.site.register(Unit)

