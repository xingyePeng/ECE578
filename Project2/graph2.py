# use file 2023.AS-rel.txt

import pandas as pd
import numpy as np
import pdb
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

np.set_printoptions(suppress=True)
# Find Globle degree
parsed_data=[]

with open("2023-rel.txt") as AS:
    for line in AS:
        values=line.strip().split('|')[:-1]
        #print(values)  
        parsed_data.append(values)
    
my_array=np.array(parsed_data,dtype=int)


# Find unique AS numbers in the first column
AS_unique = np.unique(my_array[:,0])

glbl=[]
peer=[]
prvd=[]
cstr=[]
### Find Globle degree
# Count occurrences of each unique AS number
for value in AS_unique:
    global_degree = np.count_nonzero(my_array[:] == value)
    customer_degree = np.count_nonzero(np.logical_and(my_array[:, 0] == value, my_array[:, 2] == -1))
    peer_degree = np.count_nonzero(np.logical_and(my_array[:, 0] == value, my_array[:, 2] == 0))
    provider_degree=np.count_nonzero(np.logical_and(my_array[:, 1] == value, my_array[:, 2] == -1))
    #print(f"AS Number: {value}, Global Degree: {global_degree}, Customer Degree: {customer_degree}, Peer Degree: {peer_degree},Provider Degree: {provider_degree}")
    
    glbl.append(global_degree)
    peer.append(peer_degree)
    prvd.append(provider_degree)
    cstr.append(customer_degree)

sid_st=[0,1,2,6,101,201,1000]
sid_ed=[0,1,5,100,200,1000,10000000000]
glbl_count=np.full((len(sid_st)),np.nan,float)
peer_count=np.full((len(sid_st)),np.nan,float)
prvd_count=np.full((len(sid_st)),np.nan,float)
cstr_count=np.full((len(sid_st)),np.nan,float)



for ii in range(len(sid_st)):
    glbl_count[ii]=len(list(filter(lambda x: ((x >= sid_st[ii]) and (x<=sid_ed[ii])), glbl)))
    peer_count[ii]=len(list(filter(lambda x: ((x >= sid_st[ii]) and (x<=sid_ed[ii])), peer)))
    prvd_count[ii]=len(list(filter(lambda x: ((x >= sid_st[ii]) and (x<=sid_ed[ii])), prvd)))
    cstr_count[ii]=len(list(filter(lambda x: ((x >= sid_st[ii]) and (x<=sid_ed[ii])), cstr)))
    
glbl_freq=glbl_count/np.nansum(glbl_count)
peer_freq=peer_count/np.nansum(peer_count)
prvd_freq=prvd_count/np.nansum(prvd_count)
cstr_freq=cstr_count/np.nansum(cstr_count)


fig=plt.figure(figsize=(20,17))
gspec = GridSpec(ncols=2, nrows=2, figure=fig)#, width_ratios=[2, 3])
#set the font size
fsize=15
lsize=12
#artifical axis
xaxis=np.arange(7+2)*10
xlabels=['','0','1','2-5','6-100','100-200','200-1000','>1000','']
#add plot a)
ax1=fig.add_subplot(gspec[0,0])
ax1.bar(xaxis[1:-1], glbl_freq, width = 5, color='b',align='center',label='Global')
ax1.set_xlim(min(xaxis), max(xaxis))
ax1.set_ylim(0,1)
ax1.set_xlabel('Global',fontsize=fsize)
ax1.set_ylabel('PDF',fontsize=fsize)
ax1.tick_params(axis='x',labelsize=lsize,length=5,width=3,direction='in',which='major')
ax1.tick_params(axis='y',labelsize=lsize,length=5,width=3,direction='in',which='major')
ax1.set_xticklabels(xlabels)
ax1.legend(loc='upper right',fontsize=lsize)
# ax1.text(0.05, 0.95,'a)',fontsize=lsize,ha='center',va='center',transform = ax1.transAxes)
for axis in ['top','bottom','left','right']:
    ax1.spines[axis].set_linewidth(3)

#add plot b)
ax1=fig.add_subplot(gspec[0,1])
ax1.bar(xaxis[1:-1], peer_freq, width = 5, color='b',align='center',label='Peer')
ax1.set_xlim(min(xaxis), max(xaxis))
ax1.set_ylim(0,1)
ax1.set_xlabel('Peer',fontsize=fsize)
ax1.set_ylabel('PDF',fontsize=fsize)
ax1.tick_params(axis='x',labelsize=lsize,length=5,width=3,direction='in',which='major')
ax1.tick_params(axis='y',labelsize=lsize,length=5,width=3,direction='in',which='major')
ax1.set_xticklabels(xlabels)
ax1.legend(loc='upper right',fontsize=lsize)
#ax1.text(0.05, 0.95,'a)',fontsize=lsize,ha='center',va='center',transform = ax1.transAxes)
for axis in ['top','bottom','left','right']:
    ax1.spines[axis].set_linewidth(3)

#add plot c)
ax1=fig.add_subplot(gspec[1,0])
ax1.bar(xaxis[1:-1], prvd_freq, width = 5, color='b',align='center',label='Provider')
ax1.set_xlim(min(xaxis), max(xaxis))
ax1.set_ylim(0,1)
ax1.set_xlabel('Provider',fontsize=fsize)
ax1.set_ylabel('PDF',fontsize=fsize)
ax1.tick_params(axis='x',labelsize=lsize,length=5,width=3,direction='in',which='major')
ax1.tick_params(axis='y',labelsize=lsize,length=5,width=3,direction='in',which='major')
ax1.set_xticklabels(xlabels)
ax1.legend(loc='upper right',fontsize=lsize)
#ax1.text(0.05, 0.95,'a)',fontsize=lsize,ha='center',va='center',transform = ax1.transAxes)
for axis in ['top','bottom','left','right']:
    ax1.spines[axis].set_linewidth(3)

#add plot d)
ax1=fig.add_subplot(gspec[1,1])
ax1.bar(xaxis[1:-1], cstr_freq, width = 5, color='b',align='center',label='Customer')
ax1.set_xlim(min(xaxis), max(xaxis))
ax1.set_ylim(0,1)
ax1.set_xlabel('Customer',fontsize=fsize)
ax1.set_ylabel('PDF',fontsize=fsize)
ax1.tick_params(axis='x',labelsize=lsize,length=5,width=3,direction='in',which='major')
ax1.tick_params(axis='y',labelsize=lsize,length=5,width=3,direction='in',which='major')
ax1.set_xticklabels(xlabels)
ax1.legend(loc='upper right',fontsize=lsize)
#ax1.text(0.05, 0.95,'a)',fontsize=lsize,ha='center',va='center',transform = ax1.transAxes)
for axis in ['top','bottom','left','right']:
    ax1.spines[axis].set_linewidth(3)


#plt.tight_layout()
plt.show()

#pdb.set_trace()