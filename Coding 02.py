##############################################
# Name: Kaden Eckhart
# Assignment: Coding 02
# Purpose: Calculate compound interest from user inputs.
# Notes: Formula I used for compund interest is A=P(1+r/n)**nt
# this is referenced in the notes for various formulas.
##############################################

#Formula I used for compund interest is A=P(1+r/n)**nt

#asking user for principal
principal = input('Initial Deposit?', )

#asking user for interest rate
rate = input('Interest Rate? (AS DECIMAL)', )

#asks user for number of times compounded
number_comp = input('How many times a year will it be compounded?', )

years = input('How many years will this money be in saving for?', )

rate_compounded=1.0+float(rate)/float(number_comp)

compunded_years=float(number_comp)*float(years)

savings_output=float(principal)*rate_compounded**compunded_years


print(savings_output)
