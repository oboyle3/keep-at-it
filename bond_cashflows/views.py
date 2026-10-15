from django.shortcuts import render

from .game_logic import bond_calc

from django.shortcuts import render

def home(request):
    if request.method == "POST":
        bond_face_val = float(request.POST.get("bond_face_val"))
        coupon = float(request.POST.get("coupon"))
        duration = int(request.POST.get("duration"))
        end_projected_cashflow = 1
        print(bond_face_val)
        print(coupon)
        print(duration)
        bond_calc(bond_face_val,coupon,duration)
        end_projected_cashflow =  bond_calc(bond_face_val,coupon,duration)
        print(f" end_projected_cashflow = {end_projected_cashflow}")

    return render(request, "bond_cashflows/index.html")