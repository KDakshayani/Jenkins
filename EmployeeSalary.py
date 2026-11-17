# Employee Salary Calculator
basic_salary = 50000

# Calculate HRA (20%) and DA (10%)
hra = 0.20 * basic_salary
da = 0.10 * basic_salary

# Calculate Gross Salary
gross_salary = basic_salary + hra + da

# Display the output
print(f"Basic Salary : {basic_salary}")
print(f"HRA (20%)    : {hra}")
print(f"DA (10%)     : {da}")
print(f"Gross Salary : {gross_salary}")