def f_x(x):
    return x**2

def derivative_f_x_first(f_x, x, epsilon):
    return (f_x(x+epsilon) - f_x(x))/ epsilon

def derivative_f_x_second(f_x, x, epsilon):
    if(callable(f_x)):
        return (f_x(x+epsilon) - f_x(x))/ epsilon
    else:
        return 0


def newtons_method(f_x, x_init, epsilon):
    curr_val = x_init
    next_val = x_init
    difference = 0
    # while the difference is small
    while (difference > epsilon) :
        first_derivative = derivative_f_x_first(f_x, x, epsilon)
        second_derivative = derivative_f_x_first(first_derivative, x, epsilon)

        next_val = curr_val - (first_derivative(curr_val)/second_derivative(curr_val))
        difference = math.abs(next_val-curr_val)
        curr_val = next_val
    return curr_val

if __name__ == '__main__':
    epsilon = 0.1 #not sure what this should be
    x_init = 2;
    # first_der = derivative_f_x_first(f_x, x_init, epsilon)
    # print("first_der", first_der)
    # second_der = derivative_f_x_second(first_der, x_init, epsilon)
    # print("second_der", second_der)
    print(newtons_method(x_init, f_x, epsilon))
    