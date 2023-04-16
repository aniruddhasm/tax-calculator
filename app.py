import random
from time import sleep
from os import system, name
import sys
from prettytable import PrettyTable
from constants import *

old_tax_table = PrettyTable(OLD_TAX_HEADERS)
new_tax_table = PrettyTable(NEW_TAX_HEADERS)

def clear(sleep_time):
    sleep(sleep_time)
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def old_regime(taxable_amount):
    old_tax_table.add_row([ZERO_TO_TWO_POINT_FIVE_LAKH, NIL, ZERO])
    two_lakhs_bracket = (TWO_LAKH_FIFTY_THOUSAND * 0.05)

    if taxable_amount <= FIVE_LAKHS:
        old_tax_table.add_row([ZERO_TO_FIVE_LAKH, NIL, ZERO])
        return 0

    elif taxable_amount > TEN_LAKHS:
        pending_amount = taxable_amount - TEN_LAKHS

        old_tax_table.add_row([TWO_POINT_FIVE_TO_FIVE_LAKH, FIVE_PERCENT_RANGE, two_lakhs_bracket])
        old_tax_table.add_row([FIVE_TO_TEN_LAKH, TWENTY_PERCENT_RANGE, (FIVE_LAKHS * 0.2)])
        old_tax_table.add_row([GREATER_THAN_TEN_LAKH, THIRTY_PERCENT_RANGE, (pending_amount * 0.3)])
        
        return two_lakhs_bracket + (FIVE_LAKHS * 0.2) + (pending_amount * 0.3)

    elif taxable_amount >= FIVE_LAKHS and taxable_amount <= TEN_LAKHS:
        pending_amount = taxable_amount - FIVE_LAKHS

        old_tax_table.add_row([TWO_POINT_FIVE_TO_FIVE_LAKH, FIVE_PERCENT_RANGE, two_lakhs_bracket])
        old_tax_table.add_row([FIVE_TO_TEN_LAKH, TWENTY_PERCENT_RANGE, pending_amount * 0.2])

        return two_lakhs_bracket + (pending_amount * 0.2)

    elif taxable_amount >= TWO_LAKH_FIFTY_THOUSAND and taxable_amount <= FIVE_LAKHS:
        pending_amount = taxable_amount - TWO_LAKH_FIFTY_THOUSAND

        old_tax_table.add_row([TWO_POINT_FIVE_TO_FIVE_LAKH, FIVE_PERCENT_RANGE, pending_amount * 0.05])
        
        return (pending_amount * 0.05)


def new_regime(taxable_amount):
    three_lakh_bracket = (THREE_LAKHS * 0.05)
    new_tax_table.add_row([ZERO_TO_THREE_LAKH, NIL, ZERO])

    if taxable_amount <= SEVEN_LAKHS:
        new_tax_table.add_row([ZERO_TO_SEVEN_LAKH, NIL, ZERO])
        return 0

    elif taxable_amount >= FIFTEEN_LAKHS:
        pending_amount = taxable_amount - FIFTEEN_LAKHS

        new_tax_table.add_row([THREE_TO_SIX_LAKH, FIVE_PERCENT_RANGE, three_lakh_bracket])
        new_tax_table.add_row([SIX_TO_NINE_LAKH, TEN_PERCENT_RANGE, (THREE_LAKHS * 0.1)])
        new_tax_table.add_row([NINE_TO_TWELVE_LAKH, FIFTEN_PERCENT_RANGE, (THREE_LAKHS * 0.15)])
        new_tax_table.add_row([TWELVE_TO_FIFTEEN_LAKH, TWENTY_PERCENT_RANGE, (THREE_LAKHS * 0.2)])
        new_tax_table.add_row([GREATER_THAN_FIFTEN_LAKH, THIRTY_PERCENT_RANGE, (pending_amount * 0.3)])

        return three_lakh_bracket + (THREE_LAKHS * 0.1) + (THREE_LAKHS * 0.15) + (THREE_LAKHS * 0.2) + (pending_amount * 0.3)

    elif taxable_amount >= TWELVE_LAKHS and taxable_amount <= FIFTEEN_LAKHS:
        pending_amount = taxable_amount - TWELVE_LAKHS

        new_tax_table.add_row([THREE_TO_SIX_LAKH, FIVE_PERCENT_RANGE, three_lakh_bracket])
        new_tax_table.add_row([SIX_TO_NINE_LAKH, TEN_PERCENT_RANGE, (THREE_LAKHS * 0.1)])
        new_tax_table.add_row([NINE_TO_TWELVE_LAKH, FIFTEN_PERCENT_RANGE, (THREE_LAKHS * 0.15)])
        new_tax_table.add_row([TWELVE_TO_FIFTEEN_LAKH, TWENTY_PERCENT_RANGE, (pending_amount * 0.2)])

        return three_lakh_bracket + (THREE_LAKHS * 0.1) + (THREE_LAKHS * 0.15) + (pending_amount * 0.2)

    elif taxable_amount >= NINE_LAKHS and taxable_amount <= TWELVE_LAKHS:
        pending_amount = taxable_amount - NINE_LAKHS

        new_tax_table.add_row([THREE_TO_SIX_LAKH, FIVE_PERCENT_RANGE, three_lakh_bracket])
        new_tax_table.add_row([SIX_TO_NINE_LAKH, TEN_PERCENT_RANGE, (THREE_LAKHS * 0.1)])
        new_tax_table.add_row([NINE_TO_TWELVE_LAKH, FIFTEN_PERCENT_RANGE, (pending_amount * 0.15)])

        return three_lakh_bracket + (THREE_LAKHS * 0.1) + (pending_amount * 0.15)

    elif taxable_amount >= SIX_LAKHS and taxable_amount <= NINE_LAKHS:
        pending_amount = taxable_amount - SIX_LAKHS

        new_tax_table.add_row([THREE_TO_SIX_LAKH, FIVE_PERCENT_RANGE, three_lakh_bracket])
        new_tax_table.add_row([SIX_TO_NINE_LAKH, TEN_PERCENT_RANGE, (pending_amount * 0.1)])

        return three_lakh_bracket + (pending_amount * 0.1)

    elif taxable_amount >= THREE_LAKHS and taxable_amount <= SIX_LAKHS:
        pending_amount = taxable_amount - THREE_LAKHS

        new_tax_table.add_row([THREE_TO_SIX_LAKH, FIVE_PERCENT_RANGE, (pending_amount * 0.05)])

        return (pending_amount * 0.05)    


def check_user_input(input, type):
    try:
        val = int(input)
    except ValueError:
        if type == 'salary':
            print("Invalid value. Value should not be alphanumerc, decimal, comma, dash.")
        else:
            print("Invalid value. Value cannot exceed more than 5 lakhs.")
        sys.exit(1)


def main():
    total_salary = input("Enter total salary: ")
    check_user_input(total_salary, 'salary')

    deductions = input("Enter deductions: ")
    check_user_input(deductions, 'deductions')

    old_taxslab_taxable_income = int(total_salary) - STANDARD_DEDUCTION - int(deductions)
    new_taxslab_taxable_income = int(total_salary) - STANDARD_DEDUCTION

    tax_old_slab = old_regime(old_taxslab_taxable_income)
    tax_new_slab = new_regime(new_taxslab_taxable_income)

    # print('\n')
    # print(new_tax_table)
    # print(f"Tax amount as per new regime: {format(round(tax_new_slab), ',')}\n")

    # print(old_tax_table)
    # print(f"Tax amount as per old regime: {format(round(tax_old_slab), ',')}\n")

    if tax_old_slab >= tax_new_slab:
        # print(f"You should opt for New Tax Regime.\n")
        file_data = "You should opt for New Tax Regime."
    else:
        # print(f"You should opt for Old Tax Regime.\n")
        file_data = "You should opt for Old Tax Regime."

    with open(FILENAME, 'w') as f:
        f.write(str(new_tax_table) + '\n')
        f.write(f"Tax amount as per new regime: {format(round(tax_new_slab), ',')}" + '\n\n')
        f.write(str(old_tax_table) + '\n')
        f.write(f"Tax amount as per old regime: {format(round(tax_old_slab), ',')}" + '\n\n')
        f.write(file_data)
        print(f"{FILENAME} created.")

clear(1)
main()
