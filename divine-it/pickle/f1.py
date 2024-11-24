import pickle

data = [1, 2, 3, 4, 5, 6]

serialized_data = pickle.dumps(data)

print(serialized_data)

deserialized_data = pickle.loads(serialized_data)

print(deserialized_data)
