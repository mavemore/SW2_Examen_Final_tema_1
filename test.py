# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
from src.cotizador import cotizar_seguro
from src.cotizador import calcular_cuota_basica
from src.cotizador import calcular_valores_adicionales

class Test(unittest.TestCase):
	#Cotizar seguro de mujer casada de 19 años, de Guayaquil que tiene cáncer y 0 dependientes
	def test_cotizador_1(self):
		self.assertEqual("El valor calculado de su cotización es de 50.00", cotizar_seguro('Guayaquil', 19, 'mujer', 'casado', 'cancer', 0))
		
	#Cotizar seguro de mujer soltera de 80 años, de Machala que tiene cáncer y 1 dependiente
	def test_cotizador_2(self):
		self.assertEqual("La edad ingresada no es válida. Debe de encontrarse entre 18 y 75 años.", cotizar_seguro('Machala', 80, 'mujer', 'soltero', 'cancer', 1))
		
	#Cotizar seguro de hombre soltero de 21 años, de Guayaquil que tiene cáncer y 5 dependientes
	def test_cotizador_3(self):
		self.assertEqual("Solo se puede realizar la cotización para hasta 4 dependientes en línea. Por favor acérquese a la agencia y presente una solicitud.", 
		cotizar_seguro('Guayaquil', 21, 'hombre', 'soltero', 'cancer', 5))
		
	#Cotizar seguro de mujer soltera de 45 años, de Guayaquil que tiene osteoporosis y 10 dependientes
	def test_cotizador_4(self):
		self.assertEqual("No se puede realizar una cotización para el valor ingresado de dependientes.", 
		cotizar_seguro('Guayaquil', 45, 'mujer', 'soltero', 'osteoporosis', 10))

	#Cotizar seguro de hombre soltero de 45 años, de Guayaquil que tiene infarto y 2 dependientes
	def test_cotizador_5(self):
		self.assertEqual("El valor calculado de su cotización es de 140.00", cotizar_seguro('Guayaquil', 45, 'hombre', 'soltero', 'infarto', 2))
		
	#Cotizar seguro de mujer soltera de 65 años, de Guayaquil que tiene cáncer y 3 dependientes
	def test_cotizador_6(self):
		self.assertEqual("El valor calculado de su cotización es de 160.00", cotizar_seguro('Guayaquil', 65, 'mujer', 'soltero', 'cancer', 3))
		
	#Cotizar seguro de hombre soltero de 65 años, de Loja que tiene diabetes y 4 dependientes
	def test_cotizador_7(self):
		self.assertEqual("Saludcita no opera en la ciudad ingresada.", cotizar_seguro('Loja', 65, 'hombre', 'soltero', 'diabetes', 4))
		
	#Cotizar seguro de mujer soltera de 80 años, de Machala que tiene cáncer y 1 dependiente
	def test_cotizador_8(self):
		self.assertEqual("El valor calculado de su cotización es de 70.00", cotizar_seguro('Machala', 35, 'mujer', 'soltero', 'cancer', 1))
		
	#Cotizar seguro de hombre soltero de 65 años, de Loja que tiene diabetes y 4 dependientes
	def test_cotizador_9(self):
		self.assertEqual("El valor calculado de su cotización es de 170.00", cotizar_seguro('Quito', 65, 'hombre', 'soltero', 'diabetes', 4))
		
	#Cotizar seguro de hombre soltero de 65 años, de Loja que tiene diabetes y 4 dependientes
	def test_cotizador_10(self):
		self.assertEqual("El valor calculado de su cotización es de 155.00", cotizar_seguro('Quito', 50, 'mujer', 'soltero', 'osteoporosis', 4))
		
	#Cotizar seguro de hombre soltero de 65 años, de Loja que tiene diabetes y 4 dependientes
	def test_cotizador_11(self):
		self.assertEqual("El valor calculado de su cotización es de 120.00", cotizar_seguro('Quito', 62, 'hombre', 'soltero', 'ninguna', 4))
	
if __name__ == '__main__':
	unittest.main()