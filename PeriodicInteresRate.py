# time related constants
DAYS_IN_YEAR = 365
MONTH_IN_YEAR = 12
QUARTERS_IN_YEAR = 4
MONTH_IN_QUARTER = 3
DAYS_IN_WEEK = 7
WEEKS_IN_YEAR = 52

import math

from decimal import Decimal
def round_float(v, ndigits=4, rt_str=False):
    d = Decimal(v)
    v_str = ("{0:.%sf}" % ndigits).format(round(d, ndigits))
    if rt_str:
        return v_str
    return Decimal(v_str)

def TasaDeInteresEnPeriodo(tasa_interes_anual, from_period, to_period):
    powers = {
        "year": {
            "day": 1 / DAYS_IN_YEAR,
            "week": DAYS_IN_WEEK / DAYS_IN_YEAR,
            "month": 1 / MONTH_IN_YEAR,
            "quarter": 1 / QUARTERS_IN_YEAR,
            "year": 1,
        },
        "quarter": {
            "day": 1 / (DAYS_IN_YEAR / QUARTERS_IN_YEAR),
            "week": 1 / (DAYS_IN_YEAR / QUARTERS_IN_YEAR / DAYS_IN_WEEK),
            "month": 1 / MONTH_IN_QUARTER,
            "quarter": 1,
            "year": QUARTERS_IN_YEAR,
        },
        "month": {
            "day": 1 / (DAYS_IN_YEAR / MONTH_IN_YEAR),
            "week": 1 / (DAYS_IN_YEAR / MONTH_IN_YEAR / DAYS_IN_WEEK),
            "month": 1,
            "quarter": MONTH_IN_QUARTER,
            "year": MONTH_IN_YEAR,
        },
        "week": {
            "day": 1 / DAYS_IN_WEEK,
            "week": 1,
            "month": DAYS_IN_YEAR / MONTH_IN_YEAR / DAYS_IN_WEEK,
            "quarter": DAYS_IN_YEAR / QUARTERS_IN_YEAR / DAYS_IN_WEEK,
            "year": DAYS_IN_YEAR / DAYS_IN_WEEK,
        },
        "day": {
            "day": 1,
            "week": DAYS_IN_WEEK,
            "month": DAYS_IN_YEAR / MONTH_IN_YEAR,
            "quarter": DAYS_IN_YEAR / QUARTERS_IN_YEAR,
            "year": DAYS_IN_YEAR,
        },
    }
    calculo =  (1 + tasa_interes_anual) ** (powers[from_period][to_period]) - 1
    return calculo

def ConviertePerido(from_period, to_period, plazo):
    powers = {
        "year": {
            "day":  DAYS_IN_YEAR,
            "week": WEEKS_IN_YEAR,
            "month":   MONTH_IN_YEAR,
            "quarter":   QUARTERS_IN_YEAR,
            "year": 1,
        }
    }
    return powers[from_period][to_period] * plazo
    
def PagoPorPeriodo(montoTotal, tasa_Interes_Anual, plazo, periodo):
    tasaInteresPeriodica = TasaDeInteresEnPeriodo(tasa_Interes_Anual, "year" ,  periodo)
    ppp = (montoTotal * float(tasaInteresPeriodica))/(1 - (1 + tasaInteresPeriodica)**(-plazo))
    return round_float(ppp)

def CalculaPrestamo(Monto_Total,tasa_Interes_Anual, plazo, periodo ):
    plazo_real = ConviertePerido('year',periodo,plazo)
    ppp = PagoPorPeriodo(Monto_Total, tasa_Interes_Anual, plazo_real, periodo)
    print("EL Pago Mensual a {0} años, seria: {1}".format(plazo,ppp))
    Interes_Compuesto_Futuro = ppp * plazo_real
    print("Pago Total del Prestamo: {0} a {1} años" .format(Interes_Compuesto_Futuro,plazo))
    print("Intereses Totales del Prestamo: {0} a {1} años".format(Interes_Compuesto_Futuro - Monto_Total,plazo))
    print("---------------------")