#!/usr/bin/python
from datetime import date
from money import Money
from dateutil.relativedelta import relativedelta
from decimal import Decimal
import findates
from Contract import LoanContract
import LoanCalculator

print("Standard Payments")
my_contract = LoanContract()
my_contract.set_events({"kickstarter_success":True,
                        "kickstarter_start_date": date(2015,1,1),
                        "kickstarter_payment_date":date(2015,1,15),
                        "kickstarter_revenue":50000,
                        "early_payments":[]})
calculator = LoanCalculator.LoanCalculator()
calculator.show_payments(my_contract)
print
print ("Kickstarter success")
my_contract.set_events({"kickstarter_success":True,
                        "kickstarter_start_date": date(2015,1,1),
                        "kickstarter_payment_date":date(2015,1,15),
                        "kickstarter_revenue":100000,
                        "early_payments":[]})
calculator = LoanCalculator.LoanCalculator()
calculator.show_payments(my_contract)
