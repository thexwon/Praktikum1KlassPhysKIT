"""
Parameter für die gekoppelten Pendel.

Parameter und entsprechende Unsicherheiten für die gekoppelten Pendel, in SI 
Einheiten.  
"""

L = 1020.0                   # Abstand zwischen Aufhängepunkt und Schwerpunkt der Pendelscheibe (in mm)
L_UPPER = 1020.5             # +Unsicherheit
L_LOWER = 1019.5             # -Unsicherheit

d = 100.0                    # Druchmesser der Pendelscheiben (in mm)
d_UPPER = 100.5              # +Unsicherheit
d_LOWER = 99.5               # -Unsicherheit

rho = 7.44                   # Längendichte des Schafts (in g/cm)
                             # Ohne Angabe von Unsicherheiten
                             
mk = 44                      # Masse der Koppelfederbefestigung (in g)
mk_UPPER = 44.5              # +Unsicherheit
mk_LOWER = 43.5              # -Unsicherheit

mP1 = 1400                   # Masse der schwereren Pendelscheibe (in g)
mP1_UPPER = 1400.5           # +Unsicherheit
mP1_LOWER = 1399.5           # -Unsicherheit

mP2 = 1221.0                 # Masse der schwereren Pendelscheibe (in g)
mP2_UPPER = 1221.5           # +Unsicherheit
mP2_LOWER = 1220.5           # -Unsicherheit

__version__ = 1.0
