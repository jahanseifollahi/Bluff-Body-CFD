import pandas as pd
import scipy.fft as fft
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv(r'Workbenches\bluff_body_cylinder_files\dp0\FFF-1\Fluent\report-file-0.out', skiprows=3,sep=r'\s+',usecols=[1,2],header=None)

flow_time=df[2].values
coef_lift=df[1].values

indicies_to_remove=[]

for i in range(len(flow_time)):
    
    if flow_time[i]>=1:
        break
    
    elif flow_time[i]<1:
        indicies_to_remove.append(i)

mask=np.ones(len(flow_time),dtype=bool)

mask[indicies_to_remove]=False


flow_time=flow_time[mask]
coef_lift=coef_lift[mask]

max_Cl=np.max(coef_lift)

dt=0.0008

N=len(flow_time)

print(f"dt: {dt}")

strength=fft.rfft(coef_lift)

strength=np.abs(strength)

freq=fft.rfftfreq(N,d=dt)

dom_freq=freq[np.argmax(strength)]

print(f"Dominant Frequency: {dom_freq}")
print(f"Max Cl: {max_Cl}")

St=(0.01*dom_freq)/0.2921

plt.figure(1)

plt.title('CL vs Flow Time')
plt.plot(flow_time,coef_lift)
plt.xlabel('Flow Time (S)')
plt.ylabel('Coefficient of Lift')
plt.grid(True)

plt.figure(2)

ax=plt.subplot()

plt.title('Strength vs Frequency')
ax.stem(freq,strength, basefmt=" ")
info_box=f"Dominant Frequency: {dom_freq:.3f} Hz\nStrouhal Number: {St:.3f}"
leg = plt.legend([plt.Line2D([0], [0], color='white', alpha=0)], [info_box], loc='upper right', title="Signal Info")
leg.set_draggable(True)
plt.xlabel('Frequency')
plt.ylabel('Strength')
plt.grid(True)
plt.show()