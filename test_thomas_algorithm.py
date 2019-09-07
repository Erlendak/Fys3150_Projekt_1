from thomas_algorithm import *
import nose.tools as nt

def test_n_lesser_than_3():
    """
    Test if program crash if we use a n<3, The method does not support
    n smaller than 3.
    """
    test_n = [-5,-1,0,0.5,1,2]
    for i in test_n:
        try:
            ThomasAlgorithm(i)
            raise SyntaxError('''Error code does not run as,
            intended, the code does not crash for n lesser than 3.''')
        except ValueError:
            pass

def test_irrational_tuples_nummbers():
    """
    Test if program crash if we try to use irrational tuples_nummbers
    and tuples for n to setup a n x n matrix.
    """
    test_n = [np.pi, 10/6*10, np.sqrt(10),(14,13),[15,14],np.array([24,3,4])]
    for i in test_n:
        try:
            ThomasAlgorithm(i)
            raise SyntaxError('''Error code does not run as,
            intended, the code does not crash for unsupported n.''')
        except TypeError:
            pass
        except ValueError:
            pass

def test_accuracy():
    """
    Checks that the algorithm is as accurat as expected,
    for a large n.
    """
    tol = 10e-5
    test = ThomasAlgorithm(1000000)
    success = test._error() < tol
    assert success,"Thomas algorithm is not as accurat as expected."

if __name__ == '__main__':
    test_n_lesser_than_3()
    test_irrational_tuples_nummbers()
    test_accuracy()
