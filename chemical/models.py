from django.db import models

# Create your models here.


class Chemical_Reaction(models.Model):
    # array of reactants
    reactants = models.TextField(max_length=200)

    def get_equations(self):
        equations = self.reactants.split("\n")
        return equations

    def __str__(self) -> str:
        return self.reactants
