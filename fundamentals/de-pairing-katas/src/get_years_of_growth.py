def get_years_of_growth(start_pop, end_pop, perct_growth, migration):
    count = 0
    current_pop=start_pop
    while current_pop < end_pop:
        current_pop=current_pop*(1+(perct_growth/100))+migration
        count+=1
    return count
    
