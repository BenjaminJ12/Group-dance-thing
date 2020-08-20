#19/8/20
nameArray = []  
ticketArray = []

groupName = input('What is the name of your group? ') 

groupNumber = int(input('How many peple are in your group? Enter a number between 4 and 10 '))

while groupNumber <4 or groupNumber >10:
  print('Enter a number between 4 and 10 ')
  groupNumber = int(input('How many peple are in your group? Enter a number between 4 and 10 '))

for counter in range(groupNumber):
  name = input('Enter pupil name ')
  photo = input('Do you want a group photo? Enter yes or no ' )
  
  while photo != 'yes' and photo !='Yes' and photo !='no' and photo != 'No':
   print('Please enter yes or no ')
   photo = input('Do you want a group photo? Enter yes or no ' )
  
  if photo == 'no' or photo =='No':
    ticketPrice = 3.0
  elif photo =='yes'or photo =='Yes':
    ticketPrice = 4.99
 
  nameArray.append(name)
 
  ticketArray.append(ticketPrice)

  
print('Group name: ', groupName)
print('Number of folk: ', groupNumber)

for counter in range(groupNumber):
  print(nameArray[counter], ticketArray[counter])
