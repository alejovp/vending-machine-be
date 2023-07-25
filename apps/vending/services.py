from apps.vending.models import VendingMachineSlot

MAX_ROW = 3
MAX_COLUMN = 3
DEFAULT_SLOTS_GRID = [[{} for i in range(MAX_COLUMN)] for i in range(MAX_ROW)]
DEFAULT_PASSWORD = 'Test_1234'

def format_slots_into_products_grid():
    fields = ['quantity', 'row', 'column', 'product__id', 'product__name', 'product__price']
    slots = VendingMachineSlot.objects.prefetch_related('product').values(*fields)
    slots_grid_dict = {
        (s['row'], s['column']): { "id": s['product__id'], "name": s['product__name'], "price": s["product__price"], "quantity": s["quantity"] } for s in slots
    }
    product_slots_grid = DEFAULT_SLOTS_GRID

    for (row, column), product in slots_grid_dict.items():
        product_slots_grid[row - 1][column - 1] = product
    
    return product_slots_grid
    