###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("winter")
mySprite = codesters.Sprite("cardinal")
mySprite.say("Good Morning")


print("this is the new last instruction")
mySprite2 = codesters.Sprite("baseball",-200,200)