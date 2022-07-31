from django.contrib import admin
from .models import CustomUser, Loan, Profile


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'age', 'phone_number')


class LoanAdmin(admin.ModelAdmin):
    list_display = ('customUser', 'amount',)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Loan, LoanAdmin)
admin.site.register(Profile, ProfileAdmin)
