import sys
import activation
import distribution
import inputfileparser
from updaterules import AVAILABLE_UPDATE_RULES


def perceptron(x, w, activation, theta):
    linear_sum = sum(i*j for i, j in zip(x, w))
    if activation(linear_sum, theta) >= theta:
        return 1
    else:
        return 0

def train(X_train, y_train):
    w = [1] * len(X_train[0])
    error = 0
    theta = 0
    for i in range(num_train):
        y_predicted = perceptron(X_train[i], w, activation_function, theta)
        y_true = y_train[i]
        if y_predicted != y_true:
            error = error + 1
        w, theta = update_rule(y_true, y_predicted, X_train[i], w, theta=theta)
    return w, theta


def test(X_test, y_test, w, theta):
    total_error = 0
    for x, y_true in zip(X_test, y_test):
        y_predicted = perceptron(x, w, activation_function, theta)
        err = abs(y_predicted - y_true)
        total_error = total_error + err
        print x, ":", y_predicted, ":", y_true, ":", err

    avg_error = float(total_error) / num_test
    print "Total Error :", total_error
    print "Average Error", ":", round(avg_error, 4)
    print "Epsilon : ", epsilon
    if avg_error <= epsilon:
        print "TRAINING SUCCEEDED"
    else:
        print "TRAINING FAILED"

if __name__ == "__main__":
    activation_type = sys.argv[1]
    update_rule_type = sys.argv[2]
    ground_file = sys.argv[3]
    distribution_type = sys.argv[4]
    num_train = int(sys.argv[5])
    num_test = int(sys.argv[6])
    epsilon = float(sys.argv[7])
    opfilename = "-".join([val for val in sys.argv[1:]])
    # sys.stdout = open(opfilename+'.txt', 'w')
    update_rule = AVAILABLE_UPDATE_RULES[update_rule_type]
    activation_function = activation.ALLOWED_TYPES[activation_type]
    distribution_sampler_function = distribution.ALLOWED_DISTRIBUTIONS[distribution_type]
    X_train, y_train, X_test, y_test = inputfileparser.parse(ground_file, distribution_sampler_function, num_train, num_test)
    w, theta = train(X_train, y_train)
    test(X_test, y_test, w, theta)
