from django.shortcuts import render
from .chart import get_all_states,total_waste_chart,avg_waste_chart,show_wasteprocessed,\
    states,wards,wastegen,wasteproc
import pandas as pd
from django.http import HttpResponse

# Create your views here.
def home(request):
    states = get_all_states()
    return render(request, "Home.html", {"states": states})

def chart_total(request):
    chart1 = total_waste_chart()
    return render(request, "chart_total.html", {"chart1": chart1})
  
def chart_average(request):
    chart2 = avg_waste_chart()
    return render(request, "chart_average.html", {"chart2": chart2})

def chart_processed(request):
    state = request.GET.get("state", "Delhi")  # default = Delhi
    chart3 = show_wasteprocessed(state) 
    return render(request, "chart_processed.html", {"chart3": chart3, "state": state})

def download_excel(request):
    # Create dataframe
    df = pd.DataFrame({
        "State": states,
        "NoofWards":wards,
        "wastegen16": wastegen[0],
        "wastegen17": wastegen[1],
        "wastegen18": wastegen[2],
        "wastegen19": wastegen[3],
        "wastegen20": wastegen[4],
        "wastegen21": wastegen[5],
        "wastegen22": wastegen[6],
        "wasteproc16": wasteproc[0],
        "wasteproc17": wasteproc[1],
        "wasteproc18": wasteproc[2],
        "wasteproc19": wasteproc[3],
        "wasteproc20": wasteproc[4],
        "wasteproc21": wasteproc[5],
        "wasteproc22": wasteproc[6],
    })

    # Create HTTP response with Excel content
    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = 'attachment; filename="SWM_statistics.xlsx"'

    # Write Excel file into response
    with pd.ExcelWriter(response, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Waste Data")

    return response



