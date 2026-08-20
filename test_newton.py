import pytest
import numpy as np
import math

import newton

## Important: structure of tests assumes a dictionary with an 'x'
## key as the output. 

def test_basic_function():
    assert np.isclose(newton.newtons_method(np.cos, 2.95)['new x'], math.pi)

def test_bad_input():
    with pytest.raises(TypeError):   
        newton.newtons_method(2.95, np.cos )
    ## Ideally, our function would raise the exception with a useful message.
    with pytest.raises(TypeError, match='the first argument must be a function'):
        newton.newtons_method(2.95, np.cos )
    with pytest.raises(TypeError, match='x must be an numeric'):
        newton.newtons_method(np.cos, np.cos )

def test_derivatives():
    def f_x(x):
        return x**3 + (2 * x**2) + 1
    
    assert np.isclose(newton.derivative(f_x, 2), 20)
    assert np.isclose(newton.derivative_second(f_x, 2), 16, rtol=1e-03)

    def f_x2(x):
        return x**2
    
    assert np.isclose(newton.derivative(f_x2, 1), 2)
    assert np.isclose(newton.derivative_second(f_x2, 1), 2, rtol=1e-03)
    # assert np.isclose(newton.newtons_method(f_x2, 1)['new x'], 0, rtol=1e-1)

    def f_x3(x):
        return (x**2)*(-1)
    
    assert np.isclose(newton.derivative(f_x3, 1), -2)
    assert np.isclose(newton.derivative_second(f_x3, 1), -2, rtol=1e-03)
    # assert np.isclose(newton.newtons_method(f_x3, 1)['new x'], 0, rtol=1e-20)

# def test_inputs_are_valid():
#     def f_x(x):
#         return x**2

#     assert np.isclose(newton.newtons_method(f_x, 2)['new x'], 0, rtol=1e-03)
# How to check that a warning is (correctly) emitted:
# def test_warning():
#    with pytest.warns(UserWarning, match='greater'):
#        newton.optimize(...., ....)
