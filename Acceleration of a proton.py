#  Calculating the acceleration of a proton

from scipy.constants import e, m_p
import numpy as np


def calculate_acceleration_of_proton(q,E,v,B):
  
  print('arguments: ',q,E,v,B)
  
  x = np.array([1,0,0])
  y = np.array([0,1,0])
  z = np.array([0,0,1])
  
  print('starting vectors: ',x,y,z)
 
  a = (x + y) / np.sqrt(2)
  
  print('parallel vector: ',a)
  
  # q is the charge on the electron
  q = e 
  
  # E electric field
  E = E * y
  
  # v is velocity
  v = v * a
  
  # B magnetic field
  B = B * z
  
  print('new vectors: ',E,v,B)

  force = q * (E + ( np.cross(v,B) ) )
#  force = q * E + q * v * B
  
  print('v*B: ',np.cross(v,B))
  print('force: ',force)

  mass = m_p # mass of a proton

  acceleration = force/mass
  
  print('acceleration in x,y,z=',acceleration)
  
  acceleration_magnitude = np.sqrt((acceleration[0])**2 + (acceleration[1])**2 + (acceleration[2]**2))

  return acceleration_magnitude
         
print (calculate_acceleration_of_proton(e,100,100,1))











