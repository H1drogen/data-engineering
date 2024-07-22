def count_veg(veg_list,veg_type):
    count=0
    for item in veg_list:
        if item['type'] ==veg_type:
            count+=item['quantity']
    
    return count
    pass
