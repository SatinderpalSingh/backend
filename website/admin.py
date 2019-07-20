from django.contrib import admin
from reversion.admin  import VersionAdmin
# Register your models here.
from .models import mission, vision

#admin.site.register(mission)
admin.site.register(vision)

class Adminmission(VersionAdmin):
      recover_form_template='reversion/recover_form.html'

admin.site.register(mission,Adminmission)
