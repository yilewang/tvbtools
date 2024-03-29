# import h5py
# import numpy as np
# import matplotlib.pyplot as plt
# from pactools import Comodulogram, REFERENCES
# import pandas as pd
# import seaborn as sns
# from signaltools import SignalToolkit
# df = pd.read_excel('/Users/yat-lok/workspaces/data4project/mega_table.xlsx', sheet_name='tvb_parameters')
# groups = ['SNC', 'NC', 'MCI', 'AD']

# def comodulograms(signal, fs=1024, low_fq_width=1.0, low_fq_range=np.linspace(1,10,50), methods='tort'):
#     # Compute the comodulograms and plot them
#     print('%s... ' % (methods, ))
#     estimator = Comodulogram(fs=fs, low_fq_range=low_fq_range,
#                                 low_fq_width=low_fq_width, method=methods,
#                                 progress_bar=False)
#     estimator.fit(signal)
#     estimator.plot()
#     plt.show()
#     return estimator.comod_





# # signal_left_filtered = SignalToolkit.sos_filter(signal_left, [2,100], fs=81920)
# # signal_right_filtered = SignalToolkit.sos_filter(signal_right, [2,100], fs=81920)
# mat = comodulograms(signal_left)
# fig, ax = plt.subplots()
# ax = sns.heatmap(mat.T)
# ax.invert_yaxis()