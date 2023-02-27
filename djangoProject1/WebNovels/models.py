from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=200, default='Tag')

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200, default='Author')
    date = models.DateTimeField(auto_now_add=True)
    mail = models.EmailField(null=True)

    def __str__(self):
        return self.name


class WebNovels(models.Model):

    STATUS = (
        ('Completed', 'Completed'),
        ('On a Break', 'On a Break'),
        ('Ongoing', 'Ongoing'),
    )

    name = models.CharField(max_length=200, default='Webnovel')
    pub_date = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    views = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    length = models.IntegerField(null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name