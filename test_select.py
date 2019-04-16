from programFiles.select import toSelect
from programFiles.selectcol import toSelectCol

#SELECT from (pupulation) 2018 where (population) = [huge] at 2017 
q=['SELECT', 'population', 'population', 'huge', 'from', '2018', 'where', '=', 'at', '2017']
#SELECTCOL from (population) 2018
r=['SELECTCOL','population','','from','2018']


#UNCOMMENT / COMMENT
toSelect(q, '/home/arcadi/Desktop/dbnew/testDatabase')
toSelectCol(r, '/home/arcadi/Desktop/dbnew/testDatabase')
