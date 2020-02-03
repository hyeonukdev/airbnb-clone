from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.
@admin.register(models.User)  # admin.site.register(models.User, CustomUserAdmin)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                ),
            },
        ),
    )

    # list_display = ("username", "gender", "language", "currency", "superhost")
    # list_filter = (
    #     "superhost",
    #     "language",
    #     "currency",
    # )

