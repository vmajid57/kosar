from django.contrib import admin
from .models import CustomUser, Loan


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'age', 'phone_number')


class LoanAdmin(admin.ModelAdmin):
    list_display = ('customUser', 'amount',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Loan, LoanAdmin)
