import sys
sys.path.append('../')
from main import calc_square

a  = 3
b = calc_square(a)

if (b==9):
   sys.exit(0)
sys.exit(1)
