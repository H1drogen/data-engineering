def order_veg(veg_list):
    sorted(veg_list, key=lambda x: x['quantity'])

    return veg_list
