states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[51]) -> Would produce an error as the index is out of bounds of size of the list which is 50

fruits = ["Cherry", "Apple", "Pear"]
veg = ["Cucumber", "Kale", "Spinach"]

fruits_and_veg = fruits+veg # List concatenation
print(fruits_and_veg) -> ['Cherry', 'Apple', 'Pear', 'Cucumber', 'Kale', 'Spinach']

fruits_and_veg = [fruits , veg] #List of Lists
print(fruits_and_veg) -> [['Cherry', 'Apple', 'Pear'], ['Cucumber', 'Kale', 'Spinach']]

fruits_and_veg = [fruits + veg] # List Concatenation inside a list
print(fruits_and_veg) -> [['Cherry', 'Apple', 'Pear', 'Cucumber', 'Kale', 'Spinach']]

print(len(fruits_and_veg)) ->  6 

# len() denotes the length of the list.
