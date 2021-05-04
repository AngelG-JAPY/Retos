#¿Cuántas latas de refresco sobran?

#Para organizar una fiesta de graduación del instituto se compran 9 cajas de refrescos, 
# donde cada caja contiene 24 latas de refrescos. Invitamos a 56 personas y queremos que todas y cada 
# una de ellas consuman la misma cantidad de refrescos 
# ¿Cuántas latas de refresco sobrarán?

#Análisis del problema:
#¿Qué me pide el problema? Rta: Saber cuantas de refresco sobrarán si los 56 invitados consumen la misma cantidad de refresco
#¿Qué datos necesito? cantidad total de latas de refresco y número de invitados.

#Algoritmo

cantidad_latas = 9*24
cantidad_latas_persona = cantidad_latas//56
cantidad_sobrante = cantidad_latas - 56*cantidad_latas_persona
print("Cada persona podria tomar de a",cantidad_latas_persona,"latas, donde sobrarian"
,cantidad_sobrante,"de latas")