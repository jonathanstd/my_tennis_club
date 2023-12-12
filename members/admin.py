from django.contrib import admin
from .models import Member
from .models import Court


class MemberAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'age', 'joined_date', 'age_group')

    def age_group(self, obj):
        return 'Teenager' if obj.age and obj.age < 20 else 'Adult'
    age_group.short_description = 'Age Group'
admin.site.register(Member, MemberAdmin)

class CourtAdmin(admin.ModelAdmin):
    list_display = ('name', 'court_type', 'city')
admin.site.register(Court, CourtAdmin)

