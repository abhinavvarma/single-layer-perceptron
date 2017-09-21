import re
from operator import mul

import distribution


def compute_true_value_for_threshold_fn(X, coefficients, threshold):
    return [int(sum(map(mul, x, coefficients)) >= threshold) for x in X]


def boolean_operation(num1, num2, operator):
    if operator == 'OR':
        return num1 or num2
    elif operator == 'AND':
        return num1 and num2


def compute_true_value_for_nbf(X, sign_indexes, operations):
    y = []
    for x in X:
        nums = list(map(
                   lambda i: (1 if i > 0 else -1) * x[abs(i) - 1],
                    sign_indexes))
        num1 = nums[0]
        for i in range(len(operations)):
            num2 = nums[i + 1]
            num1 = boolean_operation(num1, num2, operations[i])
        y.append(num1)
    return y


def find_max_vars(indices_with_sign):
    return max(map(abs, indices_with_sign))


def nbf(lines, num_train, num_test):
    indices_with_sign = list(map(int, re.findall("[+|-]?\d+", lines[1])))
    boolean_operations = re.findall("\w\w+", lines[1])

    n = find_max_vars(indices_with_sign)

    X_train = [distribution.ALLOWED_DISTRIBUTIONS['bool'](n)
               for i in range(num_train)]
    y_train = compute_true_value_for_nbf(X_train, indices_with_sign, boolean_operations)

    X_test = [distribution.ALLOWED_DISTRIBUTIONS['bool'](n) for i in range(num_test)]
    y_test = compute_true_value_for_nbf(X_test, indices_with_sign, boolean_operations)
    return X_train, y_train, X_test, y_test


def tf(lines, distribution, num_train, num_test):
    threshold = int(lines[1])
    coefficients = map(int, lines[2].split(" "))

    n = len(coefficients)
    X_train = [distribution(n)
               for i in range(num_train)]
    y_train = compute_true_value_for_threshold_fn(X_train, coefficients, threshold)

    X_test = [distribution(n)
              for i in range(num_test)]
    y_test = compute_true_value_for_threshold_fn(X_test, coefficients, threshold)
    return X_train, y_train, X_test, y_test


def parse(ground_file, distribution, num_train, num_test):
    with open(ground_file) as f:
        lines = f.read().split("\n")
        name = lines[0]

        if name == "NBF":
            return nbf(lines, num_train, num_test)
        elif name == "TF":
            return tf(lines, distribution, num_train, num_test)
        else:
            print "NOT PARSABLE"