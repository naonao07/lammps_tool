import pandas as pd
import matplotlib.pyplot as plt

# .datファイルを読み込む。最初の3行と4行目（メタデータ行）をスキップし、スペース区切りでデータを読み込む
df_liquid_dat = pd.read_csv('liquid_density.dat', sep='\s+', skiprows=4, header=None, names=['ChunkID', 'x', 'y', 'Ncount', 'density/mass'])

# x座標、y座標、density/massの値を準備
x_dat = df_liquid_dat['x'].values
y_dat = df_liquid_dat['y'].values
z_dat = df_liquid_dat['density/mass'].values

# x座標とy座標を入れ替えて2次元コンター図をプロット
plt.figure(figsize=(10, 6))
contour_dat = plt.tricontourf(y_dat, x_dat, z_dat, levels=14, cmap="viridis")
plt.colorbar(contour_dat, label='density/mass')
plt.xlabel('y')  # xとyのラベルを入れ替え
plt.ylabel('x')  # xとyのラベルを入れ替え
plt.title('liquid density profile')
plt.show()