# **Ancestral Stories:** In many African cultures, the art of storytelling is passed
# down from generation to generation. Imagine you're creating an application that
# records these oral stories and translates them into different languages. The
# stories vary by length, moral lessons, and the age group they are intended for.
# Think about how you would model `Story`, `StoryTeller`, and `Translator`
# objects, and how inheritance might come into play if there are different types of
# stories or storytellers.

# input 
# length,moral lessons,age group
# model story,storytellers,Translator
#output
# inheritance of different stories,storytellers and translators
# process

# create a class
# attributes length,morallessons,agegroup
# methods

class story:
    def init__(self,length,moral_lessons,age_group):
        self.length =length
        self.moral_lessons=moral_lessons
        self.age_group=age_group

    def translation(self,story,storytellers,translator):
        return f"self{storytellers} narrated  self{story} and self{translator} was able to translate it in English "

    def     

#         **African Cuisine:** You're creating a recipe app specifically for African cuisine.
# The app needs to handle recipes from different African countries, each with its
# unique ingredients, preparation time, cooking method, and nutritional
# information. Consider creating a `Recipe` class, and think about how you might
# create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
# `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
# methods.

# input
# recipes of different african countries
# each with unique ingredients, preparation time, cooking method, and nutritional information

# output
# A recipe class
# subclasses of MoroccanRecipe,EthiopianRecipe,NigerianRecipe
# Each with their unique properties and methods


class Recipe:
    def init__(self,ingredients,preparationTime,cookingMethod,nutritional information):
        self.ingredients =ingredients
        self.preparationTime=preparationTime
        self.cookingMethod=cookingMethod
        self.nutritionalInformation=nutritionalInformation

 class MoroccanRecipe:
    def init__(self,)

 class EthiopianRecipe:
    def init__(self,)

 class NigerianRecipe:
    def init__(self)   


#     **Wildlife Preservation:** You're a wildlife conservationist working on a
# program to track different species in a national park. Each species has its own
# characteristics and behaviors, such as its diet, typical lifespan, migration
# patterns, etc. Some species might be predators, others prey. You'll need to
# create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
# these classes might relate to each other through inheritance.

# input 
# diet,typical lifespan,migration patterns,
# output
# model Species,Predator,prey
class Wildlife:
    def init__(self,diet,typicalLifespaan,migrationPatterns):
        self.diet =diet
        self.typicalLifespaan=typicalLifespaan
        self.migrationPatterns=migrationPattern

class Species:
    def init__():

class Predator:
    def init__():

class Prey:
    def init__():

# **African Music Festival:** You're in charge of organizing a Pan-African music
# festival. Many artists from different countries, each with their own musical style
# and instruments, are scheduled to perform. You need to write a program to
# manage the festival lineup, schedule, and stage arrangements. Think about how
# you might model the `Artist`, `Performance`, and `Stage` classes, and consider
# how you might use inheritance if there are different types of performances or
# stages.  

# input
# attributes different countries,musicalStyle,Instruments
# classes artists,Performance,Stage  

# output
# Festivallineup,schedule,stage arrangements

class MusicFestival:
    def init__(self,countries,musicalStyle,instruments):
        self.countries =countries
        self.musicalStyle=musicalStyle
        self.instruments=instruments

class Artist:
    def init__():

class Performance:
    def init__():

class Stage:
    def init__():
    )

 












