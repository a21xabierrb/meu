# Programa fibo.py que xenera a sucesión de Fibonacci e posteriormente comproba si o valor xerado é igual ao valor
# pertencente á serie.
import unittest

# Función chamada "fibonacci" que xenera a sucesión de fibonacci co núemro de veces dado
def fibonacci(numVeces):
    secuenciaFibo = [0,1]  # Inicio da secuencia cos dous primeiros números da sucesión
    for x in range(2,numVeces):  # Comezo dende o tercer numero en adiante
        secuenciaFibo.append(secuenciaFibo[-1] + secuenciaFibo[-2])  # Engado o seguinte número sumando os dous últimos
    return secuenciaFibo  # Devolvo a secuencia ata o número dado

# Función adicional para calcular un número específico na secuencia de Fibonacci
def calcularPosicionFibo(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        num1,num2 = 0,1
        for _ in range(2,posicion + 1):
            num1,num2 = num2,num1 + num2
        return num2

# Clase para as probas unitarias
class testFibo(unittest.TestCase):
    
    # Método para probar si o quinto número da serie é igual a 3
    def testSecuenciaFibo(self):
        quintoNumero = fibonacci(5)[-1]  # Obteño o quinto número da serie
        self.assertEqual(quintoNumero,3,"O quinto número da serie de Fibonacci tendría que ser 3")

    # Método para probar o cálculo de un número específico na secuencia
    def testCalcularPosicionFibo(self):
        numeroPosicionDiez = calcularPosicionFibo(10)  # Obteño o número da décima posición
        self.assertEqual(numeroPosicionDiez,55,"O número na posición 10 da serie de Fibonacci tendría que ser 55")

# Comprobo si este arquivo executase igual ao programa principal
if __name__ == "__main__":
    unittest.main()  # Executo as probas unitarias