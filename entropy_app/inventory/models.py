import random
from datetime import date, timedelta
from django.db import models

# Create your models here.
class ItemModel(models.Model):
    """
        Item Model.
    """
    name = models.CharField(max_length=50, primary_key=True)
    depreciation_percent = models.IntegerField(default=10)

    @property
    def get_quantity(self):
        """
            Get quantity of items.
        """
        return sum([inventory.quantity for inventory in InventoryModel.objects.filter(item=self.name)])

    @property
    def get_functional_items(self):
        """
            Get length of functional items.
        """
        return self.get_quantity - len(list(CommodityModel.objects.filter(item = self.name, status='Non-Functional')))

    @property
    def get_assigned(self):
        """
            Get length of assigned commodity.
        """
        return len(list(CommodityModel.objects.filter(item = self.name)))

    @staticmethod
    def get_item_name():
        """
            Get list of item names.
        """
        return [
            'Laptop',
            'Monitor',
            'Mouse',
            'Keyboard',
            'Machines'
        ]

    @classmethod
    def create_random_data(cls):
        """
            Create random items.
        """
        for item in cls.get_item_name():
            cls.objects.create(
                name = item,
                depreciation_percent = random.randint(5, 10),
            )

    def __str__(self):
        return f'{self.name}'


class Department(models.Model):
    """
        Department Model.
    """
    name = models.CharField(max_length = 50, primary_key = True)

    @staticmethod
    def get_department_name():
        """
            Get list of department name.
        """
        return [
            'Cohort-' + str(x)
            for x in range(1, 11)
        ]
    
    @classmethod
    def create_random_departments(cls):
        """
            Create random department data.
        """
        for department in cls.get_department_name():
            cls.objects.create(name = department)

    def __str__(self):
        return f'{self.name}'


class InventoryModel(models.Model):
    """
        Inventory Model.
    """

    quantity = models.IntegerField(default=0)
    price = models.FloatField(
        help_text = 'Price of each commodity.'
    )
    current_price = models.FloatField()
    buy_date = models.DateField(
        help_text = 'Enter Date in YYYY-MM-DD format.'
    )
    item = models.ForeignKey(ItemModel, on_delete=models.CASCADE)

    @property
    def get_assigned(self):
        """
            Get assigned inventories.
        """
        inventory = InventoryModel.objects.get(id = self.id)
        return len(CommodityModel.objects.filter(inventory = inventory))

    @staticmethod
    def get_item():
        """
            Get item's queryset.
        """
        return list(ItemModel.objects.all())

    @staticmethod
    def get_date():
        """
            Get list of dates.
        """
        return [date.today() - timedelta(days = x) for x in range(40)]
    
    @classmethod
    def create_random_inventories(cls):
        """
            Create random inventory data.
        """
        items = cls.get_item()
        dates = cls.get_date()
        quantites = list(range(10, 70))
        prices = list(range(1000, 100000, 10000))
        current_prices = list(range(1000, 90000, 10000))

        for _ in range(10):
            cls.objects.create(
                quantity = random.choice(quantites),
                price = random.choice(prices),
                current_price = random.choice(current_prices),
                buy_date = random.choice(dates),
                item = random.choice(items),
            )

    def __str__(self):
        return f'{self.item} - {self.id}'


class CommodityModel(models.Model):
    """
        Commodity Model.
    """
    status_code = [
        ('Functional', 'Functional'),
        ('Non-functional', 'Non-functional')
    ]

    id = models.CharField(max_length=20, primary_key=True)
    assign_to = models.CharField(max_length=50, blank=True)
    item = models.ForeignKey(ItemModel, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    inventory = models.ForeignKey(InventoryModel, on_delete = models.CASCADE)
    status = models.CharField(max_length = 20, choices = status_code, default = 'Functional')

    @staticmethod
    def get_items():
        """
            Get item's queryset.
        """
        return list(ItemModel.objects.all())
    
    @staticmethod
    def get_id():
        """
            Get IDs.
        """
        return ['E9-' + str(i) for i in range(1, 41)]
    
    @staticmethod
    def get_names():
        """
            Get names.
        """
        return ['John', 'micheal', 'Maria', 'Joe', 'Donald', 'Richard']
    
    @staticmethod
    def get_departments():
        """
            Get department's queryset.
        """
        return list(Department.objects.all())
    
    @staticmethod
    def get_inventories():
        """
            Get inventory queryset.
        """
        return list(InventoryModel.objects.all())

    @classmethod
    def create_random_commodities(cls):
        """
            Create random commodity data.
        """
        items = cls.get_items()
        ids = cls.get_id()
        names = cls.get_names()
        departments = cls.get_departments()
        inventories = cls.get_inventories()

        for i in range(40):
            cls.objects.create(
                id = ids[i],
                assign_to = random.choice(names),
                item = random.choice(items),
                department = random.choice(departments),
                status = random.choice(['Functional', 'Non-Functional']),
                inventory = random.choice(inventories)
            )
        
    def save(self, **kwargs):
        inventory = InventoryModel.objects.get(id = self.inventory.id)
        self.item = ItemModel.objects.get(name = inventory.item)
        return super().save(**kwargs)

    def __str__(self):
        return f'{self.id}'
