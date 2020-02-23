salary = float(input("Entry with a normal salary of worker: "))
reajust = float(salary*0.15)
new_salary = float(salary+reajust)
print("new salary of worker with reajusted in 15% is ${:.2f}".format(new_salary))