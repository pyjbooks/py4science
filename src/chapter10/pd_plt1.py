import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

# %% line plot
df = pd.DataFrame(np.random.randn(500, 3), columns=list('XYZ'),
                  index=pd.date_range('1/1/2016', periods=500))

df = df.cumsum()
ax = df.plot(colormap='gray', fontsize=14)
ax.set_ylabel('Value', fontsize=14)

# %% bar plot
df2 = pd.DataFrame(np.random.rand(5, 3),
                   columns=['a', 'b', 'c'])

df2.plot(kind='bar', stacked=True, colormap='gray', fontsize=14)
