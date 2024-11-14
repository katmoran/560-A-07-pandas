 # https://goheels.com/sports/mens-basketball/roster
import pandas as pd 

player = {"Last Name": ["Davis", "Cadeau", "Trimble", "Brown", "Tyson", "Powell", "Jackson", "Washington", "Withers", "Hawkins"], 
          "First Name": ["RJ", "Elliot", "Seth", "James", "Cade", "Drake", "Ian", "Jalen", "Jae'Lyn", "Russell"],
          "height": [72, 73, 75, 82, 79, 78, 76, 82, 81, 73],
          "weight":[180, 180, 195, 215, 200, 195, 190, 235, 220, 175]
          }
data= pd.DataFrame(player)

# bmi = weight in kg/height in meters squared 
data["bmi"] = (data["weight"]/2.205)/((data["height"]/39.37)**2)
# rounding the number to 2 decimal places 
data["bmi"] = data["bmi"].round(2)

print(data)

data.to_csv("bmi.csv")