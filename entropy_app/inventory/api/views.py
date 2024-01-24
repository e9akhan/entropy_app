import json
from datetime import datetime
from  django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from inventory.models import InventoryModel, ItemModel, CommodityModel, Department


@csrf_exempt
def items_api(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf8'))

        ItemModel.objects.create(
            name = body['name'],
            depreciation_percent = body.get('depreciation_percent', 10),
        )
        return JsonResponse({'message': 'Item created'}, safe=False)

    serialized_data = serializers.serialize('json', ItemModel.objects.all())
    return JsonResponse(json.loads(serialized_data), safe=False)


@csrf_exempt
def items_api_with_name(request, name):
    item = ItemModel.objects.get(name=name)

    if request.method == 'PUT':
        body = json.loads(request.body.decode('utf8'))

        item.name = body['name']
        item.depreciation_percent = body['depreciation_percent']
        item.save()

        return JsonResponse({'message': 'Item Updated'}, safe=False)

    if request.method == 'PATCH':
        body = json.loads(request.body.decode('utf8'))

        if 'name' in body:
            item.name = body['name']

        if 'depreciation_percent' in body:
            item.depreciation_percent = body['depreciation_percent']

        item.save()
        return JsonResponse({'message': 'Item Updated'}, safe=False)

    if request.method == 'DELETE':
        item.delete()
        return JsonResponse({'message': 'Item Deleted'}, safe=False)

    serialized_data = serializers.serialize('json', ItemModel.objects.filter(name = name))
    return JsonResponse(json.loads(serialized_data), safe=False)


@csrf_exempt
def inventories_api(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf8'))

        InventoryModel.objects.create(
            quantity = body['quantity'],
            price = body['price'],
            buy_date = datetime.strptime(body['buy_date'], '%Y-%m-%d'),
            current_price = body['current_price'],
            item = ItemModel.objects.get(name=body['item'])
        )
        return JsonResponse({'message': 'Inventory created'}, safe=False)

    serialized_data = serializers.serialize('json', InventoryModel.objects.all())
    return JsonResponse(json.loads(serialized_data), safe=False)


@csrf_exempt
def inventories_api_with_pk(request, pk):
    inventory = InventoryModel.objects.get(pk = pk)

    if request.method == 'PUT':
        body = json.loads(request.body.decode('utf8'))

        inventory.pk = body['pk']
        inventory.quantity = body['quantity']
        inventory.price = body['price']
        inventory.current_price = body['current_price']
        inventory.buy_date = datetime.strptime(body['buy_date'], '%Y-%m-%d')
        inventory.item = ItemModel.objects.get(name=body['item'])

        inventory.save()
        return JsonResponse({'message': 'Inventory Updated'}, safe=False)

    if request.method == 'PATCH':
        body = json.loads(request.body.decode('utf8'))

        if 'pk' in body:
            inventory.pk = body['pk']

        if 'quantity' in body:
            inventory.quantity = body['quantity']

        if 'price' in body:
            inventory.price = body['price']

        if 'current_price' in body:
            inventory.current_price = body['current_price']

        if 'buy_date' in body:
            inventory.buy_date = datetime.strptime(body['buy_date'], '%Y-%m-%d')

        if 'item' in body:
            inventory.item = ItemModel.objects.get(name = body['item'])

        inventory.save()
        return JsonResponse({'message': 'Inventory updated'}, safe=False)

    if request.method == 'DELETE':
        inventory.delete()
        return JsonResponse({'message': 'Inventory Deleted'}, safe=False)

    serialized_data = serializers.serialize('json', InventoryModel.objects.filter(pk = pk))
    return JsonResponse(json.loads(serialized_data), safe=False)


@csrf_exempt
def department_api(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf8'))

        Department.objects.create(name = body['name'])

        return JsonResponse({'message': 'Department created'}, safe=False)

    serialized_data = serializers.serialize('json', Department.objects.all())
    return JsonResponse(json.loads(serialized_data), safe=False)


@csrf_exempt
def department_api_with_name(request, name):
    department = Department.objects.get(pk = name)

    if request.method == 'PUT':
        body = json.loads(request.body.decode('utf8'))

        department.name = body['name']
        department.save()

        return JsonResponse({'message': 'Department updated'}, safe=False)

    if request.method == 'PATCH':
        body = json.loads(request.body.decode('utf8'))

        department.name = body['name']
        department.save()

        return JsonResponse({'message': 'Department updted'}, safe=False)
    
    if request.method == 'DELETE':
        department.delete()
        return JsonResponse({'message': 'Department deleted'}, safe=False)

    serialized_data = serializers.serialize('json', Department.objects.filter(name = name))
    return JsonResponse(json.loads(serialized_data), safe=False)


@csrf_exempt
def commodity_api(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf8'))

        CommodityModel.objects.create(
            id = body['id'],
            assign_to = body['assign_to'],
            item_name = ItemModel.objects.get(pk=body['item']),
            department = Department.objects.get(name = body['department']),
            status = body['status']
        )
        return JsonResponse({'message': 'Commodity created.'}, safe=False)

    serialized_data = serializers.serialize('json', CommodityModel.objects.all())
    return JsonResponse(json.loads(serialized_data),safe=False)


@csrf_exempt
def commodity_api_with_id(request, id):
    commodity = CommodityModel.objects.get(id = id)

    if request.method == 'PUT':
        body = json.loads(request.body.decode('utf8'))

        commodity.id = body['id']
        commodity.assign_to = body['assign_to']
        commodity.item_name = ItemModel.objects.get(pk = body['item'])
        commodity.department = Department.objects.get(name = body['department'])
        commodity.status = body['status']

        commodity.save()
        return JsonResponse({'message': 'Commodity Updated'}, safe=False)

    if request.method == 'PATCH':
        body = json.loads(request.body.decode('utf8'))

        if 'id' in body:
            commodity.id = body['id']

        if 'assign_to' in body:
            commodity.assign_to = body['assign_to']

        if 'item_name' in body:
            commodity.commodity_name = ItemModel.objects.get(pk = body['item'])

        if 'department' in body:
            commodity.department = Department.objects.get(name = body['department'])

        if 'status' in body:
            commodity.status = body['status']

        commodity.save()
        return JsonResponse({'message': 'Commodity updated'}, safe=False)

    if request.method == 'DELETE':
        commodity.delete()
        return JsonResponse({'message': 'Commodity deleted'}, safe=False)

    serialized_data = serializers.serialize('json', CommodityModel.objects.filter(id = id))
    return JsonResponse(json.loads(serialized_data), safe=False)
