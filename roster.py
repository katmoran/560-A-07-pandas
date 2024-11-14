 # https://goheels.com/sports/mens-basketball/roster
import pandas as pd 

roster = ["Davis","Cadeau", "Trimble"]
player = {"Last Name": roster, 
          "First Name": ["RJ", "Elliot", "Seth"],
          "height": [72, 73, 75], 
          "weight":[180, 180, 195]}
data= pd.DataFrame(player)
print(data)          
