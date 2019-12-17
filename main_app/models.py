from django.db import models
from django.urls import reverse
from datetime import date

DAMAGE = (
    ('C', 'Critical Hit'),
    ('S', 'Super Effective'),
    ('N', 'Not very effective'),
)


class Item(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('items_detail', kwargs={'pk': self.id})


class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    attribute = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    level = models.IntegerField()
    items = models.ManyToManyField(Item)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pokemon_id': self.id})

    def battle_for_today(self):
        return self.battles_set.filter(date=date.today()).count() >= len(DAMAGE)


class Battles(models.Model):
    date = models.DateField('battle date')
    damage = models.CharField(
        max_length=1,
        choices=DAMAGE,
        default=DAMAGE[0][0]
    )
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_damage_display()} on {self.date}"

    class Meta:
        ordering = ['-date']
