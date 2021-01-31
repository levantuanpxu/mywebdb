from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Categories(models.Model):
    #định nghĩa các trường dữ liệu

    name = models.CharField(max_length=500)

    #xây dựng hàm in nội dung của đối tượng ra màn hình
    def __str__(self):
        s = str(self.name)
        return s

class Post(models.Model):

    title = models.CharField(max_length=500)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()
    categories = models.ForeignKey(Categories, null=False, verbose_name=_('Category'),
                                   on_delete=models.CASCADE)

    def __str__(self):
        return self.title