#Setting the variables
k = 0
lower = 1024
lower_land = ''
lower_twelvemonth = ''
higher = 0
higher_land = ''
higher_twelvemonth = ''
lives_computed = 0
range_lives = 0
number_select_twelvemonth = 0

#Variables for the chosen year
chosen_twelvemonth = int(input('Type the year you want to know about: '))
chosen_lower = 1024
chosen_higher = 0

#Variables for the chosen Land
chosen_land = input('What land(country) you want to know more about? ')
chosen_landlower = 1024
chosen_landhigher = 0
land_lives_range = 0
land_lives_computed = 0
land_select_twelvemonth = 0

#Code which you be executed with the variables

with open('life_expectancy.csv') as life_expectancy:
    
    for row in life_expectancy:
        k += 1
        cleanrow = row.strip()
        pieces = cleanrow.split(',')
        
        if k > 1:
            land = pieces[0]
            twelvemonth = int(pieces[2])
            lives = float(pieces[3])
            
            if lower > lives:
                lower = lives
                lower_twelvemonth = twelvemonth
                lower_land = land
                
            if higher < lives:
                higher = lives
                higher_twelvemonth = twelvemonth
                lower_land = land
                
            if chosen_twelvemonth == twelvemonth:
                lives_computed += lives
                number_select_twelvemonth += 1
                
                if chosen_lower > lives:
                    chosen_lower = lives
                    chosen_lower = lives
                    chosen_land_lower = land
                    
                if chosen_higher < lives:
                    chosen_higher = lives
                    chosen_higher = twelvemonth
                    chosen_land_higher = land
                
            if land.lower() == chosen_land.lower():
                land_lives_computed += lives
                land_select_twelvemonth +=1
                
                if chosen_landlower > lives:
                    chosen_landlower = lives
                    
                if chosen_landhigher < lives:
                    chosen_landhigher = lives
                    
range_lives = lives_computed / number_select_twelvemonth
chosen_land_range = land_lives_computed / land_select_twelvemonth

print(f'The higher life expectancy is {higher} from {higher_land} in {higher_twelvemonth}')
print(f'The lower life expectancy is {lower} from {lower_land} in {lower_twelvemonth}')
print('|-|')
print('|-|')
print('|-|') 
print('|-|')
print(f'For the year {chosen_twelvemonth}: ')
print(f'The higher life expectancy was in {chosen_landhigher} with {chosen_higher}')
print(f'The lower life expectancy was in {chosen_landlower} with {chosen_lower}')
print('|-|')
print('|-|')
print('|-|')
print('|-|')
print(f'For {chosen_land.capitalize()}, the lower life expectancy is {chosen_landlower}, and the higher life expectancy is {chosen_landhigher}, and the average is {chosen_land_range}')            
#The information below I learned in the GESCI 110 Course (Sustaining human life)
print('As you can see, life expectancy can change due to things: the way people take care of their health and the way they treat it.')
print('For example, if you take good care of your health, greater are the possibilities of you have a long life.')
print('If you do not take good care of your health, the lower are the possibilities of you have a long life.')
print('Remember: Your body is not eternal. So, take good care of it if you do not want to lose it sooner than you know') 
    
