from mars_module import*

###############################################
# Large parameter space
# Uncomment the block below to explore a large
# parameter space
# ###############################################
# n_oceans=np.array([0.4,0.8])#0.5,1.0,1.5,2.0,2.5,3.0])
# redox_fac=np.array([0.01,0.1,1.0,10.0,100.0,1000.0, 10000.0])
# H_over_C=0.55#np.array([0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9])
# for ii in range(0,1):
#     for jj in range(0,6):
#         # for kk in range (0,7):
            
#             mars=Mars(noceans=n_oceans[ii],HoverC=H_over_C,\
#                       nsteps=1000000,redox_factor=redox_fac[jj])
#             mars.time_marching(4.0)
#             mars.output_filenames()
#             mars.create_output()
#             mars.write_all_REE()
#             del mars
###############################################
# 
n_oceans= 0.8 #=0.04 #0.8#1.0#0.8
# n_oceans=np.array([1.0])
# n_oceans=np.array([0.01,0.04,0.09,0.2,0.3,0.4,0.5,0.6,0.7,0.8,1.0])
# n=np.array([5000000,10000000,5000000,10000000,10000000,10000000,0.5,0.6,0.7,0.8,1.0])

H_over_C = 0.55

# redox_fac= 0.01
redox_fac= np.array([0.1,1.0,10.0,100.0,1000.0])
# redox_fac= np.array([0.01,0.1,1.0,10.0,100.0,1000.0,1.0e4])

      
Ma2s = 1e6*365*24*60*60
Tautest = 0.001 *Ma2s
print ("Tau (s)", Tautest)
# 3.15e13s or  tau = 1 Ma

# for ii in range (0,11):
#     mars=Mars(noceans=n_oceans[ii],HoverC=H_over_C, nsteps=10000,redox_factor=redox_fac)
#     mars.time_marching(4.0,const_Ftl=False)
#     # mars.time_marching(4.0,const_Ftl=True)
#     # mars.output_filenames()
#     mars.create_output()
#     mars.write_all_REE()
#     del mars
   
for ii in range (0,7):
# for ii in range (0,2):
    mars=Mars(noceans=n_oceans,HoverC=H_over_C, nsteps=10000,redox_factor=redox_fac[ii], tau = Tautest)
    mars.time_marching(4.0,const_Ftl=False)
    # mars.time_marching(4.0,const_Ftl=True)
    # mars.output_filenames()
    mars.create_output()
    mars.write_all_REE()
    del mars
    

    # del mars

# mars=Mars(noceans=n_oceans,HoverC=H_over_C, nsteps=10000,redox_factor=redox_fac)
# # mars.time_marching(4.0,const_Ftl=True) #False)
# mars.time_marching(4.0,const_Ftl=False) #False)
# # mars.output_filenames()
# mars.create_output()
# mars.write_all_REE()
