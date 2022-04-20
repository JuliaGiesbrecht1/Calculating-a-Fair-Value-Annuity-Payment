

#### INTEREST RATE DENSE ####

test_case = 1

sparse_rates_filename  = open(f'p4_test{test_case}_interest_rates.csv', 'r') #reading in sparse file
dense_rates_filename = open(f'p4_test{test_case}_dense_rates.csv', 'w') # writing the dense file


annuity = open(f'p4_test{test_case}_terms.csv','r')
for line in annuity:
    term, inflation = line.split(',')
term = int(term)


month = 1
prev_amount = 0

for line in sparse_rates_filename:
    ir_month, ir_amount = line.split(',')
    ir_month = int(ir_month)  # convert the string cf_month into an integer
    ir_amount = float(ir_amount)  # convert the string cf_amount into a float
   
    while month < ir_month:
        dense_rates_filename.write(str(prev_amount) + '\n')  
        month += 1
    dense_rates_filename.write(str(ir_amount) + '\n') 
    month += 1
    prev_amount = ir_amount
    
while month <= term:  
    dense_rates_filename.write(str(prev_amount) + '\n')
    month += 1
sparse_rates_filename.close()
dense_rates_filename.close()
annuity.close()




#### CASH FLOW DENSE ####

test_case = 1

sparse_cf_filename = open(f'p4_test{test_case}_cash_flows.csv', 'r')#reading in sparse file
dense_cf_filename = open(f'p4_test{test_case}_dense_cf.csv', 'w')  #writing the dense file

annuity = open(f'p4_test{test_case}_terms.csv','r')
for line in annuity:
    term, inflation = line.split(',')
term = int(term)


month = 1


for line in sparse_cf_filename:
    cf_month, cf_amount = line.split(',')
    cf_month = int(cf_month)  # convert the string cf_month into an integer
    cf_amount = float(cf_amount)  # convert the string cf_amount into a float
    while month < cf_month:
        dense_cf_filename.write(str(0.0) + '\n')  # no cash flows for this month
        month += 1
    dense_cf_filename.write(str(cf_amount) + '\n') # here's the cash flow month
    month += 1
    
    
while month <= term:  # any later months until the end of the annuity term after last cash flow
    dense_cf_filename.write(str(0.0) + '\n')
    month += 1
sparse_cf_filename.close()
dense_cf_filename.close()
annuity.close()




