from django import forms
from django.contrib import admin

from personal_page.widgets import HtmlEditor
from main.models import Command


class CommandAdminForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        widgets = {
            "code": HtmlEditor(
                attrs={
                    "style": "width: 90%; height: 100%;"
                }
            )
        }

    model = Command


@admin.register(Command)
class CommandAdmin(admin.ModelAdmin):
    form = CommandAdminForm
