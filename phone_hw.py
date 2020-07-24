
### DATA LAYER
p_1_name  = "iPhone IX"
p_1_price = 1000
p_1_q     = 3   #int
p_1_ava   = True

p_2_name  = "iPhone X"
p_2_price = 2000
p_2_q     = 0   #int
p_2_ava   = False

p_3_name  = "Xiaomi MIA1"
p_3_price = 200 
p_3_q     = 15
p_3_ava   = True

### LOGIC LAYER
p_total_q = p_1_q + p_2_q + p_3_q
p_total_c = p_1_q * p_1_price + p_2_q * p_2_price + p_3_q * p_3_price
p_total_ava = p_1_ava and p_2_ava and p_3_ava

### PRESENTATION LAYER

print( "★" * 30)
print( " TOTAL PHONES: " + str(p_total_q)) 
print( " TOTAL WORTH: " + str(p_total_c)) 
print( " IS " + p_1_name + " AVAILABLE?\n\t " + str(p_1_ava) )
print( " IS " + p_2_name + " AVAILABLE?\n\t " + str(p_2_ava) )
print( " IS " + p_3_name + " AVAILABLE?\n\t " + str(p_3_ava) )
print( "ARE ALL AVAILABLE?\n\t" + str(p_total_ava))  
print( "★" * 30) 
 