# -*- coding: utf-8 -*-
#Little program to solve the puzzle of altantis 1: The lost tales (video game by cryo interactive)
#https://www.youtube.com/watch?v=Dq6Gmu9sG5s
#Author: Marie Dubremetz github:@mardub1635
#RIP Cryo 
tri=['sanglier', 'oiseau','poisson','crabe']
circ=['terre','etoile','lune','soleil']
atlantis=[(t1,t2,t3,t4,c1,c2,c3,c4) 
for t1 in tri for t2 in tri for t3 in tri for t4 in tri 
for c1 in circ for c2 in circ for c3 in circ for c4 in circ 
if len({t1,t2,t3,t4})==4 and 
   len({c1,c2,c3,c4})==4 and
   t2=='sanglier' and c2!='lune' and #je mange le coureur de la forêt mais je ne chante pas la déesse de la nuit
   [t1,t2,t3,t4].index('oiseau')==[c1,c2,c3,c4].index('terre') and #celle qui mange de l'aile et chante au monde, n'habite pas ma maison
   c4 in ['soleil'] and t4 not in ['poisson']]#Je chante à la lumière mais je ne mange pas le nageur de l'océan
print("The solutions to the 4 statues puzzle are:")
print('-***-')
for a in atlantis:
	
	print(a[0].ljust(8),a[1].ljust(8),a[2].ljust(8),a[3].ljust(8))
	print(a[4].ljust(8),a[5].ljust(8),a[6].ljust(8),a[7].ljust(8))
	print('-'*35)

print('-***-')