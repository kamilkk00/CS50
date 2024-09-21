from tabulate import tabulate
import sys


def main():
    score = 0
    what_currency = "Yes"

    debt = int(input ("\nHow much does your company want to borrow?\n"))
    company_country = input("What is the name of the country where the company operates?\n").upper()
    try:
        central_bank = float(input("What is the interest rate of the central bank of that country in percent?\n"))
    except ValueError:
        print("Interest rates must be number")
        sys.exit(1)
    interest_bank = central_bank
    
    currency_name = input("In which currency does your company want to take debt?\n").upper()
    with_currency = input("Does your company want to take the debt in the local currency? (yes/no)\n").lower()
    if 'n' in with_currency:
        central_bank = float(input("What is the interest rate of the central bank of that country in percent?\n"))
        what_currency = "No"
        interest_bank = central_bank + 2

    rating_company = input("What is the investment rating of your company?\n").upper()
    score_rating = rating(rating_company)

    maturity_years = int(input("What is the maturity of the debt your company wants to issue (in years)?\n"))
    score_maturity = maturity(maturity_years)

    score += score_rating + score_maturity + interest_bank

    interest = int (total_cost(debt, score, maturity_years))

    total = debt + interest

    if maturity_years == 1:
        x = "year"
    else:
        x = "years"

    print("\n\nIn the table below, you can find all important information and the optimal interest rates for this company:")
    data=[
        ["Company country", company_country],
        ["Currency of debt", currency_name],
        ["Central Bank interest rate", f"{central_bank}%"],
        ["Debt in local currency", what_currency],
        ["Company rating", rating_company],
        ["Maturity", f"{maturity_years} {x}"],
        ["Optimal interest rate", f"{score}% per year"],
        ["Amount of Debt", debt],
        ["Interest", interest],
        ["Total amount to repay", total]
    ]
    table = tabulate(data, headers=["Desciption", "Value"], tablefmt="grid")
    print(table)


def total_cost(debt, score, maturity_years):
    interest = debt * (score / 100) * maturity_years
    return interest

def rating(rating_company):
    interest = 0
    if 'AAA' in rating_company:
        interest += 1
    elif 'AA' in rating_company:
        interest += 1.5
    elif 'A' in rating_company:
        interest += 2.5
    elif 'BBB' in rating_company:
        interest += 4
    elif 'BB' in rating_company:
        interest += 5.5
    elif 'B' in rating_company:
        interest += 8
    elif 'CCC' in rating_company:
        interest += 12
    elif 'CC' in rating_company:
        interest += 16
    elif 'C' in rating_company:
        interest += 18
    elif 'D' in rating_company:
        interest += 20

    return interest


def maturity(maturity_years):
    interest = 0
    if maturity_years >= 1:
        if maturity_years >= 5:
            if maturity_years >= 10:
                if maturity_years >= 20:
                    interest = 4
                else:
                    interest = 3
            else:
                interest = 2
        else:
            interest = 1
    return interest


if __name__ == "__main__":
    main()
