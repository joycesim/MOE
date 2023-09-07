from mars_module import*

mars1=Mars()

r=np.linspace(mars1.core,mars1.radius) #radius in m
# print(r, type(r),r.shape[0])
# n=r.shape[0]
# print(type(n))  
# PGPa=np.zeros(n)
# solidus=np.zeros(n)
# liquidus=np.zeros(n)
# front=np.zeros(n)
# ET08solidus = np.zeros(n)
# ET08liquidus=np.zeros(n)
# ET08front=np.zeros(n)

# for ii in range(1,n):
#     PGPa[ii]=mars1.depth2PGPa(r[ii])
#     solidus[ii]=mars1.solidus(r[ii])
#     liquidus[ii]=mars1.liquidus(r[ii])
#     front[ii]=mars1.freezing_front(r[ii])
#     ET08solidus[ii] = mars1.ET08solidus(r[ii])
#     ET08liquidus[ii]=mars1.ET08liquidus(r[ii])
#     ET08front[ii]=mars1.ET08freezing_front(r[ii])

PGPa=mars1.depth2PGPa(r)
solidus=mars1.solidus(r)
liquidus=mars1.liquidus(r)
front=mars1.freezing_front(r)
ET08solidus = mars1.ET08solidus(r)
ET08liquidus=mars1.ET08liquidus(r)
ET08front=mars1.ET08freezing_front(r)
    
plt.figure(1)

plt.subplot(1,2,1)
plt.plot(PGPa,r/1.0e3)
plt.xlabel('Pressure (GPa)')
plt.ylabel('Radius (km)')
#
plt.subplot(1,2,2)
plt.plot(solidus,PGPa,'-b',linewidth=4)
plt.plot(ET08solidus,PGPa,'--b',linewidth=4)
plt.plot(liquidus,PGPa,'-r',linewidth=4)
plt.plot(ET08liquidus,PGPa,'--r',linewidth=4)
plt.plot(front,PGPa,'-g',linewidth=4)
plt.plot(ET08front,PGPa,'--g',linewidth=4)
plt.ylim=(np.max(PGPa),np.min(PGPa))
plt.gca().invert_yaxis()
plt.legend(['Duncan Solidus','ET08 Solidus','Duncan Liquidus','ET08 Liquidus','Duncan Front','ET08 Front'],loc="best")


plt.xlabel(r"Temperature $^\mathsf{o}$C")
plt.ylabel('Pressure (GPa)')


# plt.figure(3)
# mars1.radius_temperature_analytical(plot=True)
# plt.plot(mars1.T,0.0*mars1.T)
plt.show()
