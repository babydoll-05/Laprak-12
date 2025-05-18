list_data_a = ['red', 'green', 'blue']
list_data_b = ['#FF0000','#008000','#0000FF']
dictio = dict()
for key, value in zip(list_data_a, list_data_b):
    dictio[key] = value
print(dictio)