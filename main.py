from pyscript import document

def generate_message(event):
    club = document.querySelector("#club").value

    clubs = {

        "DC": """Dance Club
Advisor : Mr. Alfred Cases
Schedule : Tuesday 03:00 - 05:00 PM
Venue  : Teatro Preciosa
""",

        "GLEE": """Glee Club
Advisor : Mr. Denver Martin
Schedule : Monday 03:00 - 05:00 PM
Venue  : High School Music Room
""",

        "BAND": """Marching Band
Advisor : Mr. Emilio Alumno
Schedule : Tuesday and Wednesday 03:00 - 04:30 PM
Venue  : Band Room
""",

        "MATH": """Math Club
Advisor : Mr. Nicole Gabuya
Schedule : Monday 02:30 - 03:00 PM
Venue  : Room 404
""",

        "SCI": """Science Club
Advisor : Ms. Jameelyn Maramag
Schedule : Tuesday 03:00 - 04:00 PM
Venue  : Room 404
""",

        "SS": """Social Science Club
Advisor : Mr. Roberto Lim
Schedule : Tuesday 03:00 - 04:00 PM
Venue  : Room 409
""",

        "CAC": """Communications Arts Club
Advisor : Ms. Yannis Fernandez
Schedule : Wednesday & Friday 03:00 - 04:00 PM
Venue  : Room 406
""",

        "COCC": """COCC (Cadet Officer Candidate Course)
Advisor : SSgt. Jemima David PA (Res)
Schedule : Wednesday 02:30 - 04:30 PM
Venue  : Quadrangle / Teatro Preciosa
""",

        "VBALL": """Volleyball Varsity
Advisor : Mr. Adrian Ruiz
Schedule : Wednesday 03:00 - 04:00 PM
Venue  : Quadrangle
""",

        "BBALL": """Basketball Varsity
Advisor : Mr. Adrian Ruiz
Schedule : Monday 03:00 - 04:00 PM
Venue  : Quadrangle
"""

    }

    message = clubs.get(club, "Club information not found.")

    output = document.querySelector("#output")
    output.innerHTML = f"<pre>{message}</pre>"