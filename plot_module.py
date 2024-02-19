from mars_module import*
def plot_profile(obj):
    """This function plots a profile of RM concentrations
    the input object should be of class Mars_read"""
    f2=obj.output_filenames(const=False)
    data2=np.loadtxt(f2[3],delimiter=',')
    obj.CCO2RM   = data2[:,4]
    obj.MCO2RM   = data2[:,1]
    del data2
    data2=np.loadtxt(f2[0],delimiter=',')
    obj.akm      = data2[:,2]
    del data2
    data2=np.loadtxt(f2[2],delimiter=',')
    obj.CH2ORM   = data2[:,4]
    obj.MH2ORM   = data2[:,1]
    del data2,f2

    #print 'Shape of water, CO2, a'
    #print np.shape(obj.MH2ORM),np.shape(obj.MCO2RM),np.shape(obj.akm)
    n=np.size(obj.MH2ORM)
    dMH2ORM=obj.MH2ORM[1:n]-obj.MH2ORM[0:n-1]
    dMCO2RM=obj.MCO2RM[1:n]-obj.MCO2RM[0:n-1]
    plt.figure(figsize=(10,12))
    plt.subplot(1,2,1)
    plt.semilogx(dMCO2RM/obj.CO2MASS,obj.akm[1:n],'o',markerfacecolor='dimgray',)
    plt.semilogx(dMH2ORM/obj.H2OMASS,obj.akm[1:n],'s',markerfacecolor='teal')#,lw=4,ls='dashed')
    plt.xlim(1.0e-7,1.0e-4)
    plt.legend(['Total C',r'$\mathrm{H_2O}$'],fancybox=True\
               ,framealpha=0.7,loc=4)
    plt.xlabel(r'$\Delta M^{RM}_Z$')
    plt.ylabel('Height above CMB (km)')
    plt.subplot(1,2,2)
    plt.plot(obj.MCO2RM/obj.CO2MASS,obj.akm,'dimgray',lw=4)
    plt.plot(obj.MH2ORM/obj.H2OMASS,obj.akm,'teal',lw=4,ls='dashed')
    plt.legend(['Total C',r'$\mathrm{H_2O}$'],fancybox=True\
               ,framealpha=0.7,loc=4)
    plt.xlabel(r'Cumulative mass fraction')
    plt.ylabel('Height above CMB (km)')
def compare_Ftl_models():
    """Compares the thermal evolutions of two objects
    The second object should have a constant trapped
    melt fraction
    """
    obj1 = Mars_read(noceans=0.8,HoverC=0.55,redox_factor=1.0)
    obj2 = Mars_read(noceans=0.8,HoverC=0.55,redox_factor=1.0,Ftl_const=True)
    f=obj1.output_filenames()
    data3=np.loadtxt(f[2],delimiter=',')
    obj1.tma      = data3[:,0]
    obj1.MH2ORM   = data3[:,1]
    obj1.MH2OMO   = data3[:,2]
    #self.MH2OPA   = data3[:,3]
    obj1.CH2ORM   = data3[:,4]
    #self.CH2OMO   = data3[:,5]
    data2=np.loadtxt(f[1],delimiter=',')
    obj1.PCO2     = data2[:,1]
    obj1.PH2O     = data2[:,2]
    del data2,data3,f
    f=obj2.output_filenames(const=True)
    data3=np.loadtxt(f[2],delimiter=',')
    obj2.tma      = data3[:,0]
    obj2.MH2ORM   = data3[:,1]
    obj2.MH2OMO   = data3[:,2]
    #self.MH2OPA   = data3[:,3]
    obj2.CH2ORM   = data3[:,4]
    #self.CH2OMO   = data3[:,5]
    data2=np.loadtxt(f[1],delimiter=',')
    obj2.PCO2     = data2[:,1]
    obj2.PH2O     = data2[:,2]
    del data2,data3,f
    
    plt.figure(figsize=(18,12))
    ax1=plt.subplot(2,2,1)
    plt.plot(obj1.tma,obj1.PCO2/1.0e5,color='forestgreen',linewidth=4)
    plt.plot(obj2.tma,obj2.PCO2/1.0e5,ls='--',color='darkorange',linewidth=4)
    
    plt.ylabel(r"${P_{CO2}}$ (bar)",fontsize=30)
    #plt.xlabel('Time (Ma)',fontsize=30)
    
    yticks_bar=([140,180,220])
    plt.text(1.1,147,'(a)',fontsize=50,fontweight='bold')
    ax1.set_yticks(yticks_bar)
    plt.ylim(140,230)
    ################
    ax2=ax1.twinx()    
    newpos   = 0.1*np.array(yticks_bar)
    newlabels=newpos.astype(int)
    ax2.set_yticks(newpos)
    ax2.set_yticklabels(newlabels)
    ax2.yaxis.set_ticks_position('right') 
    ax2.yaxis.set_label_position('right') 
    ax2.spines['right'].set_position(('outward', 0))
    ax2.set_ylabel(r"${P_{CO2}}$ (MPa)",fontsize=30,labelpad=20)
    plt.ylim(22,25)
    plt.xlim(0.00,1.25 )
    ###############
    ax2=plt.subplot(2,2,2)
    plt.plot(obj1.tma,obj1.MH2ORM/1.0e21,color='forestgreen',linewidth=4)
    plt.plot(obj2.tma,obj2.MH2ORM/1.0e21,ls='--',color='darkorange',linewidth=4)
    plt.ylabel(r"$\mathrm{H_2O}$ in RM ($10^{21}$ kg)",fontsize=30,labelpad=20)
    plt.text(0.05,0.1,'(b)',fontsize=50,fontweight='bold')
    ax2.set_yticks([0.2,0.4,0.6,0.8,1.0])
    ax2.yaxis.set_ticks_position('right') 
    ax2.yaxis.set_label_position('right') 
    ax2.spines['right'].set_position(('outward', 0))
    plt.legend([r'Dynamic $F_{tl}$',r'Constant $F_{tl}$'],fancybox=True,framealpha=0.7,loc=2)
    plt.xlim(0.00,1.25 )
    ax1=plt.subplot(2,2,3)
    plt.plot(obj1.tma,obj1.PH2O/1.0e5,color='forestgreen',linewidth=4)
    plt.plot(obj2.tma,obj2.PH2O/1.0e5,ls='--',color='darkorange',linewidth=4)
    plt.ylabel(r"${P_{H2O}}$ (bar)",fontsize=30)
    plt.xlabel('Time (Ma)',fontsize=30)
    yticks_bar=([50,100,150,200,250,300])
    plt.text(1.1,25,'(c)',fontsize=50,fontweight='bold')
    ##################
    GEL=obj1.kg2GELm(obj1.H2OMASS)/1.0e3
    plt.text(0.1,220,'{:3.2f} GEL (km)'.format(GEL),fontsize=30)
    plt.text(0.1,190,'H:C = {:3.2f}'.format(obj1.HoverC),fontsize=30)
    plt.text(0.1,160,r'$K^\ast$ = {:3.2f}'.format(obj1.redox_factor),fontsize=30)
    ################
    ax2=ax1.twinx()    
    newpos   = 0.1*np.array(yticks_bar)
    newlabels=newpos.astype(int)
    ax2.set_yticks(newpos)
    ax2.set_yticklabels(newlabels)
    ax2.yaxis.set_ticks_position('right')
    ax2.yaxis.set_label_position('right') 
    ax2.spines['right'].set_position(('outward', 0))
    ax2.set_ylabel(r"${P_{H2O}}$ (MPa)",fontsize=30,labelpad=20)
    plt.xlim(0.00,1.25 )
    ###############
    ax2=plt.subplot(2,2,4)
    plt.plot(obj1.tma,obj1.MH2OMO/1.0e21,color='forestgreen',linewidth=4)
    plt.plot(obj2.tma,obj2.MH2OMO/1.0e21,ls='--',color='darkorange',linewidth=4)
    plt.ylabel(r"$\mathrm{H_2O}$ in MO ($10^{21}$ kg)",fontsize=30,labelpad=20)
    plt.xlabel('Time (Ma)',fontsize=30)
    plt.text(0.05,0.16,'(d)',fontsize=50,fontweight='bold')
    ax2.set_yticks([0.2,0.6,1.0,1.4,1.8])
    ax2.yaxis.set_ticks_position('right') 
    ax2.yaxis.set_label_position('right') 
    ax2.spines['right'].set_position(('outward', 0))
    plt.xlim(0.00,1.25 )
    plt.ylim(0.0,1.4)
    ###################
    print( '#########################')
    print( 'Final PH2O (bar), dynamic:',np.max(obj1.PH2O/1.0e5))
    print( 'Final PCO2 (bar), dynamic:',np.max(obj1.PCO2/1.0e5))
    print( 'Final MH20RM (kg), dynamic:',np.max(obj1.MH2ORM))
    print( 'Final MH20MO (kg), dynamic:',np.max(obj1.MH2OMO))
    print( '#########################')
    print( 'Final PH2O (bar), Constant:',np.max(obj2.PH2O/1.0e5))
    print( 'Final PCO2 (bar), Constant:',np.max(obj2.PCO2/1.0e5))
    print( 'Final MH20RM (kg), Constant:',np.max(obj2.MH2ORM))
    print( 'Final MH20MO (kg), Constant:',np.max(obj2.MH2OMO))
    print( '#########################')
    
def compare_evolution(obj1,obj2):
    """Compares the thermal evolutions of two objects"""
    obj1.load_evolution()
    obj2.load_evolution()
    plt.figure(figsize=(10,16))

    plt.subplot(3,1,1)
    plt.plot(obj1.tma,obj1.T,color='cornflowerblue',linewidth=4)
    plt.plot(obj2.tma,obj2.T,ls='--',color='dimgray',linewidth=4)
    plt.legend([r'$K^\ast = ${:.2f}'.format(obj1.redox_factor), r'$K^\ast = ${:.2f}'.format(obj2.redox_factor)],fancybox=True,framealpha=0.7)
    plt.ylabel(r'$T^\mathrm{o}$C',fontsize=30)
    plt.text(2.0,1500,'(a)',fontsize=40,fontweight='bold')
    plt.xlim(0.0,2.25)
    ##############################################
    ax1=plt.subplot(3,1,2)
    plt.plot(obj1.tma,obj1.PCO2/1.0e5,color='cornflowerblue',linewidth=4)
    plt.plot(obj2.tma,obj2.PCO2/1.0e5,ls='--',color='dimgray',linewidth=4)
    plt.ylabel(r"${P_{CO2}}$ (bar)",fontsize=30)
    plt.text(2.0,45,'(b)',fontsize=40,fontweight='bold')
    plt.yticks([50,150,250,350])
    plt.xlim(0.0,2.25)
    ################
    ax2=ax1.twinx()
    yticks_bar=[50,150,250,350]
    newpos   = 0.1*np.array(yticks_bar)
    newlabels=newpos.astype(int)
    ax2.set_yticks(newpos)
    ax2.set_yticklabels(newlabels)
    ax2.yaxis.set_ticks_position('right') 
    ax2.yaxis.set_label_position('right') 
    ax2.spines['right'].set_position(('outward', 0))
    ax2.set_ylabel(r"${P_{CO2}}$ (MPa)",fontsize=30,labelpad=20)
    
    ###########################################################
    ax1=plt.subplot(3,1,3)
    plt.plot(obj1.tma,obj1.PH2O/1.0e5,color='cornflowerblue',linewidth=4)
    plt.plot(obj2.tma,obj2.PH2O/1.0e5,ls='--',color='dimgray',linewidth=4)
    plt.ylabel(r"${P_{H2O}}$ (bar)",fontsize=30)
    plt.xlabel('Time (Ma)',fontsize=30)
    plt.text(2.0,20,'(c)',fontsize=40,fontweight='bold')
    plt.xlim(0.0,2.25)
    ################
    ax2=ax1.twinx()
    yticks_bar=[20,60,100,140]
    newpos   = 0.1*np.array(yticks_bar)
    newlabels=newpos.astype(int)
    ax2.set_yticks(newpos)
    ax2.set_yticklabels(newlabels)
    ax2.yaxis.set_ticks_position('right') 
    ax2.yaxis.set_label_position('right') 
    ax2.spines['right'].set_position(('outward', 0))
    ax2.set_ylabel(r"${P_{H2O}}$ (MPa)",fontsize=30,labelpad=20)
    ###########################################################
def Final_concentrations(n_oceans,H_over_C=0.55,redox_fac=1.0,redox_fac2=1.0e2):
    """Plots the final concentrations of H2O and C in the mantle
    Input:
    n_oceans      : 11 sized array of # oceans of H2O in the bulk
    H_over_C      : H:C ratio of the bulk, default 0.55
    redox_fac     : Float
    redox_fac2    : Float
    """
    CO2overH2O=1.0/(H_over_C*2.45)
    CO2_mass=n_oceans*1.6e21*CO2overH2O
    H2O_mass=n_oceans*1.6e21
    ## Load objects for the redox factor one, dynamic melt trapping
    mars1=Mars_read(noceans=n_oceans[0],HoverC=H_over_C,redox_factor=redox_fac)
    mars2=Mars_read(noceans=n_oceans[1],HoverC=H_over_C,redox_factor=redox_fac)
    mars3=Mars_read(noceans=n_oceans[2],HoverC=H_over_C,redox_factor=redox_fac)
    mars4=Mars_read(noceans=n_oceans[3],HoverC=H_over_C,redox_factor=redox_fac)
    mars5=Mars_read(noceans=n_oceans[4],HoverC=H_over_C,redox_factor=redox_fac)
    mars6=Mars_read(noceans=n_oceans[5],HoverC=H_over_C,redox_factor=redox_fac)
    mars7=Mars_read(noceans=n_oceans[6],HoverC=H_over_C,redox_factor=redox_fac)
    mars8=Mars_read(noceans=n_oceans[7],HoverC=H_over_C,redox_factor=redox_fac)
    mars9=Mars_read(noceans=n_oceans[8],HoverC=H_over_C,redox_factor=redox_fac)
    mars10=Mars_read(noceans=n_oceans[9],HoverC=H_over_C,redox_factor=redox_fac)
    mars11=Mars_read(noceans=n_oceans[10],HoverC=H_over_C,redox_factor=redox_fac)
    # Load objects for similar situation but constant trapped melt fraction
    mars1_const=Mars_read(noceans=n_oceans[0],HoverC=H_over_C,\
                      redox_factor=redox_fac,Ftl_const=True)
    mars2_const=Mars_read(noceans=n_oceans[1],HoverC=H_over_C,\
                      redox_factor=redox_fac,Ftl_const=True)
    mars3_const=Mars_read(noceans=n_oceans[2],HoverC=H_over_C,\
                      redox_factor=redox_fac,Ftl_const=True)
    mars4_const=Mars_read(noceans=n_oceans[3],HoverC=H_over_C,\
                      redox_factor=redox_fac,Ftl_const=True)
    mars5_const=Mars_read(noceans=n_oceans[4],HoverC=H_over_C,\
                      redox_factor=redox_fac,Ftl_const=True)
    mars6_const=Mars_read(noceans=n_oceans[5],HoverC=H_over_C,\
                      redox_factor=redox_fac,Ftl_const=True)
    mars7_const=Mars_read(noceans=n_oceans[6],HoverC=H_over_C,\
                      redox_factor=redox_fac,Ftl_const=True)
    mars8_const=Mars_read(noceans=n_oceans[7],HoverC=H_over_C,\
                      redox_factor=redox_fac,Ftl_const=True)
    mars9_const=Mars_read(noceans=n_oceans[8],HoverC=H_over_C,\
                      redox_factor=redox_fac,Ftl_const=True)
    mars10_const=Mars_read(noceans=n_oceans[9],HoverC=H_over_C,\
                      redox_factor=redox_fac,Ftl_const=True)
    mars11_const=Mars_read(noceans=n_oceans[10],HoverC=H_over_C,\
                      redox_factor=redox_fac,Ftl_const=True)

    #Load dynamic melt trapping data for the second, redox factor
    mars1_a=Mars_read(noceans=n_oceans[0],HoverC=H_over_C,redox_factor=redox_fac2)
    mars2_a=Mars_read(noceans=n_oceans[1],HoverC=H_over_C,redox_factor=redox_fac2)
    mars3_a=Mars_read(noceans=n_oceans[2],HoverC=H_over_C,redox_factor=redox_fac2)
    mars4_a=Mars_read(noceans=n_oceans[3],HoverC=H_over_C,redox_factor=redox_fac2)
    mars5_a=Mars_read(noceans=n_oceans[4],HoverC=H_over_C,redox_factor=redox_fac2)
    mars6_a=Mars_read(noceans=n_oceans[5],HoverC=H_over_C,redox_factor=redox_fac2)
    mars7_a=Mars_read(noceans=n_oceans[6],HoverC=H_over_C,redox_factor=redox_fac2)
    mars8_a=Mars_read(noceans=n_oceans[7],HoverC=H_over_C,redox_factor=redox_fac2)
    mars9_a=Mars_read(noceans=n_oceans[8],HoverC=H_over_C,redox_factor=redox_fac2)
    mars10_a=Mars_read(noceans=n_oceans[9],HoverC=H_over_C,redox_factor=redox_fac2)
    mars11_a=Mars_read(noceans=n_oceans[10],HoverC=H_over_C,redox_factor=redox_fac2)
    ##############################################
    #Now make the plots
    ##############################################
    # Plot: compare H2O and CO2 concentrations
    # as a function of initial CO2 content
    # For two different values of K*
    ##############################################
    final_water=np.array([mars1.CH2ORM_final,mars2.CH2ORM_final,\
                      mars3.CH2ORM_final,mars4.CH2ORM_final,\
                      mars5.CH2ORM_final,mars6.CH2ORM_final,\
                      mars7.CH2ORM_final,mars8.CH2ORM_final,\
                      mars9.CH2ORM_final,mars10.CH2ORM_final,\
                       mars11.CH2ORM_final])
    
    final_CO2=np.array([mars1.CCO2RM_final,mars2.CCO2RM_final,\
                      mars3.CCO2RM_final,mars4.CCO2RM_final,\
                      mars5.CCO2RM_final,mars6.CCO2RM_final,\
                      mars7.CCO2RM_final,mars8.CCO2RM_final,\
                    mars9.CCO2RM_final,mars10.CCO2RM_final,\
                    mars11.CCO2RM_final])
    final_time=np.array([mars1.tma_final,mars2.tma_final,\
                      mars3.tma_final,mars4.tma_final,\
                      mars5.tma_final,mars6.tma_final,\
                      mars7.tma_final,mars8.tma_final,\
                      mars9.tma_final,mars10.tma_final,\
                       mars11.tma_final])
    final_water_a=np.array([mars1_a.CH2ORM_final,mars2_a.CH2ORM_final,\
                      mars3_a.CH2ORM_final,mars4_a.CH2ORM_final,\
                      mars5_a.CH2ORM_final,mars6_a.CH2ORM_final,\
                        mars7_a.CH2ORM_final,mars8_a.CH2ORM_final,\
                        mars9_a.CH2ORM_final,mars10_a.CH2ORM_final,\
                        mars11_a.CH2ORM_final])
    final_CO2_a=np.array([mars1_a.CCO2RM_final,mars2_a.CCO2RM_final,\
                      mars3_a.CCO2RM_final,mars4_a.CCO2RM_final,\
                      mars5_a.CCO2RM_final,mars6_a.CCO2RM_final,\
                      mars7_a.CCO2RM_final,mars8_a.CCO2RM_final,\
                      mars9_a.CCO2RM_final,mars10_a.CCO2RM_final,\
                       mars11_a.CCO2RM_final])
    final_time_a=np.array([mars1_a.tma_final,mars2_a.tma_final,\
                      mars3_a.tma_final,mars4_a.tma_final,\
                      mars5_a.tma_final,mars6_a.tma_final,\
                        mars7_a.tma_final,mars8_a.tma_final,\
                        mars9_a.tma_final,mars10_a.tma_final,\
                        mars11_a.tma_final])
    final_water_const=np.array([mars1_const.CH2ORM_final,mars2_const.CH2ORM_final,\
                      mars3_const.CH2ORM_final,mars4_const.CH2ORM_final,\
                      mars5_const.CH2ORM_final,mars6_const.CH2ORM_final,\
                            mars7_const.CH2ORM_final,mars8_const.CH2ORM_final,\
                            mars9_const.CH2ORM_final,mars10_const.CH2ORM_final,\
                            mars11_const.CH2ORM_final])
    final_CO2_const=np.array([mars1_const.CCO2RM_final,mars2_const.CCO2RM_final,\
                      mars3_const.CCO2RM_final,mars4_const.CCO2RM_final,\
                      mars5_const.CCO2RM_final,mars6_const.CCO2RM_final,\
                          mars7_const.CCO2RM_final,mars8_const.CCO2RM_final,\
                          mars9_const.CCO2RM_final,mars10_const.CCO2RM_final,\
                           mars11_const.CCO2RM_final])
    
    mGEL= mars1.kg2GELm(H2O_mass)
    ################
    # Bound on initial water
    # 0.1-0.2 wt% from Brasser 2013
    initial_water_low=mars1.mass*1.0e-3
    initial_water_hi=mars1.mass*2.0e-3
    initial_CO2_low=mars1.mass*1.0e-3/(0.55*2.45)
    initial_CO2_hi=mars1.mass*2.0e-3/(0.55*2.45)
    intial_GEL_low=mars1.kg2GELm(initial_water_low)
    initial_GEL_hi=mars1.kg2GELm(initial_water_hi)
    print( 'Initial water content in Mars 0.1-0.2 wt%, Brasser (2013)')
    print( 'Initial water content in GEL(m):low, hi',intial_GEL_low,initial_GEL_hi)
    print( 'Initial water content in  kg:, low, hi:',initial_water_low,initial_water_hi)
    print( 'Initial CO2 content in  kg:, low, hi:',initial_CO2_low,initial_CO2_hi/(0.55*2.45))
    initial_water_lunine_low=0.06*1.5e21
    initial_water_lunine_hi=0.27*1.5e21
    initial_CO2_lunine_low=0.06*1.5e21/(0.55*2.45)
    initial_CO2_lunine_hi=0.27*1.5e21/(0.55*2.45)
    intial_GEL_lunine_low=mars1.kg2GELm(initial_water_lunine_low)
    initial_GEL_lunine_hi=mars1.kg2GELm(initial_water_lunine_hi)
    print( 'Initial water content in Mars 6- 27%, ocean mass (1.5e21 kg) Lunine,2003')
    print( 'Initial water content in GEL(m), Lunine:low, hi',intial_GEL_lunine_low,initial_GEL_lunine_hi)
    print( 'Initial water content in  kg, Lunine:, low, hi:',initial_water_lunine_low,initial_water_lunine_hi)
    print( 'Initial CO2 content in  kg, Lunine:C=0.55 (H):, low, hi:',initial_CO2_lunine_low,initial_CO2_lunine_hi)

    print( 'Carbon concentration in Bulk Mars Lodders anf Fegley (ppm):',2960)

    print( 'Carbon concentration in Bulk Mars Lodders anf Fegley (ppmw):',2960)

    print( 'Carbon and CO2 masses from Lodders and Fegley (kg):',mars1.mass*2960.0e-6,mars1.mass*2960.0e-6*(16.0*2+12)/12)
    ###############
    # plt.figure(figsize=(10,16))
    plt.figure(figsize=(8,12))

    ax1=plt.subplot(2,1,1)
    plt.semilogy(CO2_mass,final_CO2*1.0e6,'o',markersize=20,color='darkgreen')
    plt.semilogy(CO2_mass,final_CO2_a*1.0e6,'s',markersize=20,color='dimgray')

    plt.ylabel(r'Mantle $\mathrm{CO_2}$ (ppm)')

    plt.semilogy(CO2_mass,final_CO2*1.0e6,'-',lw=3,color='darkgreen')
    plt.semilogy(CO2_mass,final_CO2_a*1.0e6,'-',lw=3,color='dimgray')
    plt.ylabel(r'Mantle $\mathrm{CO_2}$ (ppmw)')
    
    plt.text(0.7e21,41,'oxidizing',fontsize=28,color='darkgreen')
    plt.text(0.7e21,200,'reducing',fontsize=28,color='dimgray')
    
    plt.text(1.0e21,0.2,'(a)',fontweight='bold',fontsize=50)
    rect1=patches.Rectangle((0.7e20,0.1),2.3e20, 1000, color='steelblue',alpha=0.7)

    rect2=patches.Rectangle((4.63e20,0.1),2.2e20, 1000, color='steelblue',alpha=0.4)
    ax1.add_patch(rect1)
    ax1.add_patch(rect2)
    plt.text(0.9e21,10,r'H:C={:.2f}'.format(H_over_C),fontsize=28)
    plt.text(0.2e21,2,'LCM2003',rotation=90,fontsize=28)
    plt.text(0.6e21,2.5,'Brasser2013',rotation=90,fontsize=28)
    #plt.xlim(0.0,3.5)
    
    ax2=plt.subplot(2,1,2)
    plt.text(1.0e21,0.05,'(b)',fontweight='bold',fontsize=50)
    
    plt.text(0.7e21,1.05,'oxidizing'.format(redox_fac),fontsize=28,rotation = 30,color='darkgreen')
    plt.text(0.7e21,0.25,'reducing'.format(redox_fac),fontsize=28,rotation = 10,color='dimgray')

    plt.plot(CO2_mass,final_time,'o',markersize=20,color='darkgreen')
    plt.plot(CO2_mass,final_time_a,'s',markersize=20,color='dimgray')


    plt.legend([r'$K^\ast = ${:.2f}'.format(redox_fac), r'$K^\ast = ${:.2f}'.format(redox_fac2)],fancybox=True,loc=2,framealpha=0.7)
    plt.plot(CO2_mass,final_time,'-',lw=3,color='darkgreen') #'powderblue')
    plt.plot(CO2_mass,final_time_a,'-',lw=3,color='dimgray')

    rect3=patches.Rectangle((0.7e20,0.01),2.3e20, 2.0, color='steelblue',alpha=0.7)

    rect4=patches.Rectangle((4.63e20,0.01),2.2e20, 2.0, color='steelblue',alpha=0.4)
    ax2.add_patch(rect3)
    ax2.add_patch(rect4)

    plt.legend([r'$K^\ast = ${:.2f}'.format(redox_fac), r'$K^\ast = ${:.2f}'.format(redox_fac2)],fancybox=True,loc=2,framealpha=0.7)


    plt.ylabel('Time (Ma)')

    plt.xlabel(r'Initial $\mathrm{CO_2}$ (kg)')

    ###########################################################
    ##########################################################################
    ### Plot comparing the final CO2 and H2O contents for the two different
    ### types of trapped melt fraction. K* is constant
    ##########################################################################
    # plt.figure(figsize=(10,16))
    plt.figure(figsize=(8,12))
    ax1=plt.subplot(2,1,1)

    plt.plot(H2O_mass,final_water*1.0e6,'o',markersize=20,color='darkgreen')
    plt.plot(H2O_mass,final_water_const*1.0e6,'o',markersize=20,markeredgecolor='darkorange',markerfacecolor='none',markeredgewidth=3)


    plt.ylabel(r'Mantle $\mathrm{H_2O}$ (ppm)')

    plt.plot(H2O_mass,final_water_const*1.0e6,'-',lw=3,color='darkorange')
    plt.ylabel(r'Mantle $\mathrm{H_2O}$ (ppmw)')

    
    plt.xlabel(r'Initial bulk $\mathrm{H_2O}$ (kg)')


    rect1=patches.Rectangle((0.9e20,0),4.0e20, 1800, color='steelblue',alpha=0.7)

    rect2=patches.Rectangle((6.2e20,0),6.3e20, 1800, color='steelblue',alpha=0.4)
    ax1.add_patch(rect1)
    ax1.add_patch(rect2)

    ## Create a second x-axis for GEL m of H2O
    ax2=ax1.twiny()
    #######################################
    #Fit a curve to the data
    temp=final_water*1.0e6
    slope_GEL, pcov = curve_fit(fit_func,mGEL.ravel(),temp.ravel(),p0=None)
    slope_GEL_float="{:3.3f}".format(float(slope_GEL))
    
    #temp=H2O_mass
    slope_mass, pcov = curve_fit(fit_func,H2O_mass.ravel(),temp.ravel(),p0=None)
    y_fit=fit_func(H2O_mass,slope_mass)
    plt.plot(H2O_mass,y_fit,color='darkgreen',lw=3)

    plt.text(0.65e21,500,r"H$_2$O(ppm) = {0} $h$ (GEL m)".format(slope_GEL_float),rotation=30,color='darkgreen')

    

    
    GELs=np.linspace(np.min(mGEL),np.max(mGEL),4)
    newlabels=GELs.astype(int)
    newpos   = mars1.GELm2kg(GELs)
    ax2.set_xticks(newpos)
    ax2.set_xticklabels(newlabels)
    ax2.xaxis.set_ticks_position('top') 
    ax2.xaxis.set_label_position('top') 
    ax2.spines['top'].set_position(('outward', 0))
    ax2.set_xlabel(r'Initial bulk  $\mathrm{H_2O}$ GEL (m)')
    plt.text(0.055e21,1600,'(a)',fontweight='bold',fontsize=50)
    plt.text(0.1e21,1400,'LCM2003',fontsize=30,color='darkslateblue')
    plt.text(0.7e21,1400,'Brasser2013',fontsize=30,color='darkslateblue')
    
    ax3=plt.subplot(2,1,2)
    plt.semilogy(CO2_mass,final_CO2*1.0e6,'o',markersize=20,color='darkgreen')
    plt.semilogy(CO2_mass,final_CO2_const*1.0e6,'o',markersize=20,markeredgecolor='darkorange', markerfacecolor='none',markeredgewidth=3)

    plt.ylabel(r'Mantle $\mathrm{CO_2}$ (ppmw)')
    #plt.xlim(0.0,3.5)
    plt.xlabel(r'Initial $\mathrm{CO_2}$ (kg)')
    plt.legend(['Dynamic $F_{tl}$',r'Constant $F_{tl}$'],loc=4,fancybox=2,framealpha=0.7)
    plt.semilogy(CO2_mass,final_CO2*1.0e6,'-',lw=3,color='darkgreen')
    plt.semilogy(CO2_mass,final_CO2_const*1.0e6,'-',lw=3,color='darkorange')
    plt.text(0.05e21,30,'(b)',fontweight='bold',fontsize=50)
    rect3=patches.Rectangle((0.7e20,0.01),2.3e20, 100, color='steelblue',alpha=0.7)

    rect4=patches.Rectangle((4.63e20,0.01),2.2e20, 100, color='steelblue',alpha=0.4)
    ax3.add_patch(rect3)
    ax3.add_patch(rect4)
    plt.text(0.6e21,0.15, r'H:C = 0.55, $K^\ast = ${:.2f}'.format(redox_fac),fontsize=28)

def redox_plots(k1,n1=0.8,n2=0.4,H_over_C=0.55):
    """
    
    """
    CO2overH2O=1.0/(H_over_C*2.45)
    CO2_mass=n1*1.6e21*CO2overH2O
    H2O_mass=n1*1.6e21
    CO2_mass_a=n2*1.6e21*CO2overH2O
    H2O_mass_a=n2*1.6e21
    ## Load objects for the redox factor one, dynamic melt trapping
    mars1=Mars_read(noceans=n1,HoverC=H_over_C,redox_factor=k1[0])
    mars2=Mars_read(noceans=n1,HoverC=H_over_C,redox_factor=k1[1])
    mars3=Mars_read(noceans=n1,HoverC=H_over_C,redox_factor=k1[2])
    mars4=Mars_read(noceans=n1,HoverC=H_over_C,redox_factor=k1[3])
    mars5=Mars_read(noceans=n1,HoverC=H_over_C,redox_factor=k1[4])
    mars6=Mars_read(noceans=n1,HoverC=H_over_C,redox_factor=k1[5])
    mars7=Mars_read(noceans=n1,HoverC=H_over_C,redox_factor=k1[6])

    mars1_a=Mars_read(noceans=n2,HoverC=H_over_C,redox_factor=k1[0])
    mars2_a=Mars_read(noceans=n2,HoverC=H_over_C,redox_factor=k1[1])
    mars3_a=Mars_read(noceans=n2,HoverC=H_over_C,redox_factor=k1[2])
    mars4_a=Mars_read(noceans=n2,HoverC=H_over_C,redox_factor=k1[3])
    mars5_a=Mars_read(noceans=n2,HoverC=H_over_C,redox_factor=k1[4])
    mars6_a=Mars_read(noceans=n2,HoverC=H_over_C,redox_factor=k1[5])
    mars7_a=Mars_read(noceans=n2,HoverC=H_over_C,redox_factor=k1[6])
    
    
    #############################################
    ##############################################
    # Plot: compare end products for different 
    # values of K*
    ##############################################
    plt.figure(figsize=(10,16))
    freezing_time=np.array([mars1.tma_final,mars2.tma_final,mars3.tma_final,mars4.tma_final,mars5.tma_final,mars6.tma_final,mars7.tma_final])
    
    CO2_pressure=np.array([mars1.PCO2_final,mars2.PCO2_final,mars3.PCO2_final,mars4.PCO2_final,mars5.PCO2_final,mars6.PCO2_final,mars7.PCO2_final])
    RM_CO2 = np.array([mars1.CCO2RM_final,mars2.CCO2RM_final,mars3.CCO2RM_final,mars4.CCO2RM_final,mars5.CCO2RM_final,mars6.CCO2RM_final,mars7.CCO2RM_final])

    freezing_time_a=np.array([mars1_a.tma_final,mars2_a.tma_final,mars3_a.tma_final,mars4_a.tma_final,mars5_a.tma_final,mars6_a.tma_final,mars7_a.tma_final])
    
    CO2_pressure_a=np.array([mars1_a.PCO2_final,mars2_a.PCO2_final,mars3_a.PCO2_final,mars4_a.PCO2_final,mars5_a.PCO2_final,mars6_a.PCO2_final,mars7_a.PCO2_final])
    RM_CO2_a = np.array([mars1_a.CCO2RM_final,mars2_a.CCO2RM_final,mars3_a.CCO2RM_final,mars4_a.CCO2RM_final,mars5_a.CCO2RM_final,mars6_a.CCO2RM_final,mars7_a.CCO2RM_final])
    
    plt.subplot(3,1,1)
    plt.semilogx(k1,freezing_time,'s',markersize=25,color = 'indianred')
    plt.semilogx(k1,freezing_time_a,'o',markersize=25,color = 'steelblue')


    plt.semilogx(k1,freezing_time,'-',lw=3,color = 'indianred')
    plt.semilogx(k1,freezing_time_a,'-',lw=3,color = 'steelblue')

    plt.ylabel('Freezing Time (Ma)')
    plt.yticks([0.1,0.5,1.0,1.5])
    plt.text(2000,1.5,'(a)',fontweight='bold',fontsize=40)
    ax1=plt.subplot(3,1,2)
    plt.semilogx(k1,CO2_pressure/1.0e5,'s',markersize=25,color = 'indianred')
    plt.semilogx(k1,CO2_pressure_a/1.0e5,'o',markersize=25,color = 'steelblue')


    plt.semilogx(k1,CO2_pressure/1.0e5,'-',lw=3,color = 'indianred')
    plt.semilogx(k1,CO2_pressure_a/1.0e5,'-',lw=3,color = 'steelblue')

    yticks_bar=[50,100,150,200]
    plt.yticks([50,100,150,200])
    plt.ylabel(r"${P_{CO2}}$ (bar)",fontsize=30)
    plt.text(2000,160,'(b)',fontweight='bold',fontsize=40)
    ################
    ax2=ax1.twinx()
    newpos   = 0.1*np.array(yticks_bar)
    newlabels=newpos.astype(int)
    ax2.set_yticks(newpos)
    ax2.set_yticklabels(newlabels)
    ax2.yaxis.set_ticks_position('right') 
    ax2.yaxis.set_label_position('right') 
    ax2.spines['right'].set_position(('outward', 0))
    ax2.set_ylabel(r"${P_{CO2}}$ (MPa)",fontsize=30,labelpad=20)
    ###############
    #plt.xlim(0.001,1000.0)
    plt.subplot(3,1,3)
    plt.semilogx(k1,RM_CO2*1.0e6,'s',markersize=25,color = 'indianred')
    plt.semilogx(k1,RM_CO2_a*1.0e6,'o',markersize=25,color = 'steelblue')

    plt.yticks([200,400,600,800,1000,1200])
    #plt.xlim(0.001,1000.0)
    #plt.ylim(0.0,1000.0)
    plt.legend(['Bulk CO$_2$ (kg) %.2E'%CO2_mass,'%.2E'%CO2_mass_a],fontsize=25,fancybox=True,framealpha=0.7,loc=2)
    plt.ylabel(r'Mantle CO$_2$ (ppm)')

    plt.legend(['Bulk CO$_2$ (kg) %.2E'%CO2_mass,'%.2E'%CO2_mass_a],fontsize=25,fancybox=True,framealpha=0.7,loc=2)
    plt.semilogx(k1,RM_CO2*1.0e6,'-',lw=3,color = 'indianred')
    plt.semilogx(k1,RM_CO2_a*1.0e6,'-',lw=3,color = 'steelblue')
    plt.yticks([200,400,600,800,1000,1200])
    #plt.xlim(0.001,1000.0)
    #plt.ylim(0.0,1000.0)
    
    plt.ylabel(r'Mantle CO$_2$ (ppmw)')

    plt.xlabel(r'$K^\ast$')
    plt.text(2000,100,'(c)',fontweight='bold',fontsize=40)

    print( "Case 1: carbon mass,noceans of water,:",CO2_mass,n1)
    print( " Freezing time (Ma) min, max:",np.min(freezing_time),np.max(freezing_time))
    print( " CO2 pressure (bar) min, max:",np.min(CO2_pressure/1.0e5),np.max(CO2_pressure/1.0e5))

 
    print( " Mantle carbon (ppmw) min, max:",np.min(RM_CO2*1.0e6),np.max(RM_CO2*1.0e6))


    print( "Case 2: carbon mass,noceans of water,:",CO2_mass_a,n2)
    print( " Freezing time (Ma) min, max:",np.min(freezing_time_a),np.max(freezing_time_a))
    print( " CO2 pressure (bar) min, max:",np.min(CO2_pressure_a/1.0e5),np.max(CO2_pressure_a/1.0e5))

    print( " Mantle carbon (ppm) min, max:",np.min(RM_CO2_a*1.0e6),np.max(RM_CO2_a*1.0e6))

    print( " Mantle carbon (ppmw) min, max:",np.min(RM_CO2_a*1.0e6),np.max(RM_CO2_a*1.0e6))

    

def REE_plots(mars1,mars_const):
    """"""
    
    ##############################################
    # Plot: compare REE concentrations
    # 
    ##############################################
    # Create an array for labels for REE concentration
    REE=np.zeros(23)
    for ii in range (0,23):
        REE[ii]=ii
    
        REE_label=['Rb', 'Ba', 'Th', 'U','Ta', 'K', 'La', 'Ce' ,'P' , 'Sr' , 'Nd' , 'Sm' , 'Zr' ,  'Hf' , 'Eu' ,'Gd' ,  'Tb' ,  'Dy' ,  'Y' ,  'Er' ,   'Tm' ,  'Yb' ,   'Lu']


    plt.figure(figsize=(16,18))

    #plt.semilogy(REE,(mars1.BD_TL995/mars1.CI_REE),'s',color='salmon',MArkerFacecolor='None',markersize=20)
    plt.semilogy(REE,(mars1.CREEMO_final/mars1.CI_REE),'s-',color='maroon',markersize=20)
    plt.semilogy(REE,(mars1.CREEMO_98/mars1.CI_REE),'d-',color='red',markersize=20)
    plt.semilogy(REE,(mars1.CREEMO_90/mars1.CI_REE),'d-',color='darkorange',markersize=20)
    plt.semilogy(REE,(mars1.CREEMO_80/mars1.CI_REE),'d-',color='yellow',markersize=20)
    plt.semilogy(REE,(mars1.CREEMO_60/mars1.CI_REE),'d-',color='lime',markersize=20)
    plt.semilogy(REE,(mars1.CREEMO_20/mars1.CI_REE),'d-',color='turquoise',markersize=20)
    plt.semilogy(REE,(mars1.CREEMO_05/mars1.CI_REE),'d-',color='steelblue',markersize=20)
    plt.semilogy(REE,(mars1.BD_PCS4/mars1.CI_REE),'-',color='darkorange')
    plt.xticks(REE,REE_label,rotation='vertical',fontsize=30)

    plt.legend([ r'MO after 99.5$\%$ crystallization',r'98.0$\%$',r'90.0$\%$',r'80.0$\%$',r'60.0$\%$',r'20.0$\%$', r'5.0$\%$','Borg and Draper (2003)'],loc=4,fancybox=True,framealpha=0.7)

    plt.figure(figsize=(16,18))

    #plt.semilogy(REE,(mars1.BD_TL995/mars1.CI_REE),'s',color='salmon',MArkerFacecolor='None',markersize=20)
    plt.semilogy(REE,(mars1.CREERM_final/mars1.CI_REE),'s-',color='maroon',markersize=20)
    plt.semilogy(REE,(mars1.CREERM_98/mars1.CI_REE),'d-',color='red',markersize=20)
    plt.semilogy(REE,(mars1.CREERM_90/mars1.CI_REE),'d-',color='darkorange',markersize=20)
    plt.semilogy(REE,(mars1.CREERM_80/mars1.CI_REE),'d-',color='yellow',markersize=20)
    plt.semilogy(REE,(mars1.CREERM_60/mars1.CI_REE),'d-',color='lime',markersize=20)
    plt.semilogy(REE,(mars1.CREERM_20/mars1.CI_REE),'d-',color='turquoise',markersize=20)
    plt.semilogy(REE,(mars1.CREERM_05/mars1.CI_REE),'d-',color='steelblue',markersize=20)
    plt.semilogy(REE,(mars1.BD_PCS4/mars1.CI_REE),'-',color='darkorange')
    plt.xticks(REE,REE_label,rotation='vertical',fontsize=30)

    plt.legend([ r'RM after 99.5$\%$ crystallization',r'98.0$\%$',r'90.0$\%$',r'80.0$\%$',r'60.0$\%$',r'20.0$\%$', r'5.0$\%$','Borg and Draper (2003)'],loc=4,fancybox=True,framealpha=0.7)

    plt.figure(figsize=(13,15))

    msize =20
    plt.semilogy(REE,(mars1.CREEMO_final/mars1.CI_REE),'s',color='forestgreen',markersize=msize)
    
    plt.semilogy(REE,(mars1.NWA1068/mars1.CI_REE),'o',color='moccasin',markersize=msize-5)
    plt.semilogy(REE,(mars1.shergotty/mars1.CI_REE),'o',color='cornflowerblue',markersize=msize-5)
    plt.semilogy(REE,(mars1.zagami/mars1.CI_REE),'o',color='#D4B1B1',markersize=msize-5)
    plt.semilogy(REE,(mars1.all_REE_init_conc/mars1.CI_REE),"p",color='firebrick',markersize=msize)

    # plt.semilogy(REE,(mars1.CREERM_80/mars1.CI_REE),'D',color='darkorange',markersize=20)
    # #    plt.semilogy(REE,(mars1.CREERM_final/mars1.CI_REE),'o',color='darkgreen',markersize=20)
    # plt.semilogy(REE,(mars1.BD_PCS4/mars1.CI_REE),'o',MarkerFacecolor='forestgreen',markeredgecolor='forestgreen',lw=2,markersize=20)
    
    # plt.legend([ r'MO after 99.5$\%$ crystallization', 'NWA1068','Shergotty','Zagami','Initial abundance',r'RM after 80$\%$ crystallization', 'Borg and Draper (2003)'],loc=4,fancybox=True,framealpha=0.7)

    plt.semilogy(REE,(mars1.CREERM_80/mars1.CI_REE),'D',color='forestgreen',markersize=msize)
    plt.semilogy(REE,(mars1.BD_PCS4/mars1.CI_REE),'D',MarkerFacecolor='darkorange',markeredgecolor='darkorange',lw=2,alpha=0.5,markersize=msize)
    plt.semilogy(REE,(mars1.EETA79001A/mars1.CI_REE),'o',MarkerFacecolor='darkcyan',markeredgecolor='black',lw=2,markersize=msize-5)
    plt.semilogy(REE,(mars1.Y980459/mars1.CI_REE),'o',MarkerFacecolor='lightgray', markeredgecolor='black',lw=2,markersize=msize-5)
    
    plt.legend([ r'MO after 99.5$\%$ crystallization', 'NWA1068','Shergotty','Zagami','Initial abundance',r'RM after 80$\%$ crystallization', 'Borg and Draper (2003)','EETA79001A','Y980459'],loc=4,fancybox=True,framealpha=0.7)

    plt.ylabel('Concentration/Chondrite',fontsize=30)

    curve1=(mars_const.CREERM_80/mars_const.CI_REE)
    curve2=(mars_const.CREERM_90/mars_const.CI_REE)

    plt.plot(REE,curve1,'-',color='forestgreen',lw=6)
    plt.plot(REE,curve2,'-',color='forestgreen',lw=6)
    ax=plt.gca()
    ax.fill_between(REE,curve1,curve2,color='forestgreen',alpha=0.3)
    
    plt.semilogy(REE,(mars1.CREEMO_final/mars1.CI_REE),color='forestgreen')
    #plt.semilogy(REE,(mars1.CREERM_final/mars1.CI_REE),color='darkgreen')
    # plt.semilogy(REE,(mars1.NWA1068/mars1.CI_REE),'-',color='#005668')
    # plt.semilogy(REE,(mars1.shergotty/mars1.CI_REE),'-',color='darkgreen')
    # plt.semilogy(REE,(mars1.zagami/mars1.CI_REE),'-',color='darkgreen')
    #plt.semilogy(REE,(mars1.CREEMO_80/mars1.CI_REE),'--',color='steelblue')
    plt.semilogy(REE,(mars1.all_REE_init_conc/mars1.CI_REE),'-',color='firebrick')
    plt.semilogy(REE,(mars1.CREERM_80/mars1.CI_REE),'-',color='forestgreen')
    plt.semilogy(REE,(mars1.BD_PCS4/mars1.CI_REE),'-',color='darkorange')
    plt.text(4,0.025,r'Constant $F_{tl}$ RM 80 - 90 \%',fontsize=30,color='forestgreen',rotation=25)
    #plt.text(10,19,r'60\% RM + 40\% MO',fontsize=30,color='steelblue',rotation=-5)
    ax=plt.gca()
    plt.xticks(REE,REE_label,rotation='vertical',fontsize=30)

    # arrow1 = patches.FancyArrowPatch((23.2, 1.8), (23.2, 1.1), color='darkorange',mutation_scale=100)
    # arrow2 = patches.FancyArrowPatch((23.2, 1.9), (23.2, 22), color='darkorange',mutation_scale=100)

    # plt.plot(REE,curve1,'-',color='darkorange',lw=6)
    # plt.plot(REE,curve2,'-',color='darkorange',lw=6)
    # ax=plt.gca()
    # ax.fill_between(REE,curve1,curve2,color='darkorange',alpha=0.3)
    
    # plt.semilogy(REE,(mars1.CREEMO_final/mars1.CI_REE),color='forestgreen')
    # plt.semilogy(REE,(mars1.NWA1068/mars1.CI_REE),'-',color='#005668')
    # plt.semilogy(REE,(mars1.shergotty/mars1.CI_REE),'-',color='darkgreen')
    # plt.semilogy(REE,(mars1.zagami/mars1.CI_REE),'-',color='darkgreen')
    # plt.semilogy(REE,(mars1.all_REE_init_conc/mars1.CI_REE),'-',color='firebrick')
    # plt.semilogy(REE,(mars1.CREERM_80/mars1.CI_REE),'-',color='forestgreen')
    # plt.semilogy(REE,(mars1.BD_PCS4/mars1.CI_REE),'-',color='darkorange')
    # plt.semilogy(REE,(mars1.Y980459/mars1.CI_REE),'-',color='lightgray')
    # plt.semilogy(REE,(mars1.EETA79001A/mars1.CI_REE),'-',color='darkcyan')
    # plt.text(14,0.4,r'Constant $F_{tl}$ RM 80 - 90 \%',fontsize=30,color='darkorange',rotation=14)
    
    
    # ax=plt.gca()
    # plt.xticks(REE,REE_label,rotation='vertical',fontsize=30)
    
    plt.xlim ([0,24])
    arrow1 = patches.FancyArrowPatch((23.2, 1.8), (23.2, 1.1), color='forestgreen',mutation_scale=70)
    arrow2 = patches.FancyArrowPatch((23.2, 1.9), (23.2, 22), color='forestgreen',mutation_scale=70)
    ax.add_patch(arrow1)
    ax.add_patch(arrow2)
    # Create an output for data table
    data_out=np.array([REE_label,mars1.CREEMO_final*1.0e6,mars1.CREERM_80*1.0e6,mars_const.CREERM_80*1.0e6,mars1.BD_PCS4*1.0e6]).T
    print( np.shape(data_out))
    np.savetxt('Trace_elements.csv',data_out,fmt='%s',delimiter=',',header=str(['Elements','MO after 99.5%','RM after 80%','RM constant Ftl after 80%','Borg and Draper PCS4']))

def REE_plots_no_meteorites(mars1,mars_const):
    """"""
    
    ##############################################
    # Plot: compare REE concentrations
    # 
    ##############################################
    # Create an array for labels for REE concentration
    REE=np.zeros(23)
    for ii in range (0,23):
        REE[ii]=ii
    
        REE_label=['Rb', 'Ba', 'Th', 'U','Ta', 'K', 'La', 'Ce' ,'P' , 'Sr' , 'Nd' , 'Sm' , 'Zr' ,  'Hf' , 'Eu' ,'Gd' ,  'Tb' ,  'Dy' ,  'Y' ,  'Er' ,   'Tm' ,  'Yb' ,   'Lu']

    plt.figure(figsize=(16,20))

    plt.semilogy(REE,(mars1.CREEMO_final/mars1.CI_REE),'s',color='forestgreen',markersize=30)
    
    #plt.semilogy(REE,(mars1.NWA1068/mars1.CI_REE),'o',color='None',markersize=20)
    #plt.semilogy(REE,(mars1.shergotty/mars1.CI_REE),'o',color='cornflowerblue',markersize=20)
    #plt.semilogy(REE,(mars1.zagami/mars1.CI_REE),'o',color='#D4B1B1',markersize=20)
    plt.semilogy(REE,(mars1.all_REE_init_conc/mars1.CI_REE),"p",color='firebrick',markersize=30)
    plt.semilogy(REE,(mars1.CREERM_80/mars1.CI_REE),'D',color='forestgreen',markersize=30)
   
    plt.semilogy(REE,(mars1.BD_PCS4/mars1.CI_REE),'D',MarkerFacecolor='darkorange',markeredgecolor='darkorange',lw=2,alpha=0.5,markersize=30)

    #plt.semilogy(REE,(mars1.EETA79001A/mars1.CI_REE),'o',MarkerFacecolor='darkcyan',markeredgecolor='black',lw=2,markersize=20)
    #plt.semilogy(REE,(mars1.Y980459/mars1.CI_REE),'o',MarkerFacecolor='lightgray', markeredgecolor='black',lw=2,markersize=20)
    
    #plt.legend([ r'MO after 99.5$\%$ crystallization', 'NWA1068','Shergotty','Zagami','Initial abundance',r'RM after 80$\%$ crystallization', 'Borg and Draper (2003)','EETA79001A','Y980459'],loc=4,fancybox=True,framealpha=0.7)
    plt.ylabel('Concentration/Chondrite',fontsize=30)

    curve1=(mars_const.CREERM_80/mars_const.CI_REE)
    curve2=(mars_const.CREERM_90/mars_const.CI_REE)
    plt.plot(REE,curve1,'-',color='darkorange',lw=6)
    plt.plot(REE,curve2,'-',color='darkorange',lw=6)
    ax=plt.gca()
    ax.fill_between(REE,curve1,curve2,color='darkorange',alpha=0.3)
    
    plt.semilogy(REE,(mars1.CREEMO_final/mars1.CI_REE),color='forestgreen')
    #plt.semilogy(REE,(mars1.NWA1068/mars1.CI_REE),'-',color='#005668')
    #plt.semilogy(REE,(mars1.shergotty/mars1.CI_REE),'-',color='darkgreen')
    #plt.semilogy(REE,(mars1.zagami/mars1.CI_REE),'-',color='darkgreen')
    plt.semilogy(REE,(mars1.all_REE_init_conc/mars1.CI_REE),'-',color='firebrick')
    plt.semilogy(REE,(mars1.CREERM_80/mars1.CI_REE),'-',color='forestgreen')
    plt.semilogy(REE,(mars1.BD_PCS4/mars1.CI_REE),'-',color='darkorange')
    #plt.semilogy(REE,(mars1.Y980459/mars1.CI_REE),'-',color='lightgray')
    #plt.semilogy(REE,(mars1.EETA79001A/mars1.CI_REE),'-',color='darkcyan')
    #plt.text(14,0.4,r'Constant $F_{tl}$ RM 80 - 90 \%',fontsize=30,color='darkorange',rotation=14)
    
    
    ax=plt.gca()
    plt.xticks(REE,REE_label,rotation='vertical',fontsize=30)

    arrow1 = patches.FancyArrowPatch((23.2, 1.8), (23.2, 1.1), color='forestgreen',mutation_scale=100)
    arrow2 = patches.FancyArrowPatch((23.2, 1.9), (23.2, 22), color='forestgreen',mutation_scale=100)

    ax.add_patch(arrow1)
    ax.add_patch(arrow2)
    # Create an output for data table
    data_out=np.array([REE_label,mars1.CREEMO_final*1.0e6,mars1.CREERM_80*1.0e6,mars_const.CREERM_80*1.0e6,mars1.BD_PCS4*1.0e6]).T
    print( np.shape(data_out))
    np.savetxt('Trace_elements.csv',data_out,fmt='%s',delimiter=',',header=str(['Elements','MO after 99.5%','RM after 80%','RM constant Ftl after 80%','Borg and Draper PCS4']))
def smallerCore_solidus_plot():
    """Plots the solidus and adiabat"""
    #########################################################
    # Plot: Show solidus liquidus and adiabat
    # ***Need to change core size and ... 
    ###########################################################
    mars_sol=Mars()
    print( 'Mars core radius (km)',mars_sol.core/1.0e3)
    print( 'Mars planetary radius (km)',mars_sol.radius/1.0e3)
    print( 'Mars mantle thickness',(mars_sol.radius-mars_sol.core)/1.0e3)
    r=np.linspace(mars_sol.core,mars_sol.radius) #radius in m
    r_mantle_km=(r-mars_sol.core)*1.0e-3
    PGPa=mars_sol.depth2PGPa(r)
    solidus=mars_sol.solidus(r)
    liquidus=mars_sol.liquidus(r)
    front=mars_sol.freezing_front(r)
    rad1=mars_sol.solid_radius(2100.0)

    T1=mars_sol.adiabat(2100.0,r)
    rad2=mars_sol.solid_radius(1600.0)

    T2=mars_sol.adiabat(1550.0,r)
    temp_label=[1000,1400,1800,2200,2600,3000]
    
    plt.figure(figsize=(19,12))
    #
    plt.subplot(1,2,1)
    ax = plt.gca()
    
    plt.plot(liquidus,r_mantle_km,'--',color='firebrick',linewidth=4)
    plt.plot(front,r_mantle_km,'-.',color='teal',linewidth=4)
    plt.plot(solidus,r_mantle_km,'-',color='darkslategray',linewidth=4)
    plt.xticks(temp_label)
    ax.fill_betweenx(r_mantle_km,front, solidus, where=front>= solidus, alpha=0.7,  facecolor='teal',)
    

    plt.legend(['Liquidus','Front','Solidus'],loc=3,fancybox=True,framealpha=0.7)

    plt.plot(T1,r_mantle_km,'-k',linewidth=4)
    plt.plot(T2,r_mantle_km,'-k',linewidth=4)
    plt.plot(2300,450.0,'o',color='tomato',markersize=20,alpha=0.7)
    plt.plot(1580,1715.0,'o',color='tomato',markersize=20,alpha=0.7)
    # plt.plot(2050,146.0,'o',color='tomato',markersize=20,alpha=0.7) # plot from 
    # plt.plot(1550,1776.0,'o',color='tomato',markersize=20,alpha=0.7)
    #plt.ylim(1395.0,3390.0)
    plt.ylim(0.0,2000.0)
    # plt.xlim(1000.0,2000.0)
    plt.text(1580,1050,r'1550$^\mathrm{o}$ adiabat',rotation=-85,fontsize=30)
    plt.text(2150,1050,r'2050$^\mathrm{o}$ adiabat',rotation=-85,fontsize=30)
    plt.xlabel(r'Temperature ($^\mathrm{o}$C)',fontsize=30)
    plt.ylabel('Height above CMB (km)',fontsize=30)

    #plt.text(1400,150,'(a)',fontsize=60,fontweight='bold')
    plt.text(2400,1850,'(a)',fontsize=60,fontweight='bold')
    FFL=70 #km thickness of the FF
    rect=patches.Rectangle((1000,1650),2200, FFL, color='firebrick',alpha=0.4)
    ax.add_patch(rect)
    plt.text(2200,1650,'FF %3.0f km thick'%FFL)

    plt.subplot(1,2,2)
    mars_sol.smallerCore_radius_temperature_analytical(plot=True)
    plt.xticks(temp_label)
    plt.ylim(0.0,2000.0)

    #plt.text(1400,150,'(b)',fontsize=60,fontweight='bold')
    plt.text(2400,1850,'(b)',fontsize=60,fontweight='bold')

    #
    #Plot dadT if neede
    #plt.subplot(1,3,1)
    #T=np.linspace(1300.0,2150.0,100)
    #dadT=0.0*T
    #for ii in range (0,99):
    #            dadT[ii]=mars_sol.dadT_analytical(T[ii])
    #plt.plot(T,dadT/1.0e3,'or')
    
    del mars_sol
    
def ET08_solidus_plot():
    """Plots the solidus and adiabat"""
    #########################################################
    # Plot: Show solidus liquidus and adiabat
    # 
    ###########################################################
    mars_sol=Mars()
    print ('Mars core radius (km)',mars_sol.core/1.0e3)
    print ('Mars planetary radius (km)',mars_sol.radius/1.0e3)
    print ('Mars mantle thickness',(mars_sol.radius-mars_sol.core)/1.0e3)
    r=np.linspace(mars_sol.core,mars_sol.radius) #radius in m
    r_mantle_km=(r-mars_sol.core)*1.0e-3
    PGPa=mars_sol.depth2PGPa(r)
    solidus=mars_sol.solidus(r)
    liquidus=mars_sol.liquidus(r)
    front=mars_sol.freezing_front(r)
    rad1=mars_sol.solid_radius(2100.0)

    T1=mars_sol.adiabat(2050.0,r)
    rad2=mars_sol.solid_radius(1600.0)

    
    T2=mars_sol.adiabat(1550.0,r)
    temp_label=[1300,1600,2000,2400]
    
    plt.figure(figsize=(16,10))
    #
    plt.subplot(1,2,1)
    ax = plt.gca()
    
    plt.plot(liquidus,r_mantle_km,'--',color='firebrick',linewidth=4)
    plt.plot(front,r_mantle_km,'-.',color='teal',linewidth=4)
    plt.plot(solidus,r_mantle_km,'-',color='darkslategray',linewidth=4)
    plt.xticks(temp_label)
    ax.fill_betweenx(r_mantle_km,front, solidus, where=front>= solidus, alpha=0.7,  facecolor='teal',)
    

    plt.legend(['Liquidus','Front','Solidus'],loc=3,fancybox=True,framealpha=0.7)

    plt.plot(T1,r_mantle_km,'-k',linewidth=4)
    plt.plot(T2,r_mantle_km,'-k',linewidth=4)
    plt.plot(2250,90.0,'o',color='tomato',markersize=20,alpha=0.7)
    plt.plot(1590,1320.0,'o',color='tomato',markersize=20,alpha=0.7)
    #plt.ylim(1395.0,3390.0)
    plt.ylim(0.0,1600.0)
    
    plt.text(1620,550,r'1550$^\mathrm{o}$ adiabat',rotation=-85,fontsize=30)
    plt.text(2170,550,r'2050$^\mathrm{o}$ adiabat',rotation=-85,fontsize=30)
    plt.xlabel(r'Temperature ($^\mathrm{o}$C)',fontsize=30)
    plt.ylabel('Height above CMB (km)',fontsize=30)

    #plt.text(1400,150,'(a)',fontsize=60,fontweight='bold')
    plt.text(2500,1450,'(a)',fontsize=60,fontweight='bold')
    FFL=70 #km thickness of the FF
    rect=patches.Rectangle((1000,1250),1800, FFL, color='firebrick',alpha=0.4)
    ax.add_patch(rect)
    plt.text(2200,1250,'FF %3.0f km thick'%FFL)

    plt.subplot(1,2,2)
    mars_sol.radius_temperature_analytical(plot=True)
    plt.xticks(temp_label)
    plt.ylim(0.0,1600.0)

    #plt.text(1400,150,'(b)',fontsize=60,fontweight='bold')
    plt.text(2500,1450,'(b)',fontsize=60,fontweight='bold')

    #
    #Plot dadT if neede
    #plt.subplot(1,3,1)
    #T=np.linspace(1300.0,2150.0,100)
    #dadT=0.0*T
    #for ii in range (0,99):
    #            dadT[ii]=mars_sol.dadT_analytical(T[ii])
    #plt.plot(T,dadT/1.0e3,'or')
    
    del mars_sol

def Duncan_solidus_plot():
    """Plots the solidus and adiabat"""
    #########################################################
    # Plot: Show solidus liquidus and adiabat
    # 
    ###########################################################
    mars_sol=Mars()
    print ('Mars core radius (km)',mars_sol.core/1.0e3)
    print ('Mars planetary radius (km)',mars_sol.radius/1.0e3)
    print ('Mars mantle thickness',(mars_sol.radius-mars_sol.core)/1.0e3)
    r=np.linspace(mars_sol.core,mars_sol.radius) #radius in m
    r_mantle_km=(r-mars_sol.core)*1.0e-3
    PGPa=mars_sol.depth2PGPa(r)
    solidus=mars_sol.solidus(r)
    liquidus=mars_sol.liquidus(r)
    front=mars_sol.freezing_front(r)
    rad1=mars_sol.solid_radius(2100.0)

    T1=mars_sol.adiabat(2250.0,r)
    rad2=mars_sol.solid_radius(1600.0)

    
    T2=mars_sol.adiabat(1750.0,r)
    temp_label=[1600,2000,2400,2800]
    
    plt.figure(figsize=(16,10))
    #
    plt.subplot(1,2,1)
    ax = plt.gca()
    
    plt.plot(liquidus,r_mantle_km,'--',color='firebrick',linewidth=4)
    plt.plot(front,r_mantle_km,'-.',color='teal',linewidth=4)
    plt.plot(solidus,r_mantle_km,'-',color='darkslategray',linewidth=4)
    plt.xticks(temp_label)
    ax.fill_betweenx(r_mantle_km,front, solidus, where=front>= solidus, alpha=0.7,  facecolor='teal',)
    

    plt.legend(['Liquidus','Front','Solidus'],loc=3,fancybox=True,framealpha=0.7)

    plt.plot(T1,r_mantle_km,'-k',linewidth=4)
    plt.plot(T2,r_mantle_km,'-k',linewidth=4)
    plt.plot(2465,330.0,'o',color='tomato',markersize=20,alpha=0.7)
    plt.plot(1820,1456.0,'o',color='tomato',markersize=20,alpha=0.7)
    #plt.ylim(1395.0,3390.0)
    plt.ylim(0.0,1900.0)
    plt.xlim(1400.0,3000.0)
    
    plt.text(1720,550,r'1750$^\mathrm{o}$ adiabat',rotation=-85,fontsize=30)
    plt.text(2370,550,r'2250$^\mathrm{o}$ adiabat',rotation=-85,fontsize=30)
    plt.xlabel(r'Temperature ($^\mathrm{o}$C)',fontsize=30)
    plt.ylabel('Height above CMB (km)',fontsize=30)

    #plt.text(1400,150,'(a)',fontsize=60,fontweight='bold')
    plt.text(2700,1650,'(a)',fontsize=60,fontweight='bold')
    FFL=150 #km thickness of the FF
    rect=patches.Rectangle((1400,1310),1600, FFL, color='firebrick',alpha=0.4)
    ax.add_patch(rect)
    plt.text(2350,1350,'FF %3.0f km thick'%FFL)

    plt.subplot(1,2,2)
    mars_sol.Duncan_radius_temperature_analytical(plot=True)
    plt.xticks(temp_label)
    plt.ylim(0.0,1900.0)

    #plt.text(1400,150,'(b)',fontsize=60,fontweight='bold')
    plt.text(2700,1650,'(b)',fontsize=60,fontweight='bold')

    #
    #Plot dadT if neede
    #plt.subplot(1,3,1)
    #T=np.linspace(1300.0,2150.0,100)
    #dadT=0.0*T
    #for ii in range (0,99):
    #            dadT[ii]=mars_sol.dadT_analytical(T[ii])
    #plt.plot(T,dadT/1.0e3,'or')
    
    del mars_sol
    
def NewCore_Duncan_solidus_plot():
    """Plots the solidus and adiabat"""
    #########################################################
    # Plot: Show solidus liquidus and adiabat
    # 
    ###########################################################
    mars_sol=Mars()
    print ('Mars core radius (km)',mars_sol.core/1.0e3)
    print ('Mars planetary radius (km)',mars_sol.radius/1.0e3)
    print ('Mars mantle thickness',(mars_sol.radius-mars_sol.core)/1.0e3)
    r=np.linspace(mars_sol.core,mars_sol.radius) #radius in m
    r_mantle_km=(r-mars_sol.core)*1.0e-3
    PGPa=mars_sol.depth2PGPa(r)
    solidus=mars_sol.solidus(r)
    liquidus=mars_sol.liquidus(r)
    front=mars_sol.freezing_front(r)
    rad1=mars_sol.solid_radius(2100.0)

    T1=mars_sol.adiabat(2050.0,r)
    rad2=mars_sol.solid_radius(1600.0)

    
    T2=mars_sol.adiabat(1550.0,r)
    temp_label=[1200,1600,2000,2400,2800]
    
    plt.figure(figsize=(16,10))
    #
    plt.subplot(1,2,1)
    ax = plt.gca()
    
    plt.plot(liquidus,r_mantle_km,'--',color='firebrick',linewidth=4)
    plt.plot(front,r_mantle_km,'-.',color='teal',linewidth=4)
    plt.plot(solidus,r_mantle_km,'-',color='darkslategray',linewidth=4)
    plt.xticks(temp_label)
    ax.fill_betweenx(r_mantle_km,front, solidus, where=front>= solidus, alpha=0.7,  facecolor='teal',)
    

    plt.legend(['Liquidus','Front','Solidus'],loc=3,fancybox=True,framealpha=0.7)

    plt.plot(T1,r_mantle_km,'-k',linewidth=4)
    plt.plot(T2,r_mantle_km,'-k',linewidth=4)
    plt.plot(2245,90.0,'o',color='tomato',markersize=20,alpha=0.7)
    plt.plot(1590,1310.0,'o',color='tomato',markersize=20,alpha=0.7)
    #plt.ylim(1395.0,3390.0)
    plt.ylim(0.0,1600.0)
    plt.xlim(1200.0,2800.0)
    
    plt.text(1500,550,r'1550$^\mathrm{o}$ adiabat',rotation=-85,fontsize=30)
    plt.text(2150,550,r'2050$^\mathrm{o}$ adiabat',rotation=-85,fontsize=30)
    plt.xlabel(r'Temperature ($^\mathrm{o}$C)',fontsize=30)
    plt.ylabel('Height above CMB (km)',fontsize=30)

    #plt.text(1400,150,'(a)',fontsize=60,fontweight='bold')
    plt.text(2450,1450,'(a)',fontsize=60,fontweight='bold')
    FFL=60 #km thickness of the FF
    rect=patches.Rectangle((1200,1250),1600, FFL, color='firebrick',alpha=0.4)
    ax.add_patch(rect)
    plt.text(2120,1250,'FF %3.0f km thick'%FFL)

    plt.subplot(1,2,2)
    mars_sol.Duncan_NewCore_radius_temperature_analytical(plot=True)
    plt.xticks(temp_label)
    plt.ylim(0.0,1600.0)

    #plt.text(1400,150,'(b)',fontsize=60,fontweight='bold')
    plt.text(2450,1450,'(b)',fontsize=60,fontweight='bold')

    #
    #Plot dadT if neede
    #plt.subplot(1,3,1)
    #T=np.linspace(1300.0,2150.0,100)
    #dadT=0.0*T
    #for ii in range (0,99):
    #            dadT[ii]=mars_sol.dadT_analytical(T[ii])
    #plt.plot(T,dadT/1.0e3,'or')
    
    del mars_sol
    
def Stanley_solidus_plot():
    """Plots the solidus and adiabat"""
    #########################################################
    # Plot: Show solidus liquidus and adiabat
    # 
    ###########################################################
    mars_sol=Mars()
    print ('Mars core radius (km)',mars_sol.core/1.0e3)
    print ('Mars planetary radius (km)',mars_sol.radius/1.0e3)
    print ('Mars mantle thickness',(mars_sol.radius-mars_sol.core)/1.0e3)
    r=np.linspace(mars_sol.core,mars_sol.radius) #radius in m
    r_mantle_km=(r-mars_sol.core)*1.0e-3
    PGPa=mars_sol.depth2PGPa(r)
    solidus=mars_sol.solidus(r)
    liquidus=mars_sol.liquidus(r)
    front=mars_sol.freezing_front(r)
    rad1=mars_sol.solid_radius(2100.0)

    T1=mars_sol.adiabat(2050.0,r)
    rad2=mars_sol.solid_radius(1600.0)

    
    T2=mars_sol.adiabat(1550.0,r)
    temp_label=[1200,1600,2000,2400,2800]
    
    plt.figure(figsize=(16,10))
    #
    plt.subplot(1,2,1)
    ax = plt.gca()
    
    plt.plot(liquidus,r_mantle_km,'--',color='firebrick',linewidth=4)
    plt.plot(front,r_mantle_km,'-.',color='teal',linewidth=4)
    plt.plot(solidus,r_mantle_km,'-',color='darkslategray',linewidth=4)
    plt.xticks(temp_label)
    ax.fill_betweenx(r_mantle_km,front, solidus, where=front>= solidus, alpha=0.7,  facecolor='teal',)
    

    plt.legend(['Liquidus','Front','Solidus'],loc=3,fancybox=True,framealpha=0.7)

    plt.plot(T1,r_mantle_km,'-k',linewidth=4)
    plt.plot(T2,r_mantle_km,'-k',linewidth=4)
    plt.plot(2245,90.0,'o',color='tomato',markersize=20,alpha=0.7)
    plt.plot(1590,1310.0,'o',color='tomato',markersize=20,alpha=0.7)
    #plt.ylim(1395.0,3390.0)
    plt.ylim(0.0,1600.0)
    plt.xlim(1200.0,2800.0)
    
    plt.text(1500,550,r'1550$^\mathrm{o}$ adiabat',rotation=-85,fontsize=30)
    plt.text(2150,550,r'2050$^\mathrm{o}$ adiabat',rotation=-85,fontsize=30)
    plt.xlabel(r'Temperature ($^\mathrm{o}$C)',fontsize=30)
    plt.ylabel('Height above CMB (km)',fontsize=30)

    #plt.text(1400,150,'(a)',fontsize=60,fontweight='bold')
    plt.text(2450,1450,'(a)',fontsize=60,fontweight='bold')
    FFL=60 #km thickness of the FF
    rect=patches.Rectangle((1200,1250),1600, FFL, color='firebrick',alpha=0.4)
    ax.add_patch(rect)
    plt.text(2120,1250,'FF %3.0f km thick'%FFL)

    plt.subplot(1,2,2)
    mars_sol.Stanley_radius_temperature_analytical(plot=True)
    plt.xticks(temp_label)
    plt.ylim(0.0,1600.0)

    #plt.text(1400,150,'(b)',fontsize=60,fontweight='bold')
    plt.text(2450,1450,'(b)',fontsize=60,fontweight='bold')

    #
    #Plot dadT if neede
    #plt.subplot(1,3,1)
    #T=np.linspace(1300.0,2150.0,100)
    #dadT=0.0*T
    #for ii in range (0,99):
    #            dadT[ii]=mars_sol.dadT_analytical(T[ii])
    #plt.plot(T,dadT/1.0e3,'or')
    
    del mars_sol
    
def tau_calc():
    """This function calculates the ranges of
    compaction time for a martian MO"""
    L = 130e3 #m, thickness of FF
    rho = 4287.0#kg/m^3 density of mantle
    g = 3.711 # m/s^2, surface gravity of Mars
    c1 = 9.05e13 # Pas/m^2 frictional resistance
    c2 = 9.05e15 # Pas/m^2 frictional resistance
    tau1_sec=L*c1/rho/g
    tau2_sec=L*c2/rho/g
    sec2Ma=1.0/(365*24*3600*1.0e6) # seconds to Ma
    tau1=tau1_sec*sec2Ma
    tau2=tau2_sec*sec2Ma
    print(  '#####################################')
    print(  ' Estimates for compaction time in Ma:',tau1,tau2)
    print(  '#####################################')
def compare_compaction(tau,redox):
    """This function reads the values of time averaged compaction
    from a data file and plots them against compaction times"""
    n1=np.size(tau)
    n2=np.size(redox)
    Ftl=np.zeros([n1,n2])
    Freezing=np.zeros([n1,n2])
    MCO2RM=np.zeros([n1,n2])
    MH2ORM=np.zeros([n1,n2])
    fname1='Ftl_averaged_k_tau.csv'
    Ftl=np.loadtxt(fname1,delimiter=",")
    #Header 'Time averaged F_tl values. Data in columns correspond to redox factors [0.1,1.0,10.0,100.0,1000.0], data in rows correspond to compaction times [1.0,0.5,0.3,0.2,0.1,0.01,0.001] Ma'
    fname2='Freezing_time_k_tau.csv'
    Freezing=np.loadtxt(fname2,delimiter=",")
    # Header :'Time taken for 99.5% crystallization. Data in columns correspond to redox factors [0.1,1.0,10.0,100.0,1000.0], data in rows correspond to compaction times [1.0,0.5,0.3,0.2,0.1,0.01,0.001] Ma'
    fname3='MCO2RM_averaged_k_tau.csv'
    MCO2RM=np.loadtxt(fname3,delimiter=",")
    fname4='MH2ORM_averaged_k_tau.csv'
    MH2ORM=np.loadtxt(fname4,delimiter=",")
    GEL=MH2ORM/1.0e3/144.4e12  #GEL in m
    plt.figure(figsize=(12,16))
    plt.subplot(2,1,1)
    plt.semilogx(tau,Ftl[:,2],'s',mfc='forestgreen',markersize=30)
    plt.semilogx(tau,Ftl[:,2],'-',color='forestgreen',lw=3)
    plt.text(0.001,0.3,'(a)',fontsize=60,fontweight='bold')

    plt.ylim(0,0.35)
    plt.ylabel(r'Time averaged $F_{tl}$',fontsize=30)
    plt.subplot(2,1,2)
    plt.semilogx(tau,GEL[:,2],'s',mfc='forestgreen',markersize=30)
    plt.semilogx(tau,GEL[:,2],'-',color='forestgreen',lw=3)
    plt.ylabel(r'H$_2$O GEL (m)',fontsize=30)
    plt.xlabel(r'$\tau$ (Ma)',fontsize=30)
    plt.text(0.001,5200,'(b)',fontsize=60,fontweight='bold')
    plt.ylim(1000,6000)
    
    plt.figure(figsize=(12,16))
    plt.subplot(2,1,1)
    
    plt.semilogx(tau,MCO2RM[:,4],'-',color='dimgray',lw=3)
    plt.semilogx(tau,MCO2RM[:,3],'--',color='darkgray',lw=3)
    plt.semilogx(tau,MCO2RM[:,2],'-.',color='lightsteelblue',lw=3)
    plt.semilogx(tau,MCO2RM[:,1],':',color='cornflowerblue',lw=3)
    plt.semilogx(tau,MCO2RM[:,0],linestyle=(0, (3, 10, 1, 10, 1, 10)),color='steelblue',lw=3)
    
    plt.legend([r'$K^\ast =$%3.2f'%redox[4],r'$K^\ast =$%3.2f'%redox[3],r'$K^\ast =$%3.2f'%redox[2],r'$K^\ast =$%3.2f'%redox[1],r'$K^\ast =$%3.2f'%redox[0]],fancybox=True,framealpha=0.7,loc=2)
    
    plt.semilogx(tau,MCO2RM[:,4],'o',mfc='dimgray',markersize=30)
    plt.semilogx(tau,MCO2RM[:,3],'o',mfc='darkgray',markersize=30)
    plt.semilogx(tau,MCO2RM[:,2],'o',mfc='lightsteelblue',markersize=30)
    plt.semilogx(tau,MCO2RM[:,1],'o',mfc='cornflowerblue',markersize=30)
    plt.semilogx(tau,MCO2RM[:,0],'o',mfc='steelblue',markersize=30)
    #plt.xlabel(r'$\tau$ (Ma)',fontsize=30)
    plt.ylabel('Mantle CO$_2$ mass (kg)',fontsize=30)
    plt.text(0.001,1.7e20,'(a)',fontsize=60,fontweight='bold')

    plt.subplot(2,1,2)
    plt.semilogx(tau,Freezing[:,4],'-',color='dimgray',lw=3)
    plt.semilogx(tau,Freezing[:,3],'--',color='darkgray',lw=3)
    plt.semilogx(tau,Freezing[:,2],'-.',color='lightsteelblue',lw=3)
    plt.semilogx(tau,Freezing[:,1],':',color='cornflowerblue',lw=3)
    plt.semilogx(tau,Freezing[:,0],linestyle=(0, (3, 10, 1, 10, 1, 10)),color='steelblue',lw=3)
    
    plt.semilogx(tau,Freezing[:,4],'o',mfc='dimgray',markersize=30)
    plt.semilogx(tau,Freezing[:,3],'o',mfc='darkgray',markersize=30)
    plt.semilogx(tau,Freezing[:,2],'o',mfc='lightsteelblue',markersize=30)
    plt.semilogx(tau,Freezing[:,1],'o',mfc='cornflowerblue',markersize=30)
    plt.semilogx(tau,Freezing[:,0],'o',mfc='steelblue',markersize=30)
    plt.xlabel(r'$\tau$ (Ma)',fontsize=30)
    plt.ylabel('Time to crystallization (Ma)', fontsize=30)
    plt.text(0.001,0.7,'(b)',fontsize=60,fontweight='bold')

