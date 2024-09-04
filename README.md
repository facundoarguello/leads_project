# leads_project

## Índice

1. [Descripción del Proyecto](#descripción-del-proyecto)
2. [Estructura del Proyecto](#estructura-del-proyecto)
3. [Tecnologías Utilizadas](#tecnologías-utilizadas)
   - [Python](#python)
   - [Pydantic](#pydantic)
   - [FastAPI](#fastapi)
   - [Arquitectura Hexagonal](#arquitectura-hexagonal)
   - [Alembic](#alembic)
   - [PostgreSQL](#postgresql)
   - [Docker](#docker)
   - [Pytest](#pytest)
4. [Pruebas con Docker Compose](#pruebas-con-docker-compose)

## Descripción del Proyecto

Este proyecto es una aplicación web construida con **FastAPI** en Python, utilizando la arquitectura hexagonal para mantener un diseño limpio y escalable. La aplicación persiste sus datos en una base de datos **PostgreSQL** y utiliza **Alembic** para la gestión de migraciones de la base de datos. **Docker** se emplea para contenerizar la aplicación, facilitando su despliegue y pruebas, y **Pytest** se usa para ejecutar pruebas automatizadas y garantizar la calidad del código.


### Arquitectura Hexagonal

La arquitectura hexagonal es un estilo de diseño de software que promueve la separación de las preocupaciones y la independencia de las capas del sistema. Esta arquitectura se enfoca en aislar el núcleo de la lógica de negocio de las implementaciones tecnológicas, como bases de datos, interfaces de usuario y servicios externos.

#### ¿Por qué utilizar la arquitectura hexagonal?

1. **Modularidad y Flexibilidad**: Al separar la lógica de negocio del resto de la aplicación, es más sencillo modificar o reemplazar componentes externos sin afectar el núcleo. Esto permite cambiar, por ejemplo, la base de datos o la interfaz de usuario con un impacto mínimo en el código central.

2. **Facilidad de Pruebas**: Dado que la lógica de negocio está desacoplada de las dependencias externas, es más fácil realizar pruebas unitarias y de integración. Los módulos pueden ser probados de manera aislada utilizando mocks o stubs, mejorando la calidad del código y reduciendo los errores.

3. **Mantenibilidad**: La arquitectura hexagonal promueve un código más limpio y organizado, lo que facilita la comprensión y mantenimiento del proyecto a largo plazo. Los cambios en los requerimientos o en la tecnología utilizada pueden ser manejados de manera más sencilla.

4. **Evolución y Escalabilidad**: La aplicación puede crecer y adaptarse a nuevos requerimientos de manera más eficiente. La independencia entre capas permite escalar o añadir nuevas funcionalidades sin introducir complejidad innecesaria al núcleo del sistema.

En resumen, la arquitectura hexagonal facilita la creación de sistemas robustos, flexibles y fáciles de mantener, lo que es fundamental en proyectos complejos que requieren una evolución constante.

- **Referencia**: [Hexagonal Architecture](https://alistair.cockburn.us/hexagonal-architecture/)


## Tecnologías Utilizadas

### Python

Python es el lenguaje de programación utilizado para desarrollar la aplicación. Es conocido por su sintaxis clara y su extensa biblioteca de módulos, lo que facilita el desarrollo rápido y eficiente.

- **Documentación**: [Python](https://www.python.org/doc/)

### Pydantic

**Pydantic** se utiliza para la validación de datos y la creación de modelos en Python. Es una biblioteca rápida y fácil de usar, ideal para asegurar que los datos procesados en la aplicación cumplan con los tipos y restricciones definidos.

- **Documentación**: [Pydantic](https://pydantic-docs.helpmanual.io/)

### FastAPI

**FastAPI** es el framework principal utilizado para construir la API web. Es un framework moderno, rápido y de alto rendimiento que permite la creación de APIs robustas con una mínima cantidad de código.

- **Documentación**: [FastAPI](https://fastapi.tiangolo.com/)

### Arquitectura Hexagonal

La arquitectura hexagonal es un estilo de diseño que promueve la separación de las preocupaciones. Separa la lógica de negocio (núcleo) de las implementaciones externas (infraestructura), permitiendo una mayor modularidad y testabilidad.

- **Referencia**: [Hexagonal Architecture](https://alistair.cockburn.us/hexagonal-architecture/)

### Alembic

**Alembic** es una herramienta para realizar migraciones en bases de datos en SQLAlchemy. Se utiliza para mantener el esquema de la base de datos sincronizado con los modelos definidos en la aplicación.

- **Documentación**: [Alembic](https://alembic.sqlalchemy.org/en/latest/)

### PostgreSQL

**PostgreSQL** es la base de datos relacional utilizada en el proyecto. Es conocida por su robustez, escalabilidad y cumplimiento con el estándar SQL.

- **Documentación**: [PostgreSQL](https://www.postgresql.org/docs/)

### Docker

**Docker** se utiliza para contenerizar la aplicación y sus dependencias, lo que facilita su despliegue en diferentes entornos y asegura que se ejecute de manera consistente en cualquier sistema.

- **Documentación**: [Docker](https://docs.docker.com/)

### Pytest

**Pytest** es un marco de pruebas utilizado en el proyecto para escribir y ejecutar pruebas unitarias y funcionales. Es flexible y fácil de usar, lo que facilita la creación de pruebas robustas.

- **Documentación**: [Pytest](https://docs.pytest.org/en/stable/)

## Pruebas con Docker Compose

Para ejecutar las pruebas del proyecto utilizando **Docker Compose**, sigue estos pasos:

1. Asegúrate de tener Docker y Docker Compose instalados en tu sistema.
2. Navega al directorio raíz del proyecto donde se encuentra el archivo `docker-compose.yml`.
3. Ejecuta el siguiente comando para levantar los servicios definidos en Docker Compose:

   ```bash
   docker-compose up --build

   Esto construirá las imágenes de Docker (si es necesario) y levantará los contenedores correspondientes a la aplicación, base de datos, etc.

Para ejecutar las pruebas, utiliza el siguiente comando:

```bash
docker-compose exec app pytest
```
Este comando ejecutará las pruebas definidas en el contenedor de la aplicación.

Una vez completadas las pruebas, puedes detener y eliminar los contenedores usando:

```bash

docker-compose down
```