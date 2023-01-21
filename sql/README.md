# ej03_VendedoresDeProductos.sql

### Dada la siguiente base de datos:

- Producto (idProducto, nombre, descrip, estado, idProveedor)
Proveedor (idProveedor, nombre, respdCivil, cuit)
Dirección ( idDir, idPers, calle, nro, piso, dpto )
Cliente (idCliente, nombre, respIVA, CUIL)
Vendedor (idEmpleado, nombre, apellido, DNI)
Venta (nroFactura, idCliente, fecha, idVendedor )
Detalle_venta(nroFactura,nro,idProducto, cantidad,precioUnitario)

### NOTA: El precio unitario es necesario para almacenar los valores al momento de la venta

1. Indique la cantidad de productos que tiene la empresa.
2. Indique la cantidad de productos en estado 'en stock' que tiene la empresa.
3. Indique los productos que nunca fueron vendidos.
4. Indique la cantidad de unidades que fueron vendidas de cada producto.
5. Indique cual es la cantidad promedio de unidades vendidas de cada producto.
6. Indique quien es el vendedor con mas ventas realizadas.
7. Indique todos los productos de lo que se hayan vendido más de 15.000 unidades.
8. Indique quien es el vendedor con mayor volumen de ventas.
