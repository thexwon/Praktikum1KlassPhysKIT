"""
Parameters required for task 4.

The momentum of inertia (I), mass (m), and distance (ell) of the center of mass 
to the pivotal point of the physical pendulum. All quantities have been derived 
from direct parameter estimates and rounded within their estimated uncertainties. 
They have been derived assuming simplified shapes of the corresponding objects, 
e.g. the smartphone has been approximated by a homogeneous box. All quantities 
are given in SI units.   
"""

I = 0.23523                  # Momentum of inertia in kg*m**2
I_UPPER = 0.2378             # +uncertainty
I_LOWER = 0.2328             # -uncertatiny

m = 0.789                    # Mass of the pendulum in kg
m_UPPER = 0.794              # +uncertainty
m_LOWER = 0.784              # -uncertainty

ell = 0.473                  # Distance of the center of mass from the pivotal point of the pendulum in m 0.473
ell_UPPER = 0.480            # +uncertainty
ell_LOWER = 0.466            # -uncertainty

__version__ = 1.0
