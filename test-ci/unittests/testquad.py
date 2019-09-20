import sys
sys.path.append('../')
from main import calc_square


a  = 3
a2 = calc_square(a)
if (a2==9):
   sys.exit(0)
sys.exit(1)
