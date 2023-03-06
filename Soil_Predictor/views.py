from django.shortcuts import render,HttpResponse
from ML.soil_calc import predictI
import pandas as pd 

# Create your views here.
def index(request):
    return render(request,"index.html")


def about(request):
    return render(request,"about.html")


def prediction(request):
    if request.method == 'POST':
        ph = request.POST['ph_in']
        EC = request.POST['EC_in']
        OC = request.POST['OC_in']
        p2o5 = request.POST['p2o5_in']
        k2o5 = request.POST['k2o_in']
        S = request.POST['S_in']
        Fe = request.POST['Fe_in']
        Mn = request.POST['Mn_in']
        Zn = request.POST['Zn_in']
        Cu = request.POST['Cu_in']
        print(f"ph ${ph} EC ${EC}")
        result = predictI(pd.DataFrame([[ph,EC,OC,p2o5,k2o5,S,Fe,Mn,Zn,Cu]]))
        context = {"Result":result}
        return render(request,"prediction.html",context=context)
    else:
        return HttpResponse("something went wrong")

