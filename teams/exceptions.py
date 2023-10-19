from datetime import datetime
now = datetime.now()


class NegativeTitlesError(Exception):
    def __init__(self, message):
        self.message = message


def negativeTtitlesHandler(titles):
    if titles < 0:
        raise NegativeTitlesError("titles cannot be negative")


class InvalidYearCupError(Exception):
    def __init__(self, message):
        self.message = message


def invalidYearCupHandler(year):
    if int(year[0:4]) < 1930:
        raise InvalidYearCupError("there was no world cup this year")
    validYears = [i for i in range(1926, now.year, 4)]
    if not int(year[0:4]) in validYears:
        raise InvalidYearCupError("there was no world cup this year")


class ImpossibleTitlesError(Exception):
    def __init__(self, message):
        self.message = message


def impossibleTitlesHandler(titles, first_cup):
    if int(titles) > ((now.year - int(first_cup[0:4])) / 4):
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")
