import restaurantTables as rt

def time_check(table_list):
    free_tables = []
    timeslot = int(input("Please enter a timeslot from 1 to 6: "))
    if timeslot < 1 or timeslot > 6:
        print("That timeslot doesn't exist.")
        time_check(table_list)
    else:
        table = 1
        while table <= 6:
            if table_list[timeslot][table] == "o":
                free_tables.append(table_list[0][table])
                table += 1
            else:
                table += 1
    return free_tables

def party_check(table_list):
    free_tables = time_check(table_list)
    party_size = int(input("Please enter how many people are in your party: "))
    for table in free_tables:
        if int(table[3::4]) < party_size:
            free_tables.remove(table)
    return free_tables

def table_report(table_list):
    free_tables = party_check(table_list)
    print("The following tables are available: " + str(free_tables))

table_report(rt.restaurant_tables2)