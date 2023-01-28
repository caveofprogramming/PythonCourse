text = r"""
    It was the best of times, it was the worst of times, it was 
the age of wisdom, it was the age of foolishness, it was the 
epoch of belief, it was the epoch of incredulity, it was the 
season of Light, it was the season of Darkness, it was the 
spring of hope, it was the winter of despair, we had every- 
thing before us, we had nothing before us, we were all go- 
ing direct to Heaven, we were all going direct the other 
way — in short, the period was so far like the present period, 
that some of its noisiest authorities insisted on its being 
received, for good or for evil, in the superlative degree of 
comparison only. 

There were a king with a large jaw and a queen with a 
plain face, on the throne of England; there were a king 
with a large jaw and a queen with a fair face, on the throne 
of France. In both countries it was clearer than crystal 
to the lords of the State preserves of loaves and fishes, that 
things in general were settled for ever. 

It was the year of Our Lord one thousand seven hundred 
and seventy-five. Spiritual revelations were conceded to 
England at that favoured period, as at this. Mrs. South- 
cott had recently attained her five-and-twentieth blessed 
birthday, of whom a prophetic private in the Life Guards 
had heralded the sublime appearance by announcing that 
arrangements were made for the swallowing up of London 
and Westminster.
"""

"""
\S: not space = [^\s]
\W: not alphanumeric = [^\w]
\D: not a digit = [^\d]
"""

import re

notspace = set(re.findall("\S", text))
print(notspace)
print()
notalpha = set(re.findall("\W", text))
print(notalpha)



