#juegos de equipos

from sys import argv

teams = {}
action = 0

while True:
    action = int(input("""Elige una accion:
                        1. Crear Equipo
                        2. Eliminar Equipo
                        3. Listar Equipos
                        4. Agregar miembro.
                        5. Eliminar miembro.
                        6. Listar miembros.
                        7. Salir: 
                        """))

    if action == 1:
        team_name = input("Ingrese el nombre del equipo: ")
        if (team_name in teams.keys()):
            print("El equipo ya existe")
            continue

        teams[team_name] = []
        continue
    
    elif action == 2:
        team_name = input("Ingrese el nombre del equipo: ")
        if (team_name not in teams.keys()):
            print("El equipo no existe")
            continue

        teams.pop(team_name)
        print("Equipo eliminado")
            
    elif action == 3:
        for key in teams.keys():
            print(key)
        continue

    elif action == 4:
        team_name = input("Ingrese el nombre del equipo para agregar jugadores. ")
        if (team_name not in teams.keys()):
            print("El equipo no existe")
            continue
        member = input("Ingrese el nombre del nuevo integrante: ")
        teams[team_name].append(member)

    elif action == 5:   
        team_name = input("Ingrese el nombre del equipo: ")
        if (team_name not in teams.keys()):
            print("El equipo no existe")
            continue

        member = input("Ingrese el nombre del integrante a eliminar: ")
        if (member not in teams[team_name]):
            print("El integrante no existe")

        teams[team_name].remove(member)
        
    elif action == 6:
        team_name = input("Ingrese el nombre del equipo: ")

        for member in teams[team_name]:
            print(member)

    elif action == 7:
        break;
