def palindrome_product(input_length):
    first_num=int('9'*input_length)
    second_num=first_num
    greatest_palindrome_product=0
    for j in range(1,first_num+1):
        for k in range(1,second_num+1):
            product=k*j

            if str(product)==str(product)[::-1]:
                if greatest_palindrome_product>product:
                    pass
                else:
                    greatest_palindrome_product=product

            else:
                pass
    return greatest_palindrome_product

# driver code

print(palindrome_product(3))