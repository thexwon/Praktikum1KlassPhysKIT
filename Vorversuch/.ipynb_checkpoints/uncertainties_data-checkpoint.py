"""
Uncertainties of the data points.

 * x_errors : The uncertainty in x we have estimated from a measurement of 
              intercepts T from the full time series RawData.csv, taking the 
              down-sampling by 10 into account. 
              
 * y_errors : The uncertainty in y we have estimated from a 5 min lasting 
              empty measurement for which we have placed the smartphone 
              resting on the lab floor.  
"""

x_errors = 0.0125                                # Uncertainty in x (s)
y_errors = 0.02                                  # Uncertainty in y (m/s**2)

__version__ = 1.0
