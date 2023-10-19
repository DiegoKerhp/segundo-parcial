# examen parcial
# https://replit.com/join/yecejnzgzj-diegok3

dia_de_la_semana = input("que dia de la semana es?")
Hora_actual = int(input("que hora es (en formato 24 hrs)"))
Tipo_de_tarea = input("que tipo de tarea tienes, estudio, deportes, descanso o trabajo")

if Hora_actual == 1 < Hora_actual <= 5:
  print("debes estar dormido")

if Hora_actual == 5 < Hora_actual <= 14:
  print("debes estar den clase")

if Hora_actual == 14 < Hora_actual < 22:
  print("puedes hacer tareas")

if Tipo_de_tarea == "descanso" and 14 < Hora_actual < 22:
  print("ademas de tomar una siesta puedes comenzar a realizar tus tareas")

if dia_de_la_semana == "sabado" or "domingo" and 18 < Hora_actual < 22:
  print("puedes ver una película")

if dia_de_la_semana == "lunes" or "miercoles" or "jueves" and 14 < Hora_actual < 20:
  print("puedes ir al gimnasio")


if dia_de_la_semana == "martes" or "jueves" and 13 < Hora_actual < 15:
  print("espero que estes comiendo algo muy nutritivo")
