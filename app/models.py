from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField(blank=True,null=True)
    AVTOMAT = "Avtomat"
    MEXANIKA = "Mexanika"
    Korobka = [
        (AVTOMAT , "Avtomat"),
        (MEXANIKA , "Mexanika"),
    ]
    box = models.CharField(
        max_length=100,
        choices=Korobka,
        default=MEXANIKA
    )
    GAZ = "Gaz"
    BENZIN = "Benzin"
    TOQ = "Toq"
    fuel=[
        (GAZ , 'Gaz'),
        (BENZIN , "Benzin"),
        (TOQ , 'Toq'),
    ]
    box_fuel= models.CharField(
        max_length=100,
        choices=fuel,
        default=GAZ,
    )
    four_people= models.BooleanField(blank=True,null=True)

    image=models.ImageField(blank=True,null=True)
    isbooked=models.BooleanField(blank=True,null=True,default=False)
    def __str__(self):
        return self.name