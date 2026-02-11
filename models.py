from django.db import models


# ------------------------------------------
# MAINTENANCE MODULE (MANDATORY)
# ------------------------------------------
class Maintenance(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# ------------------------------------------
# MEMBERSHIP MODULE
# ------------------------------------------
class Membership(models.Model):

    DURATION = [
        ('6M', '6 Months'),
        ('1Y', '1 Year'),
        ('2Y', '2 Years')
    ]

    membership_number = models.AutoField(primary_key=True)

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    duration = models.CharField(
        max_length=2,
        choices=DURATION,
        default='6M'
    )

    active = models.BooleanField(default=True)

    maintenance = models.ForeignKey(
        Maintenance,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return f"{self.name} - {self.membership_number}"


# ------------------------------------------
# TRANSACTION MODULE
# ------------------------------------------
class Transaction(models.Model):

    membership = models.ForeignKey(
        Membership,
        on_delete=models.CASCADE
    )

    action = models.CharField(max_length=50)

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.membership} - {self.action}"
