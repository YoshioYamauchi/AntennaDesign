
# This script creates a figure represening which direction the antenna
# most receives signal.

import numpy as np
import matplotlib.pyplot as plt
import time
import datetime
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc( 'text', usetex = True )
plt.close()
plt.close()
plt.close()

## CONSTANTS #####################
k = 3.
W1 = 1.
k0d = np.pi
theta_u = np.pi * 2./3
theta_s = np.pi * 1./3
coeff = np.array( [[ np.exp( -1j * k0d * np.cos( theta_s )), np.exp( -2j * k0d * np.cos( theta_s )) ],
                   [ np.exp( -1j * k0d * np.cos( theta_u )), np.exp( -2j * k0d * np.cos( theta_u )) ]] )
rh = np.array( [[ k ], [ 0 ]] ) - np.array( [[ W1 ], [ W1 ]] )

theta = np.linspace( 0, np.pi, 300 )
W2, W3 = np.linalg.inv( coeff ).dot( rh )
##################################

def _unvectorized_D( theta ) :
    return np.abs( W1 + W2 * np.exp( -1j * k0d * np.cos( theta )) + W3 * np.exp( -2j * k0d * np.cos( theta )))

def D( theta ):
    return np.vectorize( _unvectorized_D )( theta )


## PLOT 1 #############################################
fig1 = plt.figure()
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
## ax1 ##############
ax1 = fig1.add_subplot( 111, projection = 'polar' )
ax1.plot( theta, D( theta ))
ax1.set_rmax( 4 )
ax1.set_rticks([0.5, 1, 1.5, 2])  # less radial ticks
ax1.set_rlabel_position(-22.5)  # get radial labels away from plotted line
ax1.grid( True )
ax1.set_thetamin(0)
ax1.set_thetamax(180)
# plt.legend( loc='best' )
#####################
plt.tight_layout ()
# plt.subplots_adjust ( left = 0.12, right = 0.90, bottom = 0.11,
#                       top = 0.88, wspace = 0.20, hspace = 0.34 )
ts = datetime.datetime.now()
filename = 'fig{}.jpg'.format( ts.strftime("%Y-%m-%d_%H-%M-%S") )
fig1.savefig( '../Figures01/' + filename  )
plt.show()
###########################################################
