#19/8/20
#Hello Github
#Initialise arrays
nameArray = []  
ticketArray = []
#collect data
groupName = input('What is the name of your group? ') 

groupNumber = float(input('How many peple are in your group? Enter a number between 4 and 10 '))

#input validation
while groupNumber <4 or groupNumber >10 or not groupNumber.is_integer():
  print('Enter a number between 4 and 10 ')
  groupNumber = float(input('How many peple are in your group? Enter a number between 4 and 10 '))

#make sure number of people is whole
groupNumber = int(groupNumber)

#loops the number of people in group
for counter in range(groupNumber):
  name = input('Enter pupil name ')
  photo = input('Do you want a group photo? Enter yes or no ' )
  
  #more input validation
  while photo != 'yes' and photo !='Yes' and photo !='no' and photo != 'No':
   print('Please enter yes or no ')
   photo = input('Do you want a group photo? Enter yes or no ' )
  
  #Calculates ticket price
  if photo == 'no' or photo =='No':
    ticketPrice = 3.0
  elif photo =='yes'or photo =='Yes':
    ticketPrice = 4.99
 
 #appends arrays
  nameArray.append(name)
 
  ticketArray.append(ticketPrice)

  #Prints outputs
print('Group name:', groupName)
print('Number in group: ', groupNumber)

for counter in range(groupNumber):
  print(nameArray[counter], ticketArray[counter])
