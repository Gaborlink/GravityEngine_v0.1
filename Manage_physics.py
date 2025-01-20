import matplotlib.pylab as mpy

def gravity_power(distance:float, mass:float):
    """Gravity force of a gravity field of an object and a distance from it :
    distance -> float of the distance of the field
    mass -> float of the mass of the object
    return :
    The force in N/m²"""
    G = 6.67E-11
    Gravity_field = G*mass/(distance**2)
    return Gravity_field

def gravity_action(mass1:float, mass2:float, distance:float):
    """Gravity force of two objects and their distance of separation :
    distance -> float of the distance of their separation
    mass1 -> float of the mass of the object1
    mass2 -> float of the mass of the object2
    return :
    The force in Newton"""
    return gravity_power(distance, mass1)*mass2

def vectors_sum(vectors_coords:list):
    sum_vector_x, sum_vector_y = 0, 0
    for vectorx, vectory in vectors_coords:
        sum_vector_x += vectorx
        sum_vector_y += vectory
    return (sum_vector_x, sum_vector_y)

def gravity_vector(gravity:float, coordinates:tuple):       #champ de gravité de objet 1
    return (gravity*coordinates[0], gravity*coordinates[1]) #et coordonnées de l'objet 2 par rapport au 1

def distance_1_to_2(coordinates1:tuple, coordinates2:tuple):
    return (coordinates2[0]-coordinates1[0], coordinates2[1]-coordinates1[1])