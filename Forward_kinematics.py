import math

l1 = float(input('Enter Length of Base Link: '))
l2 = float(input('Enter Length of 1st Link/Child of Base Link: '))

def findEndEffectorPosition(theta1, theta2):
    position = []
    position.append(l1*math.cos((math.pi*theta1)/180)+l2*math.cos((math.pi*(theta1+theta2))/180))
    position.append(l1*math.sin((math.pi*theta1)/180)+l2*math.sin((math.pi*(theta1+theta2))/180))
    return position


print('Enter Values of Joint Angle')

theta1 = float(input('theta1 = '))
theta2 = float(input('theta2 = '))

position = findEndEffectorPosition(theta1,theta2)
print("X = ",position[0])
print("Y = ",position[1])
