import pandas as pd
import scipy.fft as fft
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv(r'Workbenches\bluff_body_cylinder_Operation_files\dp0\FFF\Fluent\lift_coef-rfile.out', skiprows=3,sep=r'\s+',usecols=[1,2],header=None)
df1=pd.read_csv(r'Workbenches\bluff_body_cylinder_Operation_files\dp0\FFF\Fluent\drag-coef_report-rfile.out', skiprows=3,sep=r'\s+',usecols=[1,2],header=None)
df2=pd.read_csv(r'Workbenches\bluff_body_cylinder_Operation_files\dp0\FFF\Fluent\wall-y+_report-rfile.out', skiprows=3,sep=r'\s+',usecols=[1,2],header=None) 

drag_coef=df1[1].values
y_plus=df2[1].values
flow_time=df[2].values
coef_lift=df[1].values

#average_drag

steady_df=drag_coef[(flow_time>=0.4017) & (flow_time<=0.588)]

steady_sum=steady_df.sum()

average_drag_coef=steady_sum/len(steady_df)


indicies_to_remove=[]

for i in range(len(flow_time)):
    
    if flow_time[i]>=0.3:
        break
    
    elif flow_time[i]<0.3:
        indicies_to_remove.append(i)

mask=np.ones(len(flow_time),dtype=bool)

mask[indicies_to_remove]=False


flow_time=flow_time[mask]
coef_lift=coef_lift[mask]
coef_drag=drag_coef[mask]
y_plus=y_plus[mask]


max_peak_CD=np.max(coef_drag)
min_peak_CD=np.min(coef_drag)

max_Cl=np.max(coef_lift)

dt=0.00017

N=len(flow_time)

print(f"dt: {dt}")

strength=fft.rfft(coef_lift)

strength=np.abs(strength)

freq=fft.rfftfreq(N,d=dt)

dom_freq=freq[np.argmax(strength)]

print(f"Dominant Frequency: {dom_freq:.3f} Hz")
print(f"Max CD: {max_peak_CD:.3f}")
print(f"Min CD: {min_peak_CD:.3f}")
print(f"Average Drag Coefficient: {average_drag_coef:.3f}")

St=(0.1*dom_freq)/14.61

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

plt.figure(3)

plt.title('Y+ vs Flow Time')
plt.plot(flow_time,y_plus)
plt.xlabel('Flow Time (S)')
plt.ylabel('Average-Weighted Y+')
plt.grid(True)

plt.figure(4)

plt.title('Drag Coefficient vs Flow Time')
plt.plot(flow_time,coef_drag)
plt.xlabel('Flow Time (S)')
plt.ylabel('Drag Coefficient')
plt.grid(True)

plt.show()


