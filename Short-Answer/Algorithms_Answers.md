#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) o(n) because a < n  and increases by n*n


b) o(n log n), inner loop increases at a greater rate


c) o(n) recursively returns ~= n

## Exercise II

I'm going to say this is a standard binary search tree with one way being the egg breaking and the other direction means the egg survives the fall. divide and concquor method

we'll say you have a 100 story building and at floor 15 your eggs stop being broken

initial stories 100
chop that in half
drop egg at 50
egg breaks
chop that in half
drop egg at 25
chop that in half
drop egg at 12
egg survives
chop 12 in half then add to survial floor
drop egg at 18
egg breaks
chop 6 in half and add to survival floor
drop egg at 15
egg breaks
chop 3 in half (ceiling) and add to survival floor
drop egg at 14
egg breaks
chop 2 in half and add to survival floor
drop egg at 13
egg survives
return 13th floor

so based on this you will need to know what floor the egg will break on (breakFloor) you will need to know the ground level (eggfloor), and you will need to know the height of the building in floors (eggceiling). 

You will need to take the midpoint (ceiling) of eggfloor and eggceiling to get your initial drop point of 50. 

if your egg is successful at 50, store that value in eggfloor and run the midpoint again. 

once the midpoint hits 1 (ceiling) you know you have run out of floors, and if the current midpoint is success return that midpoint plus the eggfloor, else return eggfloor

runtime complexity would be o(log 2n)

This begs to question, if we use our brains, there is no way an egg survives a fall from a tabletop, so we could just start at floor 1 and know it always breaks :) where floor 0 it is already on the ground so it succeeds
so o(n) linear time :) 