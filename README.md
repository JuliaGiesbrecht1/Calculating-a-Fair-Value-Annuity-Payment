# Calculating-a-Fair-Value-Annuity-Payment
- Case study of an insurance company that sells annuities to individuals and organizations. Created a tool using Python to find the fair amount for the monthly payments.

 - In Theory, a sales team would enter the customer's cash flows, the term of the annuity, and the inflation factor and instantly get the monthly annuity amount by using a bisection search.

- p4_create_dense_files.py is a program that takes the given test case files and produces two files that includes the data and also has entries for all the implied data for the "missing" months.

- p4_search_annuity.py is a program that uses bisection search to find the correct beginning year's monthly annuity payment in US dollars.

- p4_test1_cash_flows.csv is a 2-column csv-file with the first column being the month number (number of months from now) and the amount of the cash flow in US dollars

- p4_test1_interest_rates.csv shows the term interest rates for maturities at each month. This is a 2-column csv-file with the first column being the month number (number of months from now) and the percentage annualized interest rate between now and that month.

- p4_test1_terms.csv is the terms of the annuity. It has entries for the number of months of payments and the inflation adjustment percentage to adjust up the payments every year.
