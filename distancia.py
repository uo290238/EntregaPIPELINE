import math

def distancia_euclidea_2d(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

if __name__ == '__main__':
    p1 = (1, 2)
    p2 = (4, 6)
    print(f"Distancia Euclidiana en 2D: {distancia_euclidea_2d(p1, p2)}")
