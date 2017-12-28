from django.contrib import admin
from cmdb_app.models import *
# Register your models here.


admin.site.register(UserProfile )
admin.site.register(AdminInfo )
admin.site.register(UserGroup)
admin.site.register(BusinessUnit )
admin.site.register(IDC)
admin.site.register(Tag )
admin.site.register(Disk)
admin.site.register(NIC)
admin.site.register(Asset)
admin.site.register(Server)
admin.site.register(NetworkDevice)
admin.site.register(Memory)
admin.site.register(AssetRecord)
admin.site.register(ErrorLog)
