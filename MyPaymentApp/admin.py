# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *
# Register your models here.
# from django.apps import apps

# models = apps.get_models()

# print(models)
# for model in models:
#     pass
#     # admin.site.register(model)

admin.site.register(RazorpayResponsew)
admin.site.register(PaymentDetail)
