def my_lambda_wrapper(n):
    # n is the value passed while calling my_lambda_wrapper
    return lambda x: x + n

if __name__ == '__main__':
    x = 0
    my_lambda_fn = lambda x: x + 1
    my_second_lambda_fn = my_lambda_wrapper(2)
    print(f'Output 1: {my_lambda_fn(x)} \nOutput 2: {my_second_lambda_fn(3)}') # 3 is the value of x in the my_lambda_wrapper function