from django.db import models

class country (models.Model):
    country_name = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.country_name

class state (models.Model):
    state_name = models.CharField(max_length=200, null=True)
    country = models.ForeignKey(country, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.state_name

class city (models.Model):
    city_name = models.CharField(max_length=200, null=True)
    country = models.ForeignKey(country, on_delete=models.CASCADE, null=True)
    state = models.ForeignKey(state, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.city_name

class publication(models.Model):
    title= models.CharField(max_length=300, null=True)
    country=models.ForeignKey(country, on_delete=models.CASCADE, null=True)
    state=models.ForeignKey(state, on_delete=models.CASCADE, null=True)
    city=models.ForeignKey(city, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title