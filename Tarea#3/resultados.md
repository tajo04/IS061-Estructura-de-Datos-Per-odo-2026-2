# Resultados de la medición

Semilla usada: `random.seed(11)`.

Computador: Linux x86_64. Versión de Python: 3.12.3.

## Tabla de tiempos (mejor de 5 mediciones, en microsegundos)

| Contactos | contiene() binaria | búsqueda ingenua uno por uno | agregar + eliminar (peor caso) |
|-----------|--------------------:|------------------------------:|--------------------------------:|
| 1.000     | 0,92                | 12,72                         | 2,34                             |
| 10.000    | 1,24                | 124,39                        | 10,66                            |
| 100.000   | 1,46                | 1712,66                       | 88,82                            |

## Interpretación (10.000 → 100.000 contactos)

1. **Búsqueda binaria (`contiene`):** el tiempo pasó de 1,24 µs a 1,46 µs, es decir, se multiplicó apenas por ≈1,18. Era de esperarse: `contiene` es O(log n), y log(100.000) es solo un poco más grande que log(10.000), así que agrandar la agenda diez veces casi no le cuesta nada a la búsqueda binaria.

2. **Búsqueda ingenua uno por uno:** el tiempo pasó de 124,39 µs a 1712,66 µs, multiplicándose por ≈13,8. Era de esperarse porque esta búsqueda es O(n): al tener diez veces más contactos que recorrer, el tiempo también debería multiplicarse por diez; que salga un poco más de diez (13,8) es normal, porque con 100.000 elementos la lista ya no cabe completa en la memoria caché del procesador y cada acceso sale más caro.

3. **Agregar + eliminar (peor caso):** el tiempo pasó de 10,66 µs a 88,82 µs, multiplicándose por ≈8,3, cercano a diez. Era de esperarse porque `agregar` y `eliminar` son O(n): encontrar el sitio es barato (búsqueda binaria), pero abrirle o cerrarle el hueco al arreglo obliga a correr todos los elementos que quedan a la derecha, y con diez veces más contactos hay que correr diez veces más elementos.
