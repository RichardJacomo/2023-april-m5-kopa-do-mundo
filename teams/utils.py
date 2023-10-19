from teams.exceptions import negativeTtitlesHandler, \
                                               invalidYearCupHandler, \
                                               impossibleTitlesHandler, \
                                               NegativeTitlesError, \
                                               InvalidYearCupError, \
                                               ImpossibleTitlesError


def data_processing(data: dict):
    negativeTtitlesHandler(data["titles"])
    invalidYearCupHandler(data["first_cup"])
    impossibleTitlesHandler(data["titles"], data["first_cup"])
