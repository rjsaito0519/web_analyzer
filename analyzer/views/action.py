from flask import Blueprint, request, jsonify
from analyzer import app, db
from analyzer.models.log import Log
from analyzer.models.mppc_data import MPPC_data
action_bp = Blueprint('action', __name__)

import numpy as np
from datetime import datetime
import uproot
import numpy as np


# fetch MPPC data
@action_bp.route('/_fetch_mppc_data')
def fetch_mppc_data():

    file = uproot.open("../root/hodo_run00654_0.root")

    hist_data = file["BHT_TDC_seg0U"].to_numpy()
    bin_values = np.zeros_like(hist_data[0])
    bin_edges = hist_data[1]
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
    bin_widths  = (bin_edges[1:] - bin_edges[:-1])

    for i in range(63):
        hist = file["BHT_TDC_seg{}U".format(i)] # TNameで取得
        # ヒストグラムのデータを取得
        hist_data = hist.to_numpy()
        bin_values += hist_data[0]

    return jsonify({"bin_centers": bin_centers.tolist(), "bin_widths": bin_widths.tolist(), "bin_values": bin_values.tolist()})