 # https://goheels.com/sports/mens-basketball/roster
import pandas as pd 

roster = ["Davis","Cadeau", "Trimble"]
player = {"Last Name": roster}
data = pd.DataFrame(player)
print(data)
