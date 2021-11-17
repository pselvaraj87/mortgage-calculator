import numpy as np


def calculate_pmi_rate(credit_score):

    pmi_rate = 0

    if credit_score < 640:
        pmi_rate = 2.25
    elif 639 < credit_score < 660:
        pmi_rate = 2.05
    elif 659 < credit_score < 680:
        pmi_rate = 1.90
    elif 679 < credit_score < 700:
        pmi_rate = 1.40
    elif 699 < credit_score < 720:
        pmi_rate = 1.15
    elif 719 < credit_score < 740:
        pmi_rate = 0.95
    elif 739 < credit_score < 760:
        pmi_rate = 0.75
    elif credit_score > 760:
        pmi_rate = 0.55

    return pmi_rate


if __name__ == '__main__':
    home_price = float(input('Enter home price($): '))
    interest_rate = float(input('Enter interest rate(%): '))
    loan_duration = int(input('Enter loan duration(years): '))
    credit_score = int(input('Enter credit score: '))

    stock_appreciation = float(input('Enter stock appreciation(%): '))

    for money_down in range(5, 21):
        loan_principal = (1 - money_down/100) * home_price
        monthly_payment = loan_principal * (interest_rate/12) / (1 - (1 + (interest_rate/12)) - loan_duration*12)

        money_to_invest = (0.2 - money_down / 100) * home_price
        stock_return = money_to_invest * pow((1 + stock_appreciation / 100), loan_duration)

        if money_down < 20:
            pmi_rate = calculate_pmi_rate(credit_score)
            pmi_monthly = loan_principal*pmi_rate/loan_duration/12
            monthly_payment += pmi_monthly

            stock_return -= pmi_monthly*loan_duration*12

        print('For %i%% money down, down payment = %f, stock investment = %f\n' % (money_down, money_down/100*home_price,
                                                                                   stock_return))
