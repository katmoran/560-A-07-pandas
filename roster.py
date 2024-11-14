 # https://goheels.com/sports/mens-basketball/roster
import pandas as pd 

player = {"Last Name": ["Davis", "Cadeau", "Trimble"], 
          "First Name": ["RJ", "Elliot", "Seth"],
          "height": [72, 73, 75],
          "weight":[180, 180, 195]
          }
data= pd.DataFrame(player)
print(data)
          