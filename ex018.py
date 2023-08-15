# digite um angulo e descubra o seno o cosseno e a tangente desse valor
import math

angulo = float(input('digite um angulo: '))



sen = math.sin(math.radians(angulo))
tan = math.tan(math.radians(angulo))
cos = math.cos(math.radians(angulo))

print('o valor digitado foi {:.2f} e o seno dele é de {:.2f} ja o cosseno é {:.2f} e a tangente é de {:.2f}' .format(
    angulo, sen , cos , tan))
