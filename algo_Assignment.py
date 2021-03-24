## divide-and-conquer algorithm for karatsuba integer multiplication   

# function multiply(x, y)
# Input: Positive integers x and y,
# Output: Their product
# n = max(size of x, size of y)
# if n = 1: return xy
#
# xL, xR = leftmost dn/2e, rightmost bn/2c  of x
# yL, yR = leftmost dn/2e, rightmost bn/2c of y
# P1 = multiply(xL, yL)
# P2 = multiply(xR, yR)
# P3 = multiply(xL + xR, yL + yR)
# return P1 × 2
# n + (P3 − P1 − P2) × 2
# n/2 + P

##-------------------------------------------------------------------------------------------
# def multiply_integers(num1 , num2):
    
#     ## base condition
#     if len(str(num1)) == 1 or len(str(num2)) == 1:
#         return num1*num2
#     ## Recursive condition
#     else:

#         x = max(len(str(num1)), len(str(num2))  )

#         xby2 = x / 2

#         a = num1 / 10**(xby2)
#         b = num1 % 10**(xby2)
#         c = num2 / 10**(xby2)
#         d = num2 % 10**(xby2)

#         ac = multiply_integers(a,c)
#         bd = multiply_integers(a,d)
#         ad_plus_bc = multiply_integers(( a + b , c + d)) - ac - bd 

#         ## writing n as 2*nby2 takes care of both even and odd n
#         result = ac * 10**(2*xby2) + (ad_plus_bc * 10**xby2) + bd 

#         return result

# calling a fucntion 

# e = multiply_integers(9,12)
# print(e)

#--------------------second method for multiplication of integres------------------------------------------

def multiply_integers(num1 , num2):
        
    ## Base condtion 
    if len(str(num1)) == 1 or len(str(num2)):
        return num1 * num2
    
    # Calculate length of integers
    num1 = str(num1)
    num2 = str(num2)
    len_num1 = len(num1)
    len_num2 = len(num2)
    
    
    ## 'ceil' halves used for combining parts
    nby2 = len_num1//2 + 1 if len_num1 % 2 == 1 else len_num1//2
    mby2 = len_num2//2 + 1 if len_num2 % 2 == 1 else len_num2//2
    
    # halving multiplier and multiplicand into a,b and c,d...this where we are getting the pairs
    #   using 'floor' halves of lengths
    a , b = num1[ : len_num1 // 2] , num1[len_num1 // 2 : ]
    c , d = num2[ : num2 // 2] , num2[num2 // 2 : ]
    
    # recursively multiply ac, ad, bc and bd...this is where we multiply 
        #the pairs form from the step above
    ac , ad = multiply_integers(int(a) , int(c)) , multiply_integers(int(a) , int(d))
    bc , bd = multiply_integers(int(b) , int(c)) , multiply_integers(int(b) , int(d))
     
     # combine adding zeros and return.... this is where summation addition of zeros occur
    summation = ac * 10**(nby2 + mby2)
    summation += ad * 10**(nby2)
    summation += bc * 10**(mby2)
    summation += bd
    
    return summation
    
    

if __name__ == "__main__":
    x = multiply_integers(18 , 2)
    print(x)
