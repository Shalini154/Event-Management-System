from django.contrib import admin
from .models import Membership, Maintenance, Transaction

admin.site.register(Membership)
admin.site.register(Maintenance)
admin.site.register(Transaction)
