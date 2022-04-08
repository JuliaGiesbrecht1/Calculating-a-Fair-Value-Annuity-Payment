#!/usr/bin/env python
# coding: utf-8

# In[2]:


### Calculating a Fair Value Annuity Payment ###

from math import e

test_case = 1

cash_flow_file = open(f'p4_test{test_case}_dense_cf.csv', 'r') # Reading in the dense file for cashflow
interest_rate_file = open(f'p4_test{test_case}_dense_rates.csv', 'r') # Reading in the dense file for interest rates


# Finding annuity terms and inflation value.
terms_file = open(f'p4_test{test_case}_terms.csv','r') # Finding the annuity terms
terms_file.readline()  # skip the first line of column titles
line = terms_file.readline()  # this is the line with the numbers, e.g., '120,3.0'
annuity_term, inflation = line.split(',')  # split into our two values (as strings), e.g., '120', '3.0'
annuity_term = int(annuity_term)  # convert to an integer from a string
inflation = float(inflation) / 100.0  # convert to a float and ratio from a string with percent number
terms_file.close()


# Reading in dense files. Cashflow and interest rates.
months = 1
cf_npv= 0.0 # sum of npv of customer cashflow (present dollars before interest)
total = 0.0 # sum of cashflow from customer (future dollars) 

for cash_flow_line, interest_rate_line in zip(cash_flow_file, interest_rate_file):     
    interest_rate = float(interest_rate_line)/12.0/100.0 # IR per month into decimal 
    cash_flow = float(cash_flow_line)
    total += cash_flow  
    cf_npv += cash_flow * e ** (-interest_rate * months) # 𝑛𝑝𝑣=∑𝑛𝑖=0𝑝𝑣𝑖 finding sum of present dollars
    months += 1   
cash_flow_file.close()


print('Total customer-provided cash flows: $%.2f' % total)
print('NPV of customer-provided cash flows: $%.2f' % cf_npv)
print('\nSearching for correct beginning monthly annuity payment:')

# Bisection search variables
low = 0.0
high = total # High starts at the sum of all cashflows from customer in future dollars.
mid = (low + high)/2 # 'mid' value == 'guess' annunity payment to customer.
epsilon = 0.1 # Assuming that error of 10 cents is acceptable.

payments = 0.0 # Sum of annuity payments (today's dollars) for each guess/mid value.
iter_count = 1 # Counting how many times we guess until npv == ~ 0.
npv = 1 # Initial value must be greater that epsilon to enter while loop. Want npv to == ~ 0.
total_annuity = 0.0 # Sum of all annuity payments to customer.

while abs(npv) > epsilon: # If abs(npv) greater than epsilon (True) must keep guessing. npv not yet close enough to zero.
    mid = (low + high)/2 
    mid = round(mid, 2)
    npv = cf_npv   
    interest_rate_file = open(f'p4_test{test_case}_dense_rates.csv', 'r') # Opening interest rate file for each loop
    inflation_factor = 1.0
    months = 1
    total_annuity = 0.0
    
    
    for interest_rate in interest_rate_file:
        interest_rate = float(interest_rate)/12.0/100.0 
        payments += (mid * e ** (-interest_rate * (months))) * inflation_factor 
        total_annuity += (mid*inflation_factor)
        
        if months % 12 == 0: 
            inflation_factor = inflation_factor * (1 + inflation)     
          
        months+=1
        
    npv -= payments 
   
    
    payments = 0.0
    interest_rate_file.close()
            
    print(f'{str(iter_count)} : annuity {mid} NPV is {round(npv,2)}')
    iter_count += 1
    
    if npv < 0.0: # If npv less than zero, customer is being paid too much, greater than zero, not enough
        high = mid # guess/mid is too low, now the high value becomes the guess/mid value  
    else:
        low = mid # guess/mid is too high
        
    
        
for i in range(1, annuity_term + 1, 12): 
    if i == 1:
        print(f'First year pay ${round(mid,2)} per month')
    else:
        print(f'Next year pay ${round(mid,2)}  per month')
    mid = mid * (1 + inflation)
        
print(f'For a total of {round(total_annuity,2)}')

    
    


# In[ ]:




