import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import openpyxl
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
from pandas import Series, DataFrame


def estatisticas (dados):

    summary = df[{"TempMedia_oC", "Precip_mm/d"}].describe()  # média, desvio padrão
    var = df.var()
    mediana = df.median()
    moda = df.mode(0)
    assimetria = df.skew(axis=None)
    amplitude = df.max(axis=None) - df.min(axis=None)
    cf_var = df.std() / df.mean()  # coeficiente de variação

def plots (dados):

    if dados = tempm_mensal:
        x = 'Mês'
        y =  'tempm_mensal'
    if dados = prec_mensal:
        x = 'Mês'
        y = 'prec_anual'
    if dados = 'tempm_anual':
        x = 'Ano'
        y = 'tempm_anual'
    else:
        x = 'Ano'
        y = 'precm_anual'

    df.plot(x, y, kind='line')
    if y = 'tempm_mensal':
        plt.title("Série temporal da Temperatura média mensal (°C)")
        plt.ylabel("Temperatura ºC")
        plt.savefig('plottempmensal')
        plt.show()
        plt.close()
    if y = 'prec_mensal':
        plt.title("Série temporal da precipitação mensal (mm/mês)")
        plt.ylabel("Precipitação (mm/mês")
        plt.savefig('ploprecmensal')
        plt.show()
        plt.close()
    if y = 'prec_anual':
        plt.title("Série temporal da precipitação anual (mm/mês)")
        plt.ylabel("Precipitação (mm/mês")
        plt.savefig('ploprecanual')
        plt.show()
        plt.close()
    else:
        plt.title("Série temporal da Temperatura média anual (°C)")
        plt.ylabel("Temperatura ºC")
        plt.savefig('plottempanual')
        plt.show()
        plt.close()

def histsimples (var):

    plt.hist(var, bins=10, weights=np.ones(len(var)) / len(var), color='red')
    if var = tm or var = tma:
        plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
        plt.xlabel("Temperatura (°C)")
        plt.ylabel("Frequencia (%)")
        if var = tmm:
            plt.title("Histograma - Temperatura média mensal (ºC)")
            plt.savefig('histsimtmm')
            plt.show()
            plt.close()
        if var = ta:
            plt.title("Histograma - Temperatura média anual (ºC)")
            plt.savefig('histsimta')
    if var = pm or var = pa or var = plnm:
        plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
        plt.xlabel("Precipitação (mm/mês)")
        plt.ylabel("Frequencia (%)")
        if var = pm:
            plt.title("Histograma - Precipitação mensal (mm/mês)")
            plt.savefig('histsimpm')
            plt.show()
            plt.close()
        if var = pa:
            plt.title("Histograma - Precipitação média anual (mm/mês)")
            plt.savefig('histsimpm')
            plt.show()
            plt.close()
        if var = plnm:
            plt.title("Histograma LnP (mensal)")
            plt.savefig('histsimpplnm')
            plt.show()
            plt.close()

def histacm (var):
    ax1 = plt.hist(var, bins=30, weights=np.ones(len(var)) / len(var), cumulative=True)

    perc = [1, 50, 99]
    for q in np.percentile(temp, perc):
        plt.axvline(q, color='orange')
    plt.ylabel("Frequencia acumulada (%)")
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    if var = tm or var = tma:
        plt.xlabel("Temperatura (°C)")
        plt.ylabel("Frequencia (%)")
        if var = tmm:
            plt.title("Histograma de frequência acumulada - Temperatura média mensal (ºC)")
            plt.savefig('histac,tmm')
            plt.show()
            plt.close()
        if var = tma:
            plt.title("Histograma de frequência acumulada - Temperatura média anual (ºC)")
            plt.savefig('histacmta')
    if var = pm or var = pa or var =plnm :
        plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
        plt.xlabel("Precipitação (mm/mês)")
        plt.ylabel("Frequencia (%)")
        if var = pm:
            plt.title("Histograma de frequência acumulada - Precipitação mensal (mm/mês)")
            plt.savefig('histacmpm')
            plt.show()
            plt.close()
        if var = pa:
            plt.title("Histograma de frequência - Precipitação média anual (mm/mês)")
            plt.savefig('histacmpm')
            plt.show()
            plt.close()
        if var = plnm
            plt.title("Histograma LnP (mensal)")
            plt.savefig('histacmpplnm')
            plt.show()
            plt.close()
        if var = plna
            plt.title("Histograma LnP (anual)")
            plt.savefig('histacmpplnm')
            plt.show()
            plt.close()

def boxplot (var):

    plt.boxplot(var)

    if var = tm:
        plt.title("Boxplot - Temperatura média mensal (ºC)")
        plt.ylabel("Temperatura (°C)")
        plt.savefig('boxtmm')
        plt.show()
        plt.close()
    if var = ta:
        plt.title("Boxplot - Temperatura média anual (ºC)")
        plt.ylabel("Temperatura (°C)")
        plt.savefig('boxta')
        plt.close()
    if var = pm:
        plt.title("Boxplot - Precipitação mensal (mm/mês)")
        plt.ylabel("Precipitação (mm/mês)")
        plt.savefig('boxtpm')
        plt.show()
        plt.close()
    if var = pa:
        plt.title("Boxplot - Precipitação anual (mm/mês)")
        plt.ylabel(""Precipitação (mm/mês)"")
        plt.savefig('boxtpa')
        plt.show()
        plt.close()

if __name__ == '__main__':

    df = pd.read_excel(
        "C:\\Users\\Administrador\\Documentos\\Meteorologia\\ClimatologiaII\\serie exercicios_lista1\\lista2\\IAG_Cientec_Tmed_Precip diaria.xlsx",
        sheet_name="IAG_temp_prec 2")

    df['Dia'] = pd.to_datetime(df['Dia'], format='%d/%m/%Y')

    #TODO: Novos dataframes

    #tempm_mensal
    #tempm_anual
    #prec_mensal
    #precm_anual

    # Estatísticas básicas
    est_tempm_mensal = estatisticas (tempm_mensal)
    est_tempm_anual = estatisticas (tempm_anual)
    est_prec_mensal = estatisticas (prec_mensal)
    est_precm_anual = estatisticas(precm_anual)

    # Plots simples
    plots(tempm_mensal)
    plots(tempm_anual)
    plots(prec_mensal)
    plots(precm_anual)


    # Variavéis histogramas e boxplots
    tmm = tempm_mensal['tempm_mensal']
    tma = tempm_anual['tempm_anual']
    pm =  prec_mensal['prec_mensal']
    pa =  precm_anual['precm_anual']
    plnm = np.log(pm)
    pnla = np.log(pa)

    # Histogramas simples
    histsimples(tmm)
    histsimples(tma)
    histsimples(pm)
    histsimples(pa)
    histsimples(plnm)
    histsimples(plna)

    #Histogramas frequência acumulada
    histacm(tmm)
    histacm(tma)
    histacm(pm)
    histacm(pa)
    histacm(plnm)
    histacm(plna)

    # Boxplots
    boxplot(tmm)
    boxplot(tma)
    boxplot(pm)
    boxplot(pa)

