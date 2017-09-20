import sys
import activation
import distribution
import inputfileparser
from updaterules import AVAILABLE_UPDATE_RULES


def perceptron(x, w, activation, theta):
    '''Takes an input, weights
    applies an activation on the linear product of inputs and weights
    and returns 1 if the output of activation is greater than theta
    if not it returns 0 '''

    linear_sum = sum(i*j for i, j in zip(x, w))

    if activation(linear_sum, theta) >= theta:
        return 1
    else:
        return 0


def train(X_train, y_train):
    ''' Training the perceptron to find the most ideal weights or parameters
    Returns the best W and theta'''

    w = [1] * len(X_train[0])
    error = 0
    theta = 0
    for i in range(num_train):

        y_predicted = perceptron(X_train[i], w, activation_func, theta)
        y_true = y_train[i]
        if y_predicted != y_true:
            error = error + 1
        w, theta = update_rule(y_true, y_predicted, X_train[i], w, theta=theta)

    return w, theta


def test(X_test, y_test, w, theta):
    '''Uses the precomputed w and theta and
     tests the performance on the test data'''

    total_error = 0
    for x, y_true in zip(X_test, y_test):
        y_predicted = perceptron(x, w, activation_func, theta)

        err = abs(y_predicted - y_true)
        total_error = total_error + err
        print x, ":", y_predicted, ":", y_true, ":", err

    avg_error = float(total_error) / num_test

    print sys.argv
    print "Total error :", total_error
    print "average error", ":", round(avg_error, 4)
    print "epsilon : ", epsilon
    if avg_error <= epsilon:
        print "Training success"
    else:
        print "Training fail"

if __name__ == "__main__":
    activation_name = sys.argv[1]
    update_name = sys.argv[2]
    ground_file = sys.argv[3]
    distribution_type = sys.argv[4]
    num_train = int(sys.argv[5])
    num_test = int(sys.argv[6])
    epsilon = float(sys.argv[7])
    update_rule = AVAILABLE_UPDATE_RULES[update_name]
    activation_func = activation.ALLOWED_TYPES[activation_name]
    distribution_sampler_function = distribution.ALLOWED_DISTRIBUTIONS[distribution_type]

    X_train, y_train, X_test, y_test = inputfileparser.parse(ground_file, distribution_sampler_function, num_train, num_test)
    w, theta = train(X_train, y_train)
    test(X_test, y_test, w, theta)
