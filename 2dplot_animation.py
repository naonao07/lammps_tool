import pandas as pd
import matplotlib.pyplot as plt
import imageio
import glob


i = 0
for i in range(0,10):
    filename='liquid_density_' + str(i) + '.dat'
    outputname='liquid_density_' + str(i) + '.png'
    print(filename)
# .datファイルを読み込む。最初の3行と4行目（メタデータ行）をスキップし、スペース区切りでデータを読み込む
    df_liquid_dat = pd.read_csv(filename, sep='\s+', skiprows=4, header=None, names=['ChunkID', 'x', 'y', 'Ncount', 'density/mass'])

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
    timestep=(i*0.1)
    rounded_num = round(timestep, 2)
    plt.text(-65,15, str(rounded_num) + "ps" , fontsize=12, color='white', ha='left', va='top')
    plt.savefig(outputname)
    #plt.show()



filenames = sorted(glob.glob('liquid_density_*.png'))  # 'sorted' でファイル名を順番に並べる

# GIF として保存するための画像データを読み込む
images = []
for filename in filenames:
    images.append(imageio.v2.imread(filename))

# GIF アニメーションとして保存
imageio.mimsave('animation.gif', images, fps=2)  # fps は秒間フレーム数

print("Finish")
