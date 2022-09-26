from django.shortcuts import render
import yfinance as yf

# Create your views here.


def convert(request, amt):
    ccys = ['USDHKD=X','GBPUSD=X','USDSGD=X','USDCHF=X','USDCAD=X', 'EURUSD=X']
    df = yf.download(ccys, period='5d').Close
    cols = list(df.columns )
    cols = [x.lower() for x in cols]
    cols = [x.replace('usd', '') for x in cols]
    cols = [x.replace('=x', '') for x in cols]
    df.columns = cols
    df.gbp = 1 / df.gbp
    df.eur = 1 / df.eur
    df = df.iloc[-1]
    print(df)
    base = 'gbp'

    if base == 'usd':
        base_rate = 1
    else:
        base_rate = df.loc[base]

    usd_amt = round(amt / base_rate / 1, 2)
    hkd_amt = round(amt / base_rate * df.loc['hkd'], 2)
    gbp_amt = round(amt / base_rate * df.loc['gbp'], 2)
    sgd_amt = round(amt / base_rate * df.loc['sgd'], 2)
    chf_amt = round(amt / base_rate * df.loc['chf'], 2)
    cad_amt = round(amt / base_rate * df.loc['cad'], 2)
    eur_amt = round(amt / base_rate *  df.loc['eur'], 2)

    context = {
        'base': base,
        'amt': amt,
        'usd': usd_amt,
        'hkd': hkd_amt,
        'gbp': gbp_amt,
        'sgd': sgd_amt,
        'chf': chf_amt,
        'cad': cad_amt,
        'eur': eur_amt
    }

    return render(request, 'fx/convert.html', context)

