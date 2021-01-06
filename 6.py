from turtle import *

a = 0
b = ['#16a085', '#16a085', '#27ae60', '#2ecc71', '#3498db', '#2980b9', '#8e44ad', '#9b59b6', '#34495e', '#2c3e50', '#f1c40f', '#f39c12', '#e67e22', '#d35400']
while a < 12:
	a = a + 1
	
	forward(150)
	left(150)
	color(b[a])