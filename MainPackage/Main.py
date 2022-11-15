'''
Name: David Patton and Josh Earley
email: pattondk@mail.uc.edu and earleyja@mail.uc.edu
Assignment: Assignment 11
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: Created a module that calls and API and creates a url
Citations: 
Anything else that's relevant: This was a group project 
'''
import json
import requests
response = requests.get('https://api.nal.usda.gov/fdc/v1/foods/search?query=apple&pageSize=2&api_key=XN9jws7B0PKQGDqBWuhde8MqvJgV2Y8xo8Oj8XKp')
json_string = response.content
    
parsed_json = json.loads(json_string) # This creates a python dictionary 
  
print(parsed_json) #Calls all data relating to "apples" from the API
print("Your current search criteria are", parsed_json['foodSearchCriteria']) #Calls all query criteria for "apple"
print("The total number of results for Apples is", parsed_json['totalHits']) #Calls all of the instances of "apple" in the API

print('The current Data on Apples is',parsed_json['foods'])

#FoodInformation = parsed_json['foods']
#print(type(FoodInformation))
#for food in FoodInformation['foods']:
        #print(parsed_json(-7:1))
        
#for ingredients in parsed_json['foods']:
    #print(ingredients)   
