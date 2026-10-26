# """ introduccion a python"""
# print( "hello world!" )
# print("hello world " *3)

# Bienvenida = print("hola este es el sitema de conteo de...")
# cantidad = int(input("Coloque una cantidad especifica"))

# if cantidad in range(1, 11):
#   print("insuficiente")
# elif 11 <= cantidad <= 20:
# print("basico")
# elif 20 < cantidad <= 30:
# print("bien")


# def suma(n1, n2):
#   resultado = n1+n2
#  return (resultado)


# def resta(n1, n2):
#   resultado = n1-n2
#  return (resultado)


# def multiplicacion(n1, n2):
#   resultado = n1*n2
#  return (resultado)


# def division(n1, n2):
#   resultado = n1/n2
#  return (resultado)


# print(int(input("Coloque operacion: ")))

# if input == "suma":
#   print(f"es,{suma}")

# if input == "resta":
#   print(f"es,{resta}")

# if input == "multiplicacion":
#   print(f"es{multiplicacion}")
#
# if input == "divison":
#   print(f"es{division}")

# def nombre_usu(nombre):
# nombre = print(input("Please enter your full name: "))
# print(f"su nombre es: {nombre}")


# print("hello welcome to python intro course for beginers")


# 1. Pedir un dato al usuario y guardarlo en una variable
# -----------------------------------------------------------------------
# "Bienvenidos a peaje calamar"

# carro = "carro"
# moto = "moto"  # defenimos cada vehiculo que pasara por el peaje
# camion = "camion"

# pago_carro = "20.000 COP"
# definimos el costo de cada uno de los vehiculo
# pago_moto = "30.000 COP"
# pago_camion = "50.000 COP"

# preguntamos que tipo de vehiculo tiene el usuario
# pago = input("Coloque su vehiculo: ")

# if pago == carro:
#    print(f"tu vehiculo debe pagar {pago_carro} ")

# elif pago == moto:
#   print(f"tu vehiculo debe pagar {pago_moto}")  # aplicamos

# elif pago == camion:
#   print(f"tu vehiculo debe pagar {pago_camion}")

# pago_completo = input("Ya pagaste el costo del paso: ")
# respuesta = "si"
# respuesta_no = "no"
# if pago_completo == respuesta:
#    print("gracias por el pago, puedes pasar.")
# if pago_completo == respuesta_no:
#    print("debes pagar para pasar.")
# -----------------------------------------------------------------------------------

# print("welcome to adidas shop")

# print("Adidas shop it's a plesure to recive you on our shop.")
# print("here on our store you can find different styles for your outfits from caps to enter sets")


# product = input("please choose a product - caps, pants or shoes - : ")
# product = product.upper()


# cap_cost = "caps cost is 100.000 COP"
# pants_cost = "pant cost is 200.000 COP"
# shoes_cost = "shoes cost is 500.000 COP"

# if product == "CAPS":
#    print(cap_cost)

# elif product == "PANTS":
# print(pants_cost)

# elif product == "SHOES":
#   print(shoes_cost)
# ___________________________________________________________________________________________________________

# "sistemas de pago"

# print("bienvenido al sistema de pago de producto")

# producto_1 = "perro caliente"
# producto_2 = "pizza"
# producto_3 = "pasta"

# escojer_producto = input(
#    "podras escojer tres productos perro caliente, pizza o pasta: ")
# escojer_producto = escojer_producto.upper()

# costo_perro = "10.000 COP"
# costo_pizza = "30.000 COP"
# costo_pasta = "20.000 COP"

# costo_perro_vuelto = 10000
# costo_pizza_vuelto = 30000
# costo_pasta_vuelto = 20000

# tipo_de_pago = input("como desea pagar efectivo o datafono: ")
# tipo_de_pago = tipo_de_pago.upper()


# if tipo_de_pago == "EFECTIVO":
#    efectivo = int(input("con que cuanto pagara: "))
#    vuelto_perro = efectivo - costo_perro_vuelto
#    vuelto_pizza = efectivo - costo_pizza_vuelto
#    eevuelto_pasta = efectivo - costo_pasta_vuelto

# elif tipo_de_pago == "DATAFONO":
#    print("pida que le den el datafono para pagar")

# if escojer_producto == "PERRO CALIENTE" and tipo_de_pago == "EFECTIVO":
#    print(
#        f"el perro caliente cuesta {costo_perro} y su vuelto es de {vuelto_perro} ")
# elif escojer_producto == "PERRO CALIENTE":
#    print(f"el costo del perro es {costo_perro}")

# if escojer_producto == "PIZZA" and tipo_de_pago == "EFECTIVO":
#    print(
#        f"el producto pizza es {costo_pizza} y su vuelto es de {vuelto_pizza}")
# elif escojer_producto == "PIZZA":
#    print(f"el producto pizza es {costo_pizza}")

# if escojer_producto == "PASTA" and tipo_de_pago == "EFECTIVO":
#    print(
#        f"el producto pasta es {costo_pasta} y su vuelto es de {eevuelto_pasta}")

# print("gracias por su compra")
# __________________________________________________________________________________________________________

# "sistema de pago 2"

# print("Welcome to payment sistem for costumers")
# print("You can find shoes, pants and jeans in our store")

# shoes_price = "250.000 COP"
# pants_price = "90.000 COP"
# jeans_price = "180.000 COP"
# shoes_int_cost = 250000
# pants_int_cost = 90000
# jeans_int_cost = 180000

# choose_product = input("Please choose a product from our store: ")
# choose_product = choose_product.upper()

# if choose_product == "SHOES":
# print(f"Shoes price is {shoes_price}")

# elif choose_product == "PANTS":
#   print(f"Pants price is {pants_price}")

# elif choose_product == "JEANS":
#   print(f"Jeans price is {jeans_price}")

# print("let's continue whit netx payment step")

# payment_method = input("How do you want pay, cash or dataphone: ")
# payment_method = payment_method.upper()

# if payment_method == "CASH":
#  payment_amount = int(input("How much money will you pay: "))


# if payment_method == "CASH" and choose_product == "SHOES":
#  change_shoes = payment_amount - shoes_int_cost
#  print(
#      f"You will pay {shoes_price} whit {payment_amount} and your change is {change_shoes} ")

# elif payment_method == "DATAPHONE" and choose_product == "SHOES":
#  print("Please ask for a dataphone and pay")

# if payment_method == "CASH" and choose_product == "PANTS":
#  change_pants = payment_amount - shoes_int_cost
#   print(
#        f"You will pay {pants_price} whit {payment_amount} and your change is {change_pants}")

# elif payment_method == "DATAPHONE" and choose_product == "PANTS":
#   print("Please ask for a dataphone and pay")

# if payment_method == "CASH" and choose_product == "JEANS":
#   cahnge_jeans = payment_amount - jeans_int_cost
#   print(
#       f"You will pay {jeans_price} whit {payment_amount} and your change is {cahnge_jeans}")

#  elif payment_method == "DATAPHONE" and choose_product == "JEANS":
#   print("Please ask for a dataphone and pay")

# print("Thanks for your visit")
# _________________________________________________________________________________________________________________________

# "Control de abastecimiento en bodegas"

# print("Hi welcome to supply control sistem")
# print("Here you can record our supply sistem")


# product_1 = "pencil"
# pencil_amount = "100"
# pencil_int = 100
# product_2 = "books"
# books_amount = "50"
# books_int = 50
# product_3 = "pen"
# pen_amount = "100"
# pen_int = 100
# product_4 = "redma shets"
# market_pen_amount = "100"
# re_int = 100


# supply_check = input("Please enter here which product is out-stock: ")
# supply_check = supply_check.upper()
# how_meny_product_are = int(input("Plese enter how meny products are there: "))
# how_meny_product_missing = 100 - how_meny_product_are
# how_meny_product_missing_book = 50 - how_meny_product_are


# if supply_check == "PENCIL" and how_meny_product_are < pencil_int:
#     print(
#         f"please it's missing {how_meny_product_missing} pencils to relocate")

# elif supply_check == "PENCIL" and how_meny_product_are > pencil_int:
#     print("Please sell or relocate pencils the amount is too much")


# if supply_check == "BOOK" and how_meny_product_are < books_int:
#     print(
#         f"Please it's missing {how_meny_product_missing_book} books to relocate")

# elif supply_check == "BOOK" and how_meny_product_are > books_int:
#     print(f"Please sell or relocate pencils the amount is too much")


# if supply_check == "PEN" and how_meny_product_are < pen_int:
#     print(f"Please it's missing {how_meny_product_missing} pens to relocate")

# elif supply_check == "PEN" and how_meny_product_are > pen_int:
#     print(f"Please sell or relocate pens the amount is too much")


# if supply_check == "REDMA SHETS" and how_meny_product_are < re_int:
#     print(
#         f"Please it's missing {how_meny_product_missing} redma shets to relocate")

# elif supply_check == "REDMA SHETS" and how_meny_product_are > re_int:
#     print("Please sell or relocate pencils the amount is too much")

# print("recount amount products")

# recount = int(input("please enter how meny product are in the store: "))

# if recount == 350:
#     print("Amount is ok thank's for using the sistem")

# elif recount < 350:
#     print("Please back to read")
# ________________________________________________________________________________________________-

# print("=======factura electronica========")

# producto_1 = "canasta 10.000 COP"
# costo_1 = 10000
# producto_2 = "sillon 50.000 COP"
# costo_2 = 50000
# producto_3 = "meson 60.000 COP"
# costo_3 = 60000

# costo_total = if is

# producto_escojido = input("Porfavor coloque aqui que proucto/s que escojio: ")
# producto_escojido = producto_escojido.upper()

# if producto_escojido == "CANASTA" or "SILLON" or "MESON":
#     print(f"tus productos son {producto_escojido}")

# if producto_escojido == "CANASTA" or "SILLON" or "MESON":
#     print(f"el precio de los productos son")

# ______________________________________________________________________________________________

# print("Welcome to ATM")

# user = float(input("Please enter your count amount: "))
# print(f"Your count amoun is {user}")


# print("1.Withdraw money")
# print("2.Send money")
# print("3.Enter money")

# option = int(input("Please choose a option: "))

# if option == 1:
#     how_much_rest = float(input("Please choose amount will retire:"))
#     print(
#         f"you've retired {how_much_rest} COP and you had {user} COP in your count amount")
#     rest = user - how_much_rest
#     print(f"your count amount is {rest} COP")

# elif option == 2:
#     send = float(input("Please enter how much mony do you want to send: "))
#     print(
#         f"you've send {send} COP and you had {user} COP in your count amount")
#     send_rest = user - send
#     print(f"your count amount is {send_rest}")

# elif option == 3:
#     ent_money = float(
#         input("Please enter how much mony you will enter in your counr¡t amount: "))
#     print(
#         f"you've enter {ent_money} COP and you had {user} COP in your count amount")
#     ent_rest = user + ent_money
#     print(f"you have {ent_rest} in your count amount")

# print("Thank's for using ATM")
# ________________________________________________________________________________________________

# print("welcome to cost sistem store")
# print("Choose a product and ask for there product")

# product_1 = "pen"
# product_2 = "book"
# product_3 = "book_2"
# cost_product_1 = "1.000 COP"
# cost_product_2 = "50.000 COP"
# cost_product_3 = "70.000 COP"

# print("1. Pen 1.000 COP")
# print("2. Book 50.000 COP")
# print("3. Book 2 70.000 COP")
# choose_product = input("Please choose a product: ")
# choose_product = choose_product.upper()

# if choose_product == 1 or choose_product == "PEN":
#     print(f"pen cost is {cost_product_1}")

# elif choose_product == 2 or choose_product == "BOOK":
#     print(f"Book cost is {cost_product_2}")

# elif choose_product == 3 or choose_product == "BOOK 2":
#     print(f"Book 2 cost is {cost_product_3}")

# pay = input("Do you want to pay your product enter yes or not: ")
# pay = pay.upper()

# if pay == "YES":
#     print(f"you'll buy {choose_product} let's continue whit next step")

# elif pay == "NO":
#     print("Thank's for your visit")

# pay_step = input("how do you want to pay product cash or dataphone: ")
# pay_step = pay_step.upper()

# if pay_step == "CASH" or 1 and choose_product == "PEN":
#     print(f"Pay {cost_product_1} for the {product_1}")

# elif pay_step == "CASH" or 2 and choose_product == "BOOK":
#     print(f"Pay {cost_product_2} for the {product_2}")

# elif pay_step == "CASH" or 3 and choose_product == "BOOK 2":
#     print(f"Pay {cost_product_3} for the {product_3}")

# _________________________________________________________________________________________

# import sys
# print("WELCOME TO INVENTORY RECORD FROM PYTHON")
# print("Here you can record how meny inventary are in the store")


# workers = ["Emiro", "Emilio", "Roberto"]

# n = input("Enter your username to find the worker who could manipulate the sistem: ")
# n = n.capitalize()

# if n in workers:
#     print(f"Hello sr {n} you can pass")

# else:
#     print("You can`t pass and the sistem is close for secure")
#     sys.exit()


# print(f"sr {n} please find the product are not there")

# p = "Meat"
# p2 = "Pork"
# p3 = "Fish"
# amount = 10
# amount2 = 20
# amount3 = 30

# print("""Product moust be in this amount order:
#         Meat = 10 libras
#         Pork = 20 libras
#         Fish = 30 """)
# print("Order in store is:")
# amount_p = int(input("Meat = "))
# amount_p2 = int(input("Pork = "))
# amount_p3 = int(input("Fish = "))

# f_p = 10 - amount_p
# f_p2 = 20 - amount_p2
# f_p3 = 30 - amount_p3

# if amount_p < 10:
#     print(f"""Please sr {n} restock the Meat
#               it's {f_p} for 10""")
# else:
#     print("Stock Meat is good continue whit the revision")

# if amount_p2 < 20:
#     print(f"""Please sr {n} restock the Pork
#               it's {f_p2} for 20""")
# else:
#     print("Stock Pork is good continue whit the revision")

# if amount_p3 < 30:
#     print(f"""Please sr {n} restock the Fish
#                 it's {f_p3} for 30""")
# else:
#     print("Stock Fish is good continue.")

# if amount_p == 10 and amount_p2 == 20 and amount_p3 == 30:
#     print(f"Stock store is good sr {n} thank for the revision")
# _______________________________________________________________________________

# import sys
# print("WELCOME TO REGISTER AMOUNT PEOPLE IN THE COURSE")
# print("In the program you can look for people in the course")


# pass_for = ["Emiro", "Robert", "Emilio"]

# s = input("Please enter your username to find worker who can use the program: ")
# s = s.capitalize()

# if s in pass_for:
#     print(f"sr {s} you can use the program")
# else:
#     print("You can't use the program for security")
#     sys.exit()

# print("People amount must be 100")

# people_amount = int(input("Please enter how meny people are in the course: "))

# m = 100 - people_amount

# if people_amount < 100:
#     print("The course can't stars becouze people amount is low")
#     print(f"it`s missing {m} people in the course ")
# else:
#     print("The course can stars if amount people is hig ask for a opcion")
# _____________________________________________________________________________________________________

# print("Welcome to sistem register hours from people who work in the store")

# n = ["Robert", "Emiro", "Roberto", "Ander"]

# na = input("Please enter your name: ")
# na = na.capitalize()

# e = input(f"Please enter what time did you started work sr {na}: ")
# print(f"you started work at {e}")

# other_part = input("Please enter what time it's: ")

# if na in n and e == "8:00 AM" and other_part == "6:30 PM":
#     print("You've worked 10 hr and 30 mins you can pass")
# else:
#     print("Please back to work")

# _______________________________________________________________________________________________________________

# import sys
# p = ["Emer", "Robert", "Emiro"]

# ap = input("Hi please enter your name: ")
# ap = ap.capitalize()

# if ap in p:
#     print(f"Hi sr {ap} people amount must be 100 find how meny there are")
# else:
#     print("You can't use the program for secure")
#     sys.exit()


# t = int(input(f"sr {ap} enter how meny people there are: "))

# hm = 100 - t

# if t < 100:
#     print(
#         f"sr {ap} people amount is to low it missing {hm} people to start the course")
# elif t >= 100:
#     print(f"sr {ap} people amount in the course is enough to start")

# print("Thamk's for using it")
# opt = input("Do you want revaluate people amount or finish: ")

# if opt == "finish":
#     print("See you soon")
#     sys.exit()
# ___________________________________________________________________________________________________

# "Food sistem order"
# print("Welcome to our sevice")

# order_choose = int(input("""You can choose:
#     Menu:
#     1. Hot dog : 10.000
#     2. Pizza : 10.000
#     3. Hamburguer : 20.000
# .  Enter which product did you choose for example(p1 or p2): """))

# drink_choose = int(input("""You can also choose a drink to complement your order
#     Drinks:
#      1.1 Hit : 5.000
#      2.2 Mora : 3.900
#      3.3 Orange : 7.000
# . Enter which drink did you choose for examole(1 or 2): """))
# ______________________________________________________________________________________________________________

# print("Welcome to our order sistem")
# print(""""-----MENU----
#     1. Hot dog ----- 8.000 COP
#     2. Pizza ------- 10.000 COP
#     3. Soda -------- 5.000 COP
#     """)

# # products
# p1 = "Hot dog"
# p2 = "Pizza"
# p3 = "Soda"
# # prices
# p1c = 8000
# p2c = 10000
# p3c = 5000

# Entrada = input("choose your preferense product per number: ")

# if Entrada == "1":
#     print(f"You've have choosed {p1} and it cost is {p1c}")

# elif Entrada == "2":
#     print(f"You've choosed {p2} and it cost is {p2c}")

# else:
#     print(f"you've choosed {p3} and it cost is {p3c}")

# pay = input("Please choose you payment method (cash/electronic): ")

# if pay == "cash":
#     print("Pay and enjoy your product")

# else:
#     print("Ask for a electronic method and pay for your product")

# print("Tank's for buying")

# _____________________________________________________________________________________________

# Sistema completo

# print("Bienvenidos sistema de sumas, resta, multiplicacion y division")
# a = int(input("Ingrese su primer numero: "))
# b = int(input("Ingrese su segundo numero: "))
# operacion = input("Que operacion va a hacer: ")


# def suma(a, b):
#     resultado_sum = a + b
#     print(f"resultado: {resultado_sum}")


# def rest(a, b):
#     resultado_rest = a - b
#     print(f"Resultado: {resultado_rest}")


# def mult(a, b):
#     resultado_mult = a * b
#     print(f"Resultado: {resultado_mult}")


# def div(a, b):
#     reultado_div = a / b
#     if b == 0:
#         print("No se puede divir entre 0")
#     else:
#         print(f"Resultado: {reultado_div}")
# # funcion


# if operacion == "sumar" or "suma":
#     suma(a, b)
# if operacion == "restar" or "resta":
#     rest(a, b)
# if operacion == "dividir":
#     div(a, b)
# if operacion == "multiplicar":
#     mult(a, b)

# print(f"Gracias por usar el programa para {operacion}.")
# _________________________________________________________________________________________

# print("Proyect enter workers")

# Empleados = ["Carlos", "Roberto", "Omar", "Juan", "Fede", "Osman"]

# Access = ["Carlos", "Omar"]


# password_c = "123"
# password_o = "321"


# worker = input("Hi which worker is using the program: ")
# worker = worker.capitalize()

# # verification:

# if worker in Access:
#     print(f"Hi {worker} you can pass")

#     ceri_contra = input("Please enter the passwor before start the program: ")

#     if worker == "Carlos" and ceri_contra == "123":
#         print(f"Sure {worker} starting program")

#     elif worker == "Omar" and ceri_contra == "321":
#         print(f"Sure {worker} starting program")

#     elif worker == "carlos" and ceri_contra == "321":
#         print(f"You arn't {worker}")

#     elif worker == "Omar" and ceri_contra == "123":
#         print(f"You arn't {worker}")


# elif worker == "Roberto" or "Juan" or "Fede" or "Osman":
#     print(f"Hi {worker}, sorry you can't pass ")
# ____________________________________________________________________________________________________________________________________________

# print("Welcome to our program")
# nombre = input("Please enter your user name: ")
# user_adm = ["Cami", "Sof", "And"]

# if nombre in user_adm:
#     print(f"Hi {nombre}, you can pass")

# else:
#     print(f"{nombre} you are not adm")


# _____________________________________________________________________________________________

# REGISTRO DE NOTAS PRIMER SEMESTRE
# nota_1 = float(input("Ingrese su primera nota: "))
# nota_2 = float(input("Ingrese su segunda nota: "))
# nota_3 = float(input("Ingrse su tercera nota: "))

# nota_1 = nota_1 * 0.20
# nota_2 = nota_2 * 0.30
# nota_3 = nota_3 * 0.50

# promedio = nota_1 + nota_2 + nota_3

# if promedio >= 3.0:
#    print("Usted tiene un promedio de: ", promedio)

# else:
#    print("Tu promdio es", promedio,  "Reprobaste")
# ______________________________________________________
# Algoritmo tienda

# productos = "arroz", "carne", "salchicha"
# tienda_abierta = True

# print("""Bienvenido a la tienda, que productos desea:
# 1. arroz
# 2. carne
# 3. salchicha
# Escoja a su gusto y pague el producto.""")
# arroz = 10000
# carne = 20000
# salchicha = 5000
# while tienda_abierta == True:
#     compra = input("¿ Que producto desea escoge ?  ")
# if compra in productos:
#     print("escogiste", compra)
# else:
#     print("No esta ese producto")
# print("Tu compra es", compra)
# if compra == "arroz":
#     print("Tienes que pagar 10.000 por el arroz")
# elif compra == "carne":
#     print("Tienes que pagar 20.000 por la carne")
# else:
#     print("Tienes que pagar 5000 por la salchicha")
# m_d_pago = input("Que metodo de pago desea: ")
# if m_d_pago == "efectivo":
#     print("Paga en caja con el efectivo")
# else:
#     print("Paga en caja con tarjeta")
# ____________________________________________________________
# ESTADO DE ALERTA EN BODEGA DE TIENDA

# producto = 1000
# dinero = 5000000
# personal = 20

# print("Estado de alerta en bodega")

# e_productos = int(input("Productos en bodega: "))
# e_dinero = int(input("Estado de dinero: "))
# e_Personal = int(input("Personal en tienda: "))

# if e_productos < 500 or e_dinero < 2500000 or e_Personal < 10:
#     print("Alerta! Alerta! Alerta!")


# if e_productos < 500:
#     print("Sistema de producto vacio menos del 50 porciento reabastecer rapidamente!!!")
# if e_dinero < 2500000:
#     print("Sistema de dinera vacio menos de 50 porciento reabastecer dinero!!!")
# if e_Personal < 10:
#     print("Personal insuficiente contratar!!!")

# else:
#     print("No hay aleta todo esta bien ._.")
# _____________________________________________________________________________________________
# EJEMPLO CLIENTE EN GEMINI
# monto_a_pagar = int(input("Ingrese el monto a pagar: "))
# tipo_cliente = input("Ingrese que tipo de cliente es (VIP, Regular, Nuevo): ")
# lista_clientes = ["VIP", "Regular", "Nuevo"]

# if tipo_cliente == "VIP" and monto_a_pagar > 50000:
#     descuento_1 = monto_a_pagar * 20 / 100
#     total_1 = monto_a_pagar - descuento_1
#     print("El total a pagar con descuento es", total_1)
# elif tipo_cliente == "VIP" and monto_a_pagar <= 50000:
#     descuento_2 = monto_a_pagar * 10 / 100
#     total_2 = monto_a_pagar - descuento_2
#     print("El total a pagar con descuento es", total_2)

# if tipo_cliente == "Regular" and monto_a_pagar > 50000:
#     descuento_3 = monto_a_pagar * 10 / 100
#     total_3 = monto_a_pagar - descuento_3
#     print("El total a pagar con descuento es", total_3)

# elif tipo_cliente == "Regular" and monto_a_pagar <= 50000:
#     print("Usted es un cliente regular su descuento es ninguno pague", monto_a_pagar)


# if tipo_cliente == "Nuevo":
#     descuento_4 = monto_a_pagar * 5 / 100
#     total_4 = monto_a_pagar - descuento_4
#     print("su total es de:", total_4)

# if tipo_cliente not in lista_clientes:
#     print("Cliente no identificado")
# _________________________________________________________________________________________
# SISTEMA DE AUTOCANCELACION DE SALARIOS (INSUMEDICAL S.A)

# personal = ["Karen", "Camila", "Rocio", "Carlos", "Kevin"]
# personal_SM = ["Ezequiel", "Roberto", "Liliana"]

# p_personal = 2000000
# p_peronalSM = 5000000
# pr_insumedical = 500000000

# # PEDIR ESTADO DE TIENDA Y NOBRE DEL EMPLEADO
# estado_tienda = input(
#     "Ingrese estado de sofware (Abierto/Cerrado): ").capitalize()
# # INICIO DE PROCESO DE EVALUACION
# while estado_tienda == "Abierto":
#     if pr_insumedical <= 50000000:
#         print("\n[ALERTA] Presupuesto insuficiente para continuar con la nómina.")
#         break
#     # PEDIR NOMBRE DE EMPLEADO O CERRAR SOF
#     nombre_empleado = input(
#         "Por favor ingrese su nombre para realizar el pago de su salario (fin para finalizar): ").capitalize()
#     # PARA CERRAR SOF
#     if nombre_empleado == "Fin":
#         print("Proceso finalizado por el usuario.")
#         break
#     # PAGO SI EMPLEDAO TIENE SALARIO MINIMO
#     if nombre_empleado in personal:
#         pr_insumedical = pr_insumedical - p_personal
#         print(f"""============Hola {nombre_empleado} gracias por tu servicio==============
#             >tu pago total es de {p_personal:,.0f} COP
#             >Saldo en Insumedical: {pr_insumedical:,.0f} COP """)
# # PAGO SI EMPLEADO TIENE MAYOR SUELDO
#     elif nombre_empleado in personal_SM:
#         pr_insumedical = pr_insumedical - p_peronalSM
#         print(f"""================Hola {nombre_empleado} gracias por tu servicio================
#                 >tu pago total es de {p_peronalSM:,.0f} COP
#                 >Saldo en Insumedical: {pr_insumedical:,.0f} COP """)
#     else:
#         print("No en entidad")
# _____________________________________________________________________________________________________

# Ejercicios aplicando diccionarios

# contacto = {
#     "nombre": "carlos",
#     "telefono": "555-1234",
#     "correo": "carlos@email.com",
# }

# contacto["telefono"] = "555-9876"

# print(contacto["telefono"])

# contacto["Ciudad"] = "Bogotá"

# del contacto["correo"]

# for clave, valor in contacto.items():
#     print(clave, ":", valor)
# _________________________________________________________________________________________________

# Lista de diccionarios
# contactos = [
#     {"nombre": "carlos", "apellido": "perez",
#         "telefono": "555-1234", "correo": "carlos@email.com"},
#     {"nombre": "juan", "apellido": "perez",
#         "telefono": "555-1234", "correo": "juan@email.com"},
#     {"nombre": "luis", "apellido": "perez",
#         "telefono": "555-1234", "correo": "luis@email.com"}
# ]

# for contacto in contactos:
#     print(
#         f"\n nombre: {contacto['nombre']}\n apellido: {contacto['apellido']}\n telefono: {contacto['telefono']}\n correo: {contacto['correo']}")
#     print("=============================================")

# print(contactos[1]["apellido"]) #con esta sintaxis podemos acceder a un elemento especifico de la lista de diccionarios
# _____________________________________________________________________________________________________
# Ejemplo sistema de registro de productos

# import tkinter as tk
# from tkinter import messagebox

# # --- TUS DATOS Y BACKEND ORIGINAL (INTACTOS) ---
# productos = [
#     {"nombre": "Salchipapa", "precio": "10.000 COP", "stock": 10},
#     {"nombre": "Arepa", "precio": "5.000 COP", "stock": 20},
#     {"nombre": "Hamburguesa", "precio": "15.000 COP", "stock": 5},
# ]

# total_facturado = 0


# # --- CONFIGURACIÓN DE LA INTERFAZ GRÁFICA (GUI) ---
# root = tk.Tk()
# root.title("Sistema de Tienda - Compras")
# root.geometry("450x550")
# root.config(bg="#f0f0f0")

# # Título principal
# titulo = tk.Label(root, text="Bienvenido al Sistema de Tienda",
#                   font=("Arial", 14, "bold"), bg="#f0f0f0", fg="#333")
# titulo.pack(pady=10)

# # Mostrar inventario inicial en pantalla
# frame_inventario = tk.LabelFrame(
#     root, text=" Productos Disponibles ", font=("Arial", 10, "bold"), bg="#f0f0f0")
# frame_inventario.pack(fill="x", padx=20, pady=5)

# for i in productos:
#     lbl_prod = tk.Label(frame_inventario, text=f"• {i['nombre']} = {i['precio']}  (Stock: {i['stock']})", font=(
#         "Arial", 10), bg="#f0f0f0", anchor="w")
#     lbl_prod.pack(fill="x", padx=10, anchor="w")

# # Sección de entradas (Inputs)
# frame_entradas = tk.Frame(root, bg="#f0f0f0")
# frame_entradas.pack(pady=10)

# lbl_nombre = tk.Label(frame_entradas, text="¿Qué producto deseas comprar?:", font=(
#     "Arial", 10), bg="#f0f0f0")
# lbl_nombre.grid(row=0, column=0, sticky="w", pady=5)
# entry_nombre = tk.Entry(frame_entradas, font=("Arial", 10), width=20)
# entry_nombre.grid(row=0, column=1, pady=5, padx=5)

# lbl_cantidad = tk.Label(frame_entradas, text="¿Cuántas unidades deseas?:", font=(
#     "Arial", 10), bg="#f0f0f0")
# lbl_cantidad.grid(row=1, column=0, sticky="w", pady=5)
# entry_cantidad = tk.Entry(frame_entradas, font=("Arial", 10), width=20)
# entry_cantidad.grid(row=1, column=1, pady=5, padx=5)

# # Consola de texto para mostrar los mensajes del sistema
# frame_consola = tk.Frame(root)
# frame_consola.pack(fill="both", expand=True, padx=20, pady=5)

# txt_consola = tk.Text(frame_consola, height=8, font=(
#     "Consolas", 9), bg="#1e1e1e", fg="#00ff00")
# txt_consola.pack(side="left", fill="both", expand=True)

# scrollbar = tk.Scrollbar(frame_consola, command=txt_consola.yview)
# scrollbar.pack(side="right", fill="y")
# txt_consola.config(yscrollcommand=scrollbar.set)

# # Mensaje inicial en la consola
# txt_consola.insert(tk.END, "=== Sistema iniciado correctamente ===\n")


# # --- FUNCIÓN QUE CONECTA LOS BOTONES CON TU LÓGICA ---
# def procesar_compra():
#     global total_facturado
#     nombre_producto = entry_nombre.get().strip()
#     cantidad_str = entry_cantidad.get().strip()

#     # Validar que la cantidad sea un número
#     if not cantidad_str.isdigit():
#         messagebox.showerror(
#             "Error", "Por favor ingresa un número válido para la cantidad.")
#         return

#     cantidad = int(cantidad_str)

#     # --- AQUÍ ESTÁ EXACTAMENTE TU BÚSQUEDA DEL BACKEND ---
#     producto_encontrado = False

#     for producto in productos:
#         if producto["nombre"].lower() == nombre_producto.lower():
#             producto_encontrado = True

#             if cantidad <= producto["stock"]:
#                 total = cantidad * \
#                     int(producto["precio"].split()[0].replace(".", ""))
#                 total_facturado += total
#                 producto["stock"] -= cantidad

#                 # Imprimir en la consola gráfica
#                 txt_consola.insert(
#                     tk.END, f"¡Éxito! Añadiste a tu compra {cantidad} {producto['nombre']} por {total:,} COP\n")
#             else:
#                 txt_consola.insert(
#                     tk.END, f"❌ No hay stock de {producto['nombre']}. Disponible: {producto['stock']}\n")

#             break

#     if not producto_encontrado:
#         txt_consola.insert(
#             tk.END, f"❌ Producto '{nombre_producto}' no encontrado.\n")

#     # Limpiar los inputs para la siguiente compra
#     entry_nombre.delete(0, tk.END)
#     entry_cantidad.delete(0, tk.END)
#     txt_consola.see(tk.END)


# def finalizar_programa():
#     # --- AQUÍ ESTÁ EXACTAMENTE TU BLOQUE FINAL ---
#     txt_consola.insert(tk.END, "\n" + "="*35 + "\n")
#     txt_consola.insert(
#         tk.END, f" Gracias por su compra. Total facturado: {total_facturado:,} COP\n")
#     txt_consola.insert(tk.END, "="*35 + "\n")

#     # Deshabilitar botones al terminar
#     btn_comprar.config(state="disabled")
#     btn_terminar.config(state="disabled")
#     messagebox.showinfo(
#         "Ticket Final", f"Gracias por su compra.\nEl total facturado es: {total_facturado:,} COP")


# # Botones de acción interfaz
# frame_botones = tk.Frame(root, bg="#f0f0f0")
# frame_botones.pack(pady=10)

# btn_comprar = tk.Button(frame_botones, text="Añadir a la Compra", font=(
#     "Arial", 10, "bold"), bg="#4CAF50", fg="white", command=procesar_compra)
# btn_comprar.pack(side="left", padx=5)

# btn_terminar = tk.Button(frame_botones, text="Terminar y Pagar", font=(
#     "Arial", 10, "bold"), bg="#f44336", fg="white", command=finalizar_programa)
# btn_terminar.pack(side="left", padx=5)

# # Ejecutar la ventana
# root.mainloop()

# ________________________________________________________________________________________________________________

# tienda tecnologica con lista de diccionarios

# productos = [
#     {"nombre": "Laptop", "precio": 3000000, "stock": 20},
#     {"nombre": "Smartphone", "precio": 1500000, "stock": 20},
#     {"nombre": "Televisor", "precio": 2000000, "stock": 10},
# ]

# print("Productos disponibles en la tienda tecnológica:")
# for producto in productos:
#     print(
#         f"\n{producto['nombre']}\n - Precio: {producto['precio']} COP\n - Stock: {producto['stock']} unidades")

# total_facturado = 0
# while True:
#     print("Bienvenido a la tienda tecnológica")
#     producto_elegido = input(
#         "¿Qué producto deseas comprar? (Laptop, Smartphone, Televisor) o escribe 'salir' para terminar y pagar: ").capitalize()
#     if producto_elegido.lower() == "salir":
#         print(
#             f"Gracias por visitar la tienda. Compra exitosa de {total_facturado:,} COP. ¡Hasta luego!")
#         break

#     producto_encontrado = None
#     for elemento in productos:
#         if elemento["nombre"] == producto_elegido:
#             producto_encontrado = elemento  # Se asigna el diccionario completo
#             break

#     if producto_encontrado:
#         cantidad = int(
#             input(f"¿Cuántas unidades de {producto_encontrado['nombre']} deseas comprar? "))
#         if cantidad <= producto_encontrado["stock"]:
#             total = cantidad * producto_encontrado["precio"]
#             total_facturado += total
#             producto_encontrado["stock"] -= cantidad
#             print(
#                 f"¡Éxito! Añadiste a tu compra {cantidad} {producto_encontrado['nombre']} por {total:,} COP.")
#         else:
#             print(
#                 f"Lo siento, no hay suficiente stock de {producto_encontrado['nombre']}.")
#     else:
#         print(f"Producto '{producto_elegido}' no encontrado.")
