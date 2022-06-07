import math
import matplotlib.pyplot as plt

class Manipulator:
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2

    def findEndEffectorPosition(self, theta1, theta2):
        position = []

        position.append(l1 * math.cos((math.pi * theta1) / 180) + l2 * math.cos((math.pi * (theta1 + theta2)) / 180))
        position.append(l1 * math.sin((math.pi * theta1) / 180) + l2 * math.sin((math.pi * (theta1 + theta2)) / 180))
        return position

    def findJointAngle(self, X, Y):
        joint_angle = []

        P = l1 * l1 + l2 * l2
        Q = 2 * l1 * l2
        R = X * X + Y * Y - P

        S = math.sqrt(Q * Q - R * R)
        theta2 = math.atan(S / R)

        a = l1 + l2 * math.cos(theta2)
        b = l2 * math.sin(theta2)

        num = Y * a - X * b
        den = X * a + Y * b

        theta1 = math.atan(num / den);

        theta1 = (180 * theta1) / math.pi
        theta2 = (180 * theta2) / math.pi

        joint_angle.append(theta1)
        joint_angle.append(theta2)

        return joint_angle;


l1 = float(input('Enter Length of Base Link: '))
l2 = float(input('Enter Length of 1st Link/Child of Base Link: '))

x = int(input("Forward Kinematics - Enter 1, Inverse Kinematics - Enter 0: "))

my_robo = Manipulator(l1, l2)

if(x):
    print('Enter Values of Joint Angle')

    theta1 = float(input('theta1 = '))
    theta2 = float(input('theta2 = '))

    position = my_robo.findEndEffectorPosition(theta1,theta2)
    print("X = ",position[0])
    print("Y = ",position[1])

else:
    X = float(input("X Coordinate of End Effector: "))
    Y = float(input("Y Coordinate of End Effector: "))
    joint_angle = my_robo.findJointAngle(X, Y)
    print("theta1 = ", joint_angle[0])
    print("theta2 = ", joint_angle[1])


