import random
from datetime import date, timedelta
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class InventoryModel(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    depreciation_percent = models.IntegerField(default=10)

    @staticmethod
    def get_inventory_name():
        return [
            'Laptop',
            'Monitor',
            'Mouse',
            'Keyboard',
            'Machines'
        ]

    @staticmethod
    def create_random_data():
        for inventory in InventoryModel.get_inventory_name():
            InventoryModel.objects.create(name = inventory, depreciation_percent = random.randint(5, 10)).save()

    def __str__(self):
        return f'{self.name}'


class Department(models.Model):
    name = models.CharField(max_length = 50, primary_key = True)

    @staticmethod
    def get_department_name():
        return [
            'Cohort-' + str(x)
            for x in range(1, 11)
        ]
    
    @staticmethod
    def create_random_departments():
        for department in Department.get_department_name():
            Department.objects.create(name = department).save()

    def __str__(self):
        return f'{self.name}'


class CommoditiesModel(models.Model):

    quantity = models.IntegerField(default=0)
    price = models.FloatField(
        help_text = 'Price of each commodity.'
    )
    current_price = models.FloatField()
    buy_date = models.DateField(
        help_text = 'Enter Date in YYYY-MM-DD format.'
    )
    total_assigned = models.IntegerField(default=0)
    inventory = models.ForeignKey(InventoryModel, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    @staticmethod
    def get_inventory():
        return list(InventoryModel.objects.all())
    
    @staticmethod
    def get_department():
        return list(Department.objects.all())

    @staticmethod
    def get_date():
        return [date.today() - timedelta(days = x) for x in range(40)]
    
    @staticmethod
    def create_random_commodities():
        inventories = CommoditiesModel.get_inventory()
        departments = CommoditiesModel.get_department()
        dates = CommoditiesModel.get_date()
        quantites = list(range(10, 70))
        prices = list(range(1000, 100000, 10000))
        current_prices = list(range(1000, 90000, 10000))
        assigned = list(range(10, 50))

        for _ in range(10):
            CommoditiesModel.objects.create(
                quantity = random.choice(quantites),
                price = random.choice(prices),
                current_price = random.choice(current_prices),
                buy_date = random.choice(dates),
                total_assigned = random.choice(assigned),
                inventory = random.choice(inventories),
                department = random.choice(departments),
            )

    def __str__(self):
        return f'Commodities - {self.inventory} - {self.id}'


class CommodityModel(models.Model):
    status_code = [
        ('functional', 'Functional'),
        ('nonfunctional', 'Non-functional')
    ]

    id = models.CharField(max_length=20, primary_key=True)
    assign_to = models.CharField(max_length=50)
    commodity_name = models.ForeignKey(CommoditiesModel, on_delete=models.CASCADE)
    status = models.CharField(max_length = 20, choices = status_code, default = 'functional')

    @staticmethod
    def get_commodities():
        return list(CommoditiesModel.objects.all())
    
    @staticmethod
    def get_id():
        return ['E9-' + str(i) for i in range(1, 41)]
    
    @staticmethod
    def get_names():
        return ['John', 'micheal', 'Maria', 'Joe', 'Donald', 'Richard']

    @staticmethod
    def create_random_commodity():
        commodities = CommodityModel.get_commodities()
        ids = CommodityModel.get_id()
        names = CommodityModel.get_names()

        for i in range(40):
            CommodityModel.objects.create(
                id = ids[i],
                assign_to = random.choice(names),
                commodity_name = random.choice(commodities),
                status = random.choice(['functional', 'nonfunctional'])
            )

    def save(self, **kwargs):
        self.commodity_name.total_assigned += 1
        return super().save(**kwargs)

    def __str__(self):
        return f'{self.commodity_name.inventory} - {self.id}'
