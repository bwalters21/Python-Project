# -*- coding: cp1252 -*-

# This is a Formula for calculating your golf handicap 
# The formula allows you to compute five rounds of golf from any course
# You can enter your score, course rating and slope average for each course
# After you have entered five rounds your handicap is rounded to the tenths place
 

import math
handicap_differential = []
for number in range(5):
    score = float(raw_input("enter the score of your round: "))
    course_rating = float(raw_input("enter the course rating: "))
    slope_number = float(raw_input("enter the slope number: "))
#   (Note: The number 113 represents the slope rating of a golf course of average difficulty, as set by the USGA.)
    handicap_differential.append(((score - course_rating)* 113)/ slope_number)
print("Your Golf Handicap: {0}".format(round(min(float(i) for i in handicap_differential)*0.96, 1)))

# you now have your USGA handicap!
