__author__ = 'Christian Dansereau'

import cPickle
import gzip
import numpy

def load_data():
    with gzip.open('mnist.pkl.gz', 'rb') as f:
        train_set, valid_set, test_set = cPickle.load(f)

    train_X, train_y = train_set

    # Whatever else needs to be done

def one_hot_encode(y, num_classes):
    print y

while abs(x_new - x_old) > precision:
    x_old = x_new
    x_new = x_old - eps * f_prime(x_old)
    print("Local minimum occurs at", x_new)

if __name__ == "__main__":
    # my code here
    load_data()

