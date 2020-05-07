number='2'

 

plotants(vis='spw4-session'+str(number)+'.ms', figfile='1-ant_loc.png')

gencal(vis='spw4-session'+str(number)+'.ms', caltable='antpos.cal', caltype='antpos', antenna='')

from recipes import tec_maps
tec_image, tec_rms_image, plotname=tec_maps.create(vis='spw4-session'+str(number)+'.ms',doplot=True)

gencal(vis='spw4-session'+str(number)+'.ms', caltype='tecim', caltable='tecim.cal', infile='spw4-session'+str(number)+'.ms.IGS_TEC.im')

gencal(vis='spw4-session'+str(number)+'.ms', caltable='gaincurve.cal', caltype='gceff')

myTau = plotweather(vis='spw4-session'+str(number)+'.ms', doPlot=True)

gencal(vis='spw4-session'+str(number)+'.ms', caltable='opacity.cal', caltype='opac', spw='', parameter=myTau)

setjy(vis='spw4-session'+str(number)+'.ms', field='1331+305=3C286', spw='', scalebychan=True, model='3C286_L.im')


##------------------------------------------------------
##
##
##          start here after flagging 
##
##
##
##------------------------------------------------------



gaincal(vis='spw4-session'+str(number)+'.ms', caltable='delays.cal', field='1331+305=3C286', refant='ea06', gaintype='K', solint='int', gaintable=['antpos.cal','gaincurve.cal','opacity.cal', 'tecim.cal'])

gaincal(vis='spw4-session'+str(number)+'.ms', caltable='bpphase.gcal', field='1331+305=3C286', refant='ea06', calmode='p', gaintable=['antpos.cal','gaincurve.cal','opacity.cal', 'tecim.cal','delays.cal'])

bandpass(vis='spw4-session'+str(number)+'.ms', caltable='bandpass.bcal', field='1331+305=3C286', refant='ea06', solint='inf', gaintable=['antpos.cal','gaincurve.cal','opacity.cal', 'tecim.cal','delays.cal', 'bpphase.gcal'])




'''### not on-the-fly applying ###''' 
###applycal(vis='spw4-session'+str(number)+'.ms', field='J1316-3338',gaintable=['antpos.cal','gaincurve.cal','opacity.cal','tecim.cal', 'delays.cal', 'bpphase.gcal'],gainfield=['','','','J1316-3338','J1316-3338'], calwt=False) 





'''### Gain Calibration ###'''


gaincal(vis='spw4-session'+str(number)+'.ms', caltable='intphase.gcal', field='1331+305=3C286,J1316-3338', refant='ea06', solint='int',minsnr=3.0, calmode='p', gaintable=['antpos.cal','gaincurve.cal','opacity.cal', 'tecim.cal', 'delays.cal', 'bandpass.bcal'])

gaincal(vis='spw4-session'+str(number)+'.ms', caltable='scanphase.gcal', field='1331+305=3C286,J1316-3338', refant='ea06', solint='inf', minsnr=2.0, calmode='p', gaintable=['antpos.cal','gaincurve.cal','opacity.cal', 'tecim.cal', 'delays.cal', 'bandpass.bcal'])

gaincal(vis='spw4-session'+str(number)+'.ms', caltable='amp.gcal', field='1331+305=3C286,J1316-3338', refant='ea06', solint='inf', minsnr=2.0, calmode='p', gaintable=['antpos.cal','gaincurve.cal','opacity.cal', 'tecim.cal', 'delays.cal', 'bandpass.bcal', 'intphase.gcal'])

fluxscale(vis='spw4-session'+str(number)+'.ms', caltable='amp.gcal', fluxtable='flux.cal', reference='1331+305=3C286', incremental=True)


'''### Apply ###'''

##gain/phase
applycal(vis='spw4-session'+str(number)+'.ms', 
        field='J1316-3338', 
        gaintable=['antpos.cal','tecim.cal', 'gaincurve.cal','opacity.cal', 'delays.cal', 'bandpass.bcal', 'intphase.gcal', 'amp.gcal', 'flux.cal'], 
        gainfield=['','','','','1331+305=3C286','1331+305=3C286','J1316-3338','J1316-3338','J1316-3338'],
        calwt=False)

##bandpass/flux
applycal(vis='spw4-session'+str(number)+'.ms', 
        field='1331+305=3C286', 
        gaintable=['antpos.cal', 'tecim.cal', 'gaincurve.cal','opacity.cal', 'delays.cal', 'bandpass.bcal', 'intphase.gcal', 'amp.gcal', 'flux.cal'], 
        gainfield=['','','','','1331+305=3C286','1331+305=3C286','1331+305=3C286','1331+305=3C286','1331+305=3C286'],
        calwt=False)


##bandpass and gain applying to target field IDs

applycal(vis='spw4-session'+str(number)+'.ms', 
        field='M83-S, M83-SE, M83-SW, M83-W, M83-C, M83-E, M83-NE, M83-NC, M83-NW, M83-N', 
        gaintable=['antpos.cal','tecim.cal', 'gaincurve.cal','opacity.cal', 'delays.cal', 'bandpass.bcal', 'intphase.gcal', 'amp.gcal', 'flux.cal'], 
        gainfield=['','','','','1331+305=3C286','1331+305=3C286','J1316-3338','J1316-3338','J1316-3338'],
        calwt=False)




