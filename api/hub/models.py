from django.db import models

class Link(models.Model):
    CATEGORY_CHOICES = [
        ('1_project', 'Featured Projects'),
        ('2_cert', 'Certificates'),
        ('3_social', 'Social Connect'),
    ]
    
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200, blank=True)
    url = models.URLField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='1_project')
    icon_name = models.CharField(max_length=50, default='link', help_text="Lucide icon name (e.g., cpu, award, github)")
    image = models.ImageField(upload_to='previews/', blank=True, null=True, help_text="Upload local photo/certificate (Overrides URL)")
    image_url = models.CharField(max_length=500, blank=True, null=True, help_text="URL or static path to banner image")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['category', 'order']

    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"