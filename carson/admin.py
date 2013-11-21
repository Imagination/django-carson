from django.contrib import admin
from carson.models import Account, Tag
from carson.utils import lookup_twitter_ids

class AccountAdmin(admin.ModelAdmin):
    list_display = ["twitter_username", "twitter_id", 'active']
    actions = ('populate_twitter_ids', 'activate', 'deactivate')

    def populate_twitter_ids(self, request, queryset):
        updated = lookup_twitter_ids(queryset)
        self.message_user(request, "%d account(s) updated" % updated)
    populate_twitter_ids.short_description = "Lookup Twitter IDs"

    def activate(self, request, queryset):
	queryset.update(active = True)

    def deactivate(self, request, queryset):
	queryset.update(active = False)


class TagAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", 'active']
    actions = ('activate', 'deactivate')

    def activate(self, request, queryset):
	queryset.update(active = True)

    def deactivate(self, request, queryset):
	queryset.update(active = False)

    

admin.site.register(Account, AccountAdmin)
admin.site.register(Tag, TagAdmin)
