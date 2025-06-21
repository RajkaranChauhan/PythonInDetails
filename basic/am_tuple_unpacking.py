stock_price=[('apple',200),('infy',150),('micro',99)]

#1
for val in stock_price:
    print(val)
    # ('apple', 200)
    # ('infy', 150)
    # ('micro', 99)

#2
for stock,price in stock_price:
    print(stock)

# apple
# infy
# micro

#3
for stock,price in stock_price:
    print(price+price*.1)

# 220.0
# 165.0
# 108.9

#4
work_hours=[('raj',40),('karan',42),('laxmi', 45)]

def emp_of_month(work_hr):
    max_hour = 0
    emp_of_month = ''
    for name,hours in work_hr:
        if (hours>max_hour):
            max_hour=hours
            emp_of_month=name
        else:
            pass
    return f"Employee of the month is '{emp_of_month}' with working hours '{max_hour}'"

print(emp_of_month(work_hours)) # Employee of the month is 'laxmi' with working hours '45'



