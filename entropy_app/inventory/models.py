import random
from datetime import date, timedelta
from django.db import models


# Create your models here.
class NomenclatureModel(models.Model):
    """
    Item Model.
    """

    name = models.CharField(max_length=50, primary_key=True)

    @property
    def get_quantity(self):
        """
        Get quantity of items.
        """
        return sum(
            [
                record.quantity
                for record in RecordModel.objects.filter(nomenclature=self.name)
            ]
        )

    @property
    def generate_id(self):
        """
        Generate ids.
        """
        items = list(
            AssignItemModel.objects.filter(nomenclature=self.name, status="Assigned")
        ) + list(
            AssignItemModel.objects.filter(
                nomenclature=self.name, functionality="Non-Functional"
            )
        )
        ids = [self.name[:3] + "-" + str(i) for i in range(1, self.get_quantity + 1)]

        for item in items:
            id = item.item_id
            if id in ids:
                ids.remove(item.item_id)

        return ids

    @property
    def get_functional_items(self):
        """
        Get length of functional items.
        """
        return self.get_quantity - len(
            list(
                AssignItemModel.objects.filter(
                    nomenclature=self.name, functionality="Non-Functional"
                )
            )
        )

    @property
    def get_remaining_items(self):
        """
        Get remaining items.
        """
        return self.get_functional_items - len(
            list(
                AssignItemModel.objects.filter(
                    nomenclature=self.name, status="Assigned"
                )
            )
        )

    @staticmethod
    def get_item_name():
        """
        Get list of item names.
        """
        return ["Laptop", "Monitor", "Mouse", "Keyboard", "CPU"]

    @classmethod
    def create_random_data(cls):
        """
        Create random nomenclature.
        """
        for item in cls.get_item_name():
            cls.objects.create(
                name=item,
            )

    def __str__(self):
        """String representation"""
        return f"{self.name}"


class Department(models.Model):
    """
    Department Model.
    """

    name = models.CharField(max_length=50, primary_key=True)

    @staticmethod
    def get_department_name():
        """
        Get list of department name.
        """
        return ["Cohort-" + str(x) for x in range(1, 11)]

    @classmethod
    def create_random_departments(cls):
        """
        Create random department data.
        """
        for department in cls.get_department_name():
            cls.objects.create(name=department)

    def __str__(self):
        """String representation"""
        return f"{self.name}"


class RecordModel(models.Model):
    """
    Inventory Model.
    """

    quantity = models.IntegerField(default=0)
    price = models.FloatField(help_text="Price of each commodity.")
    buy_date = models.DateField(help_text="Enter Date in YYYY-MM-DD format.")
    nomenclature = models.ForeignKey(NomenclatureModel, on_delete=models.CASCADE)

    @staticmethod
    def get_nomenclatures():
        """
        Get item's queryset.
        """
        return list(NomenclatureModel.objects.all())

    @staticmethod
    def get_date():
        """
        Get list of dates.
        """
        return [date.today() - timedelta(days=x) for x in range(40)]

    @classmethod
    def create_random_records(cls):
        """
        Create random records.
        """
        nomenclatures = cls.get_nomenclatures()
        dates = cls.get_date()
        quantites = list(range(10, 70))
        prices = list(range(1000, 100000, 10000))

        for _ in range(10):
            cls.objects.create(
                quantity=random.choice(quantites),
                price=random.choice(prices),
                buy_date=random.choice(dates),
                nomenclature=random.choice(nomenclatures),
            )

    def __str__(self):
        """String representation"""
        return f"{self.id:0>8d}"


class AssignItemModel(models.Model):
    """
    Assign Item Model.
    """

    status_code = [("Assigned", "Assigned"), ("In-Stock", "In-Stock")]

    functionality_code = [
        ("Functional", "Functional"),
        ("Non-Functional", "Non-Functional"),
    ]

    assign_to = models.CharField(max_length=50, blank=True)
    nomenclature = models.ForeignKey(NomenclatureModel, on_delete=models.CASCADE)
    item_id = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=status_code, default="Assigned")
    functionality = models.CharField(
        max_length=20, choices=functionality_code, default="Functional"
    )

    @staticmethod
    def get_items():
        """
        Get item's queryset.
        """
        return list(NomenclatureModel.objects.all())

    @staticmethod
    def get_names():
        """
        Get names.
        """
        return ["John", "micheal", "Maria", "Joe", "Donald", "Richard"]

    @staticmethod
    def get_departments():
        """
        Get department's queryset.
        """
        return list(Department.objects.all())

    def __str__(self):
        """String representation"""
        return f"{self.item_id}"
