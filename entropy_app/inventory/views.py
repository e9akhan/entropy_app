from django.shortcuts import render
from django.views.generic import CreateView
from inventory.forms import CommoditiesForm, CommodityForm, AddInventoryForm
from inventory.models import Commodities, Commodity, Inventory


# Create your views here.
