from datetime import datetime


class TimeToGoHome:
    now = datetime.now().strftime("%H:%M")
    homeTime = "19:00"

    @staticmethod
    def restar_hora(hora1, hora2):
        formato = "%H:%M"
        h1 = datetime.strptime(hora1, formato)
        h2 = datetime.strptime(hora2, formato)
        resultado = h1 - h2
        return str(resultado)

    if restar_hora(homeTime, now) < "0":
        print("Hora de irse a casa")
    else:
        print("Para ir a casa falta: ", restar_hora(homeTime, now))
