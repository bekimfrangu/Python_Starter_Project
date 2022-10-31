from django.contrib import admin
from .models import Tutorial, TutorialCategory, TutorialSeries

class TutorialAdmin(admin.ModelAdmin):
    # fields = ["tutorial_title",
    #           "tutorial_published",
    #           "tutorial_content",
    #           ]
    fieldsets = [
        ("Title/Date", {"fields":["tutorial_title","tutorial_published"]}),
        ("URL", {"fields":["tutorial_slug"]}),
        ("Series", {"fields":["tutorial_series"]}),
        ("Content", {"fields":["tutorial_content"]})
    ]
# Register your models here.
admin.site.register(TutorialCategory)
admin.site.register(TutorialSeries)
admin.site.register(Tutorial, TutorialAdmin)
