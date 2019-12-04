% remember to add 
% import sys
% sys.setrecursionlimit(5000)
% and
% hiddenimports=['pandas._libs.tslibs.timedeltas']
pyinstaller main.py -p classes/abstract -p classes/exception -p classes/ISSUU -p classes/test --onefile