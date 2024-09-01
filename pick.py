import compress_pickle import load
loaded_data = pickle.load('similarity.pkl', compression='gzip')

print(loaded_data)
