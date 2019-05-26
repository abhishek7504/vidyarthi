from django.contrib import admin
from .models import Profile,Education,Courses,Other_doc, ProfileQRCode

class EducationAdmin(admin.StackedInline):
        model = Education
        extra = 0

class CoursesAdmin(admin.StackedInline):
        model = Courses
        extra = 0

class Other_docAdmin(admin.StackedInline):
        model = Other_doc
        extra = 0

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
        list_display = ['__str__','id']
        inlines = [EducationAdmin,CoursesAdmin,Other_docAdmin]


admin.site.register(ProfileQRCode)        