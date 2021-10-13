import pickle

some_data = ["a list", "containing", 5, "values including another list", ['inner', 'list']]


with open("pickled_list", 'wb') as file:
    pickle.dump(some_data, file)

with open("pickled_list", 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)
assert some_data == loaded_data
print('done, nothing wrong')