import uproot

# Standard imports
import matplotlib.pyplot as plt
import numpy as np
import sys
import plotly.graph_objects as go

plt.rcParams['font.family'] = 'Times New Roman' #全体のフォントを設定
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.size'] = 22
plt.rcParams['axes.linewidth'] = 1.0# 軸の線幅edge linewidth。囲みの太さ
plt.rcParams['axes.grid'] = True
plt.rcParams["xtick.direction"] = "in"               #x軸の目盛線を内向きへ
plt.rcParams["ytick.direction"] = "in"               #y軸の目盛線を内向きへ
plt.rcParams["xtick.minor.visible"] = True           #x軸補助目盛りの追加
plt.rcParams["ytick.minor.visible"] = True           #y軸補助目盛りの追加
plt.rcParams["xtick.major.size"] = 10                #x軸主目盛り線の長さ
plt.rcParams["ytick.major.size"] = 10                #y軸主目盛り線の長さ
plt.rcParams["xtick.minor.size"] = 5                 #x軸補助目盛り線の長さ
plt.rcParams["ytick.minor.size"] = 5                 #y軸補助目盛り線の長さ
plt.rcParams['figure.subplot.left'] = 0.1
plt.rcParams['figure.subplot.right'] = 0.98
plt.rcParams['figure.subplot.top'] = 0.95
plt.rcParams['figure.subplot.bottom'] = 0.1


# プロット
fig = go.Figure()

width = 1

fig.add_trace(
    go.Bar(
        x=np.array([0, 1, 2, 3]),
        y=[1, 2, 3, 4],
        width= np.full_like(np.array([0, 1, 2, 3]), width),
        marker=dict(color='blue'),
        name="Histogram"
    )
)

fig.update_layout(
    title="Histogram from ROOT file",
    xaxis_title="Bin",
    yaxis_title="Counts",
    bargap=0.1
)

fig.show()

sys.exit()

file = uproot.open("../root/hodo_run00654_0.root")

hist = file["BHT_TDC_seg30U"] # TNameで取得
# ヒストグラムのデータを取得
hist_data = hist.to_numpy()

data = np.zeros_like(hist_data[0])

for i in range(63):
    hist = file["BHT_TDC_seg{}U".format(i)] # TNameで取得
    # ヒストグラムのデータを取得
    hist_data = hist.to_numpy()
    data += hist_data[0]


# x軸のビンエッジ、ビンの内容を取得
# bin_contents = hist_data[0]
bin_contents = data
bin_edges = hist_data[1]

# 中心値を取得するために、ビンエッジをビンの中心値に変換
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

# プロット
plt.hist(bin_centers, bins=bin_edges, weights=bin_contents, histtype='step', label="Histogram")

plt.xlabel("Bin")
plt.ylabel("Counts")
plt.title("Histogram from ROOT file")
plt.legend()
plt.show()



# x軸のビンエッジ、ビンの内容を取得
bin_contents = hist_data[0]
bin_edges = hist_data[1]

# プロット
fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=bin_edges[:-1],
        y=bin_contents,
        width=bin_edges[1:] - bin_edges[:-1],
        marker=dict(color='blue'),
        name="Histogram"
    )
)

fig.update_layout(
    title="Histogram from ROOT file",
    xaxis_title="Bin",
    yaxis_title="Counts",
    bargap=0.1
)

fig.show()

# import plotly.io as pio
# pio.write_html(fig, file='histogram.html', auto_open=True)