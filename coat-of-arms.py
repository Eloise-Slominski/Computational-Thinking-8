###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("baseballfield")

q1=codesters.Square(100,100,200,'Lightpink')
q2=codesters.Square(-100,100,200,'Snow')
q3=codesters.Square(-100,-100,200,'Lavender')
q4=codesters.Square(100,-100,200,'Lavenderblush')

s1=codesters.Sprite("bat",100,100)
s2=codesters.Sprite("cardinal",-100,-100)
s3=codesters.Sprite("pump",-100,100)
s3.set_size(0.6)
s4=codesters.Sprite("suki",100,-100)
s4.set_size(0.3)

message1=codesters.Text("Eloise Slominski",0,220,"black")
message2=codesters.Text("Your only limit is you",0,-220,"black")