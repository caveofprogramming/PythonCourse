import sklearn.datasets as ds

data = ds.load_iris(as_frame=True)

target = data['target']
target_names = data['target_names']

df = data['data']
df['species_index'] = target
df['species'] = target.map(lambda n: target_names[n])

print(df)