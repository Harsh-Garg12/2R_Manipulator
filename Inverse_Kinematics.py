import math
l1 = float(input('Enter Length of Base Link: '))
l2 = float(input('Enter Length of 1st Link/Child of Base Link: '))

def findJointAngle(X, Y):
    joint_angle = []

    P = l1 * l1 + l2 * l2
    Q = 2 * l1 * l2
    R = X * X + Y * Y - P

    S = math.sqrt(Q*Q - R*R)
    theta2 = math.atan(S/R)

    a = l1 + l2*math.cos(theta2)
    b = l2*math.sin(theta2)

    num = Y*a - X*b
    den = X*a + Y*b

    theta1 = math.atan(num/den);

    theta1 = (180*theta1)/math.pi
    theta2 = (180 * theta2)/math.pi

    joint_angle.append(theta1)
    joint_angle.append(theta2)

    return joint_angle;


X = float(input("X Coordinate of End Effector: "))
Y = float(input("Y Coordinate of End Effector: "))

joint_angle = findJointAngle(X, Y)
print("theta1 = ", joint_angle[0])
print("theta2 = ", joint_angle[1])
