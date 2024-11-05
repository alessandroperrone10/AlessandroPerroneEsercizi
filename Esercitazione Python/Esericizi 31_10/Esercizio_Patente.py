età = 17
patente = "si"
tasso_alcol = "alto"



if età < 18:
    print("Non puoi guidare perchè sei minorenne")
elif patente != "si":
    print("Sei maggiorenne, ma non hai la patente")
elif tasso_alcol == "alto":
    print("Sei maggiorenne, hai la petente, ma non puoi guidare per il tuo tasso alcolemico")
else:
    print("Sei maggiorenne, hai la patente e se in grado guidare")




