# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2019 replay file
# Internal Version: 2018_09_24-13.41.51 157541
# Run by nidish on Tue Mar 17 16:00:21 2020
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(1.36719, 1.36719), width=201.25, 
    height=135.625)
session.viewports['Viewport: 1'].makeCurrent()
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
execPyFile(
    '/home/nidish/Software/Abaqus2019/SIMULIA/CAE/2019/linux_a64/code/python2.7/lib/noGuiInteractive.pyc', 
    __main__.__dict__)
#: The model database "/home/nidish/Documents/Academics/RESEARCH/INTRED_STUDY/ABAQUS_MODELS/HOLEPLATE/MATEX/../HOLEPLATE.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: The model database "/home/nidish/Documents/Academics/RESEARCH/INTRED_STUDY/ABAQUS_MODELS/HOLEPLATE/MATEX/../HOLEPLATE.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
print 'RT script done'
#: RT script done
