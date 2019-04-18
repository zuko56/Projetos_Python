from math import radians, sin, cos, tan
angulo = float(input('Digite seu angulo: '))
print('Seu seno é {:.2f}, seu cosseno é {:.2f} e sua tangente é {:.2f}'.format(sin(radians(angulo)), cos(radians(angulo)), tan(radians(angulo))))