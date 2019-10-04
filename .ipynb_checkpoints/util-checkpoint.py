def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='latin1')
    return dict

def translateDicc():
    return ['avión', 'auto', 'pájaro',
            'gato', 'ciervo', 'perro',
            'rana', 'caballo', 'barco',
            'camión']

from numpy import min, max, zeros

def customNormalize(in_np_arr):
    min_val = min(in_np_arr)
    max_val = max(in_np_arr)
    return (in_np_arr-min_val)/(max_val-min_val)