from django.contrib.syndication.views import Feed
from django.urls import reverse


class NewInventoryFeed(Feed):
    title = "New Inventory"
    link = "/newitem/"

    def items(self):
        return ("iphone12", "pixel4xl", "samsung note")

    def item_title(self, item):
        return "New Inventory Item"

    def item_description(self, item):
        return item

    def item_link(self, item):
        return reverse('newitem')