# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

#stay consistent with " rather than ' and cover int with parenthesis, not dot.
#one "=" is enough, rather than two.
#changed by UserLAZ (LA886@live.mdx.ac.uk)
year = int(input("Greetings! What is your year of origin? "))

#you need to close the statment with :
#changed by UserLAZ (LA886@live.mdx.ac.uk)
if year <= 1900:
    #using " is a lot more convinient as to not clash with certain words.
    #changed by UserLAZ (LA886@live.mdx.ac.uk)
    print ("Woah, that's the past!")
#use "and" instead of "&&"
#changed by UserLAZ (LA886@live.mdx.ac.uk)
elif year > 1900 and year < 2020:
    print ("That's totally the present!")
#the line below is only applicable if the year given is beyond 2020.
#changed by UserLAZ (LA886@live.mdx.ac.uk)
elif year > 2020:
    print ("Far out, that's the future!!")
