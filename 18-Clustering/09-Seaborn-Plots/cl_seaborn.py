import sklearn.datasets as ds
import seaborn as sn
import matplotlib.pyplot as plt

data = ds.load_iris(as_frame=True)

target = data['target']
target_names = data['target_names']

df = data['data']
df['species_index'] = target
df['species'] = target.map(lambda n: target_names[n])

print(df)

sn.pairplot(df, height=2, hue="species", palette="husl", aspect=1)

plt.show()