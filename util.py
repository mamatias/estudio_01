def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='latin1')
    return dict

def pickle(data, filename):
    import pickle
    file = open(filename, 'wb')
    pickle.dump(data, file)


def translateDicc():
    return ['avión', 'auto', 'pájaro',
            'gato', 'ciervo', 'perro',
            'rana', 'caballo', 'barco',
            'camión']

from numpy import min, max, zeros, argmax

def customNormalize(in_np_arr):
    min_val = min(in_np_arr)
    max_val = max(in_np_arr)
    return (in_np_arr-min_val)/(max_val-min_val)

def one_hot_enconde(lbls, n_classes = 10):
    tr = zeros((len(lbls), n_classes))
    for idx, val in enumerate(lbls):
        tr[idx][val] = 1
    return tr

def decodeOHE(oheArray):
    return translateDicc()[argmax(oheArray)]