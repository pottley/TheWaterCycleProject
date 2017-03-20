#This is my Water Cycle Project. It took me 2 hours and 50 minutes! There's 150 lines!
#Author: Parker Ottley <parker@ottleys.net>
import time
import random

explanationIsDone = False

def solarRadiation():
    print('Solar radiation is when the sun emits waves of heat that cause evaporation.')

def convection():
    print('Convection is when wind spreads heat and evaporates things faster.')

def evaporation():
    print('Evaporation is when heat turns a liquid into a gas.')

def condensation():
    print('Condensation is when a gas turns into a liquid.')

def precipitation():
    print('Precipitation is when a liquid comes down from a cloud as rain, snow, sleet, or hail.')

def transpiration():
    print('Transpiration is the process of water movemont through a plant.')

def infiltration():
    print('Infiltration is when water that touches the ground and gets soaked up into the ground.')

def surfaceRunOff():
    print('Surface run off is when water that doesn\'t get infiltrated runs across the Earth\'s surface.')

def collection():
    print('Collection is when water collects at a place.(Lakes, Oceans, Rivers, and others.)')

def waterCycle():
    print('''???: Hello! The water cycle has many parts in it.
          I will explain most of them in a quiz. Remember TTQA!
          (Turn The Question Around.)''')
    time.sleep(4)
    print('You: Who are you, and what\'s the water cycle?')
    time.sleep(4)
    print('''???: I am the water cycle of course, and the water
cycle is a cycle of water that uses the three states of matter.''')
    time.sleep(4)
    print('You: How do the three states of mater relate to the water cycle?')
    time.sleep(4)
    print('Water Cycle: Evaporation turns a liquid into a gas.')
    time.sleep(4)
    print('Water Cycle: Precipitation can turn water into a solid.')
    time.sleep(4)
    print('Water Cycle: This is an important part of weather.')
    time.sleep(4)
    print('You: How does the water cycle relate to weather?')
    time.sleep(4)
    print('''Water Cycle: Precipitation is rain, ice, sleet or hail.
          Theese are types of weather. Weather is good we should protect it,
          same with water.''')
    time.sleep(4)
    print('You: How can we protect water?')
    time.sleep(4)
    print('''Water Cycle: We can protect water by turning of sinks
when no ones using them,
not dumping things into them like dirt, gas, soap.
There are other ways.''')
    print('''Water Cycle: Anyways, quiz time!
There\'s solar radiation, convection, evaporation,
condensation, precipitation, infiltration, surface run off, collection.''')
    time.sleep(4)
    print('Water Cycle: First, what\'s solar radiation?(TTQA)')
    guess1 = input()
    if guess1 == 'Solar radiation is when the sun emits waves of heat and causes evaporation.' :
        print('Good job your correct!')
        solarRadiation()
    else:
        print('I\'m sorry but you\'re incorrect!')
        solarRadiation()
    time.sleep(5)
    print('Water Cycle: What\'s convection?(TTQA)')
    guess2 = input()
    if guess2 == 'Convection is when wind spreads heat and evaporates things faster.':
        print('Good job you got it!')
        convection()
    else:
        print('I\'m sorry but you\'re incorrect!')
        convection()
    time.sleep(5)
    print('Water Cycle: What\'s evaporation?(TTQA)')
    guess3 = input()
    if guess3 == 'Evaporation is when heat turns a liquid into a gas.':
        print('Good job you got it!')
        evaporation()
    else:
        print('I\'m sorry but you\'re incorrect!')
        evaporation()
    time.sleep(5)
    print('Water Cycle: What\'s condensation?(TTQA)')
    guess4 = input()
    if guess4 == 'Condensation is when a gas turns into a liquid.':
        print('Good job you got it!')
        condensation()
    else:
        print('I\'m sorry but you\'re incorrect!')
        condensation()
    time.sleep(5)
    print('Water Cycle: What\'s precipitation?(TTQA)')
    guess5 = input()
    if guess5 =='Precipitation is when a liquid comes down from a cloud as rain, snow, sleet, or hail.':
        print('Good job you got it!')
        precipitation()
    else:
            print('I\'m sorry but you\'re icorrect!')
            precipitation()
    time.sleep(5)
    print('Water Cycle what\'s transpiration?(TTQA)')
    guess6 = input()
    if guess6 == 'Transpiration is the process of water movement through a plant.':
        print('Good job you got it!')
        transpiration()
    else:
        print('I\'m sorry but you\'re incorrect!')
        transpiration()
    print('Water Cycle: What\'s infiltration?(TTQA)')
    guess7 = input()
    if guess7 =='Infiltration is when water that touches the ground and gets soaked up into the ground.':
        print('Good job you got it!')
        infiltration()
    else:
        print('I\'m sorry but you\'re incorrect!')
        infiltration()
    time.sleep(5)
    print('Water Cycle: What\'s surface run off?(TTQA)')
    guess8 = input()
    if guess8 == 'Surface run off is when water that doesn\'t get infiltrated runs across the Earth\'s surface.':
        print('Good job you got it!')
        surfaceRunOff()
    else:
        print('I\'m sorry but you\'re incorrect!')
        surfaceRunOff()
    time.sleep(5)
    print('Water Cycle: What\'s collection?(TTQA')
    guess9 = input()
    if guess9 == 'Collection is when water collects at a place.(Lakes, Oceans, Rivers, and others.)':
        print('Good job you got it!')
        collection()
    else:
        print('I\'m sorry but you\'re incorrect!')
        collection()

while explanationIsDone == False:
    waterCycle()
    explanationIsDone = True

