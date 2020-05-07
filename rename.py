import sys
sys.path.append('./')
import os
import glob
#from tasks import gaincal
#from tasks import bandpass
#from tasks import fluxscale
#from tasks import applycal

r='fourthround'
#bu='backup'

number=['18']
#number=['2','3','4','5','6','7','8','9','10','11','12','13','17','18','19','20','21','22']
#sessions=['14','15'] #different gain calibrator ; s16 flagged since whole spw4 is flagged
#path='./'+str(number)+'s/'

for s in number:
    path='./'+str(s)+'s/'
    os.rename(str(path)+'delays.cal', str(path)+'delays-'+str(r)+'.cal')
    os.rename(str(path)+'bpphase.gcal', str(path)+'bpphase-'+str(r)+'.gcal')
    os.rename(str(path)+'bandpass.bcal', str(path)+'bandpass-'+str(r)+'.bcal')
    os.rename(str(path)+'intphase.gcal', str(path)+'intphase-'+str(r)+'.gcal')
    os.rename(str(path)+'scanphase.gcal', str(path)+'scanphase-'+str(r)+'.gcal')
    os.rename(str(path)+'amp.gcal', str(path)+'amp-'+str(r)+'.gcal')
#   os.rename(str(path)+'spw4-session'+str(s)+'.ms.contsub', str(path)+'spw4-session'+str(s)+'-'+str(bu)+'.ms.contsub')
    os.rename(str(path)+'spw4-session'+str(s)+'.ms.cont', str(path)+'spw4-session'+str(s)+'-'+str(bu)+'.ms.cont')

