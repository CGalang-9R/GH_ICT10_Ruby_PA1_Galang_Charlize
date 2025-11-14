from pyscript import display

glee = {'Galang', 'Escobar', 'Rufo'}
commarts = {'Nardo', 'Sangreo', 'Rufo'}

display("Students involved in at least one club", glee | commarts, target='output')
display("Students who belong to both clubs", glee & commarts, target='output')
display("Students in Glee Club", glee, target='output')
display("Students in Commarts", commarts, target='output')
display("Students who are in exactly one club", glee ^ commarts, target='output')
