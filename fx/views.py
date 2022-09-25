from django.shortcuts import render

# Create your views here.


def convert(request, amt):
    usd_amt = amt
    hkd_amt = round(usd_amt * 7.8, 2)
    gbp_amt = round(usd_amt / 1.08, 2)
    sgd_amt = round(usd_amt * 1.41, 2)
    chf_amt = round(usd_amt * .98, 2)
    cad_amt = round(usd_amt * 1.33, 2)
    eur_amt = round(usd_amt * .98, 2)

    context = {
        'usd': usd_amt,
        'hkd': hkd_amt,
        'gbp': gbp_amt,
        'sgd': sgd_amt,
        'chf': chf_amt,
        'cad': cad_amt,
        'eur': eur_amt
    }

    return render(request, 'fx/convert.html', context)

