def main():
    print("Money Changer")
    mmk = eval(input("Input amount in MMK : "))
    print("Currency\t","Buying Rate\t","Selling Rate")
    thb_b = mmk*0.012
    thb_s = mmk*0.013
    print("THB","\t\t",round(thb_b,2),"\t\t",round(thb_s,2))
    usd_b = mmk*0.0005
    usd_s = mmk*0.00034
    print("USD","\t\t",round(usd_b,2),"\t\t",round(usd_s,2))
    gb_b = mmk*0.00038
    gb_s = mmk*0.000254
    print("GB","\t\t",round(gb_b,2),"\t\t",round(gb_s,2))
    yuan_b = mmk*0.0035
    yuan_s = mmk*0.0021
    print("YUAN","\t\t",round(yuan_b,2),"\t\t",round(yuan_s,2))
    aud_b = mmk*0.00074
    aud_s = mmk*0.00052
    print("AUD","\t\t",round(aud_b,2),"\t\t",round(aud_s,2))

main()
