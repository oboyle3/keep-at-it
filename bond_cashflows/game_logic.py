def bond_calc(bond_face_val,coupon,duration):
    #\[Total Cashflows} = ({Coupon} x {Duration}) + {Face Value}
    projected_cashflow = ((coupon * duration) + bond_face_val)
    return projected_cashflow