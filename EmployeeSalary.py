# Function to calculate allowances and gross salary
import sys
def calculate_salary(basic_salary):
    hra = 0.20 * basic_salary
    da = 0.10 * basic_salary
    gross_salary = basic_salary + hra + da
    return hra, da, gross_salary

# Function to display the salary breakdown
def display_salary(basic_salary, hra, da, gross_salary):
    print("\n--- Salary Breakdown ---")
    print(f"Basic Salary : {basic_salary:.2f}")
    print(f"HRA (20%)    : {hra:.2f}")
    print(f"DA (10%)     : {da:.2f}")
    print(f"Gross Salary : {gross_salary:.2f}")

# Main function to run the program
def main():
    basic_salary=int(sys.argv[1])
    basic_salary = float(input("Enter the Basic Salary: "))
    hra, da, gross_salary = calculate_salary(basic_salary)
    display_salary(basic_salary, hra, da, gross_salary)

# Execute the program
if __name__ == "__main__":
    main()