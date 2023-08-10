<style>
  h4{
    text-align: center;
    color: red;
  }
</style>
<h1>Proyecto de Web Scrapping.</h1>

<h4>En busca de una mejora sustancial en nuestro proceso de ventas, he desarrollado un proyecto que aprovecha la tecnología para optimizar la forma en que operamos. Mi solución se basa en un programa de web scraping personalizado que escanea la página de nuestro proveedor en busca de los precios más recientes de nuestros productos más populares. Estos datos se organizan en tablas y se exportan a archivos PDF, facilitando su acceso y uso durante el proceso de venta. Esta solución no solo ahorra tiempo valioso al eliminar la necesidad de búsqueda manual de precios, sino que también mejora la precisión de la información proporcionada durante las ventas. La automatización de este proceso, que se ejecuta dos veces al día, ha reducido drásticamente el tiempo dedicado a la actualización manual de precios. Este proyecto ha demostrado ser un factor clave para aumentar la eficiencia de nuestro equipo de ventas. La volatilidad de los precios en Argentina exige una vigilancia constante, y por eso he incorporado notificaciones por correo electrónico que nos alertan de inmediato sobre cualquier aumento de precios. Esto nos permite tomar decisiones informadas en tiempo real y ajustar nuestras estrategias de venta de manera ágil y precisa.</h4>

<h5>El proyecto se ejecuta todos los dias a las 🕣08:30 y a las 🕞15:30 (Media hora antes de los turnos de atencion) y obtiene los precios de ciertos productos previamente detallados. Esos productos fueron separados en 4 listas dependiendo de la zona del mostrador donde se encuentre el producto en cuestion. Los precios obtenidos son comparados con la informacion en el archivo csv y en el caso que hayan aumentos, envia el email. En cualquiera de los dos casos, realiza un push al repositrio para actualizar el archivo csv.</h5>

<h5>Para lograr el web scrapping tuve que usar la libreria Selenium por su capacidad de interaccion con el navegador, ya que se requieren usuario y contraseña para ingresar al sitio web del proveedor, y con BeautifulSoup no podia lograr, y logre automatizar la ejecucion con GitHub Actions.</h5>
