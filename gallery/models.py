from django.db import models


class Pictures(models.Model):
    title = models.CharField("Название", max_length=56)
    picture = models.URLField("Картина")
    description = models.TextField("Описание картины")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/gallery/{self.id}"

    class Meta:
        verbose_name = "Картина"
        verbose_name_plural = "Картины"
