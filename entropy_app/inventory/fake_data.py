from inventory.models import CommoditiesModel, CommodityModel, InventoryModel

if __name__ == '__main__':
    InventoryModel.create_random_data()
    CommoditiesModel.create_random_commodities()
    CommodityModel.create_random_commodity()