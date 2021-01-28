#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 16:54:29 2021

@author: lilygoodyersait
"""
###Basic analysis of data using loops

names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

###For loops
total_cost=0
for i in estimated_insurance_costs:
  total_cost+=i
  
print(total_cost)

average_cost=total_cost/len(estimated_insurance_costs)

print("Average Insurance Cost: "+str(average_cost)+ " dollars.")
for i in range(len(names)):
  name=names[i]
  insurance_cost=actual_insurance_costs[i]
  print("The insurance cost for " + name + " is " + str(insurance_cost)+ " dollars.")
  if insurance_cost > average_cost:
    print("The insurance cost for "+name+ " is above average.")
  elif insurance_cost < average_cost:
    print("The insurance cost for "+name+" is below average.")
  else:
    print("The insurance cost for " +name+ " is equal to the average.")


updated_estimated_costs=[x*1.1 for x in estimated_insurance_costs]
print(updated_estimated_costs)


### while loops and calculate difference between average and actual costs

total_cost=0
i=0
while i < len(estimated_insurance_costs):
  total_cost+=estimated_insurance_costs[i]
  i+=1
  
print(total_cost)

average_cost=total_cost/len(estimated_insurance_costs)

print("Average Insurance Cost: "+str(average_cost)+ " dollars.")

for i in range(len(names)):
  name=names[i]
  insurance_cost=actual_insurance_costs[i]
  difference=actual_insurance_costs[i]-average_cost
  print("The insurance cost for " + name + " is " + str(insurance_cost)+ " dollars.")
  if insurance_cost > average_cost:
    print("The insurance cost for "+name+ " is " + str(difference) + " dollars more than average.")
  elif insurance_cost < average_cost:
    print("The insurance cost for "+name+" is " + str(difference)+ " dollars less than average")
  else:
    print("The insurance cost for " +name+ " is equal to the average.")


updated_estimated_costs=[x*1.1 for x in estimated_insurance_costs]
print(updated_estimated_costs)