from django.contrib.sitemaps import Sitemap


class LatestSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return {"iphone8", "Lenovo", "Pixel 3a"}

    def lastmod(self, obj):
        return obj.pub_date