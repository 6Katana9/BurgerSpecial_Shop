from django.db import models


class Cotegory(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return str(self.title)


class Company(models.Model):
    name = models.CharField('Название', max_length=40)
    about = models.CharField('О компании', max_length=1000)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

class Products(models.Model):
    images = models.ImageField(upload_to='media/', verbose_name='Вид', blank=True, null=True)
    name = models.CharField('Название', max_length=30)
    cotegory = models.ForeignKey(Cotegory, related_name='products', on_delete=models.CASCADE)
    companys = models.ManyToManyField(Company, verbose_name='Изготовитель')
    about = models.TextField('О блюде')
    price = models.PositiveIntegerField(null=True, verbose_name="Цена")

    def get_absolute_url(self):
        return f'/menu/{self.id}'

    def get_companys(self):
        return ', '.join([cat.name for cat in self.companys.all()])

    def __str__(self):
        return str(self.name)
    

    @property
    def images_url(self):
        if self.images and hasattr(self.images, 'url'):
            return self.images.url
    
    class Meta:
        verbose_name = 'Еду'
        verbose_name_plural = 'Еда'

