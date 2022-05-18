
Vas por muy buen camino, solo necesitas una modificación. 
Fíjate que cuando calculas el promedio, la suma, el máximo y el mínimo, lo haces sobre todo el dataframe.
Eso puede resultar muy costoso computacionalmente si tenemos muchos datos. 
En este caso, no vale la pena puesto que sólo necesitas dos promedios, una suma, un máximo y un mínimo.
 En lugar del filtro que haces en la línea 11 para quedarte únicamente con lo que te sirve, podrías hacerlo desde antes, 
 calculando las métricas sólo sobre las columnas que te interesan. 
