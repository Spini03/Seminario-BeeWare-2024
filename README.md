# Seminario de Investigación: BeeWare

Este repositorio contiene la investigación y el código de demostración para el seminario "Seminario de investigación BeeWare", realizado para la asignatura "Soporte a la Gestión de Datos con Programación Visual" de la Universidad Tecnológica Nacional, Facultad Regional de Rosario.

**Autores:**
* Caro Ariana (47943)
* Spini Santiago (49799)

**Docentes:**
* Juan Ignacio Torres
* Mario Castagnino

**Fecha:** 05/11/2024

---

## 1. Introducción a BeeWare

BeeWare es una colección de herramientas y bibliotecas diseñada para facilitar el desarrollo de aplicaciones nativas multiplataforma utilizando exclusivamente Python.

El objetivo principal del proyecto, fundado por Russell Keith-Magee en 2015, es permitir a los desarrolladores crear aplicaciones con un **único código base** que funcionen nativamente en:
* Windows
* macOS
* Linux
* Android
* iOS
* Web

---

## 2. Componentes Principales

La suite de BeeWare se compone de varias herramientas clave:

* **Toga**: Es un *toolkit* de widgets multiplataforma. Permite crear interfaces gráficas (GUI) utilizando los componentes nativos de cada sistema operativo, asegurando que la aplicación se sienta "en casa" en cualquier plataforma.
* **Briefcase**: Es la herramienta de empaquetado. Se encarga de tomar el proyecto de Python y convertirlo en un artefacto distribuible nativo (como un instalador `.msi` en Windows, una app de macOS, un `.apk` de Android, etc.).
* **Bibliotecas de Acceso Nativo**: Como *Rubicon ObjC*, que permiten a Python interactuar directamente con las librerías nativas del sistema operativo.
* **Compilaciones de Python**: BeeWare proporciona versiones precompiladas de Python para plataformas donde un instalador oficial no está disponible (ej. Android, iOS).

---

## 3. Comparativa con Alternativas

Una parte clave de la investigación fue comparar BeeWare con otros *frameworks* populares para el desarrollo de GUI en Python.

| Framework | Tecnología | Apariencia (GUI) | Ventaja Clave | Desventaja Clave |
| :--- | :--- | :--- | :--- | :--- |
| **BeeWare** | Python (Toga) | **Nativa** (usa widgets del SO) | Facilidad de empaquetado (Briefcase) y apariencia nativa. | Proyecto joven, menos maduro. |
| **Kivy** | Python (Kivy) | **Personalizada** (no nativa) | Optimizado para gráficos intensivos y multitáctiles (juegos). | La apariencia no es nativa. |
| **PyQt** | Python (Binding de Qt/C++) | **Nativa** (simula bien la natividad) | Muy robusto, maduro y con extensa documentación. | Licencia (requiere licencia comercial para apps cerradas). |
| **Electron** | JS, HTML, CSS | **Web** (renderizada en Chromium) | Ideal para desarrolladores web que pasan al escritorio. | Aplicaciones muy pesadas (incluye un navegador). |

---

## 4. Análisis de la Investigación

### Características Claves (Ventajas)

* **Interfaces Nativas**: Al usar Toga, las aplicaciones se ven y sienten como deberían en cada plataforma, mejorando la experiencia del usuario.
* **Python Puro**: No se requiere aprender JavaScript (como en Electron) o lenguajes de widgets personalizados (como en Kivy).
* **Código Abierto**: Posee una licencia BSD, eliminando costos de licenciamiento para proyectos comerciales.
* **Empaquetado Sencillo**: Briefcase automatiza el complejo proceso de compilación y distribución para múltiples plataformas.

### Oportunidades y Desafíos

* **Madurez**: Es un proyecto relativamente joven comparado con PyQt o Kivy. Esto puede implicar menos estabilidad o funcionalidades faltantes.
* **Comunidad**: Aunque activa y en crecimiento, la comunidad es más pequeña y hay menos recursos (tutoriales, ejemplos) que en alternativas más establecidas.
* **Rendimiento**: El rendimiento puede no estar tan optimizado como en herramientas más maduras o especializadas.

### Demanda Laboral y Proyección

La investigación sobre la demanda laboral concluyó que:

1.  **Demanda Específica Baja**: Actualmente, hay pocas ofertas que pidan "BeeWare" explícitamente.
2.  **Interés Creciente**: Se observa un interés creciente en la comunidad Python.
3.  **Impulso por Python**: La enorme popularidad de Python impulsa la búsqueda de herramientas que permitan usar ese *skillset* para crear aplicaciones de escritorio y móviles.
4.  **Proyección Futura**: Se espera que BeeWare gane adopción, especialmente en *startups* y proyectos pequeños que buscan soluciones rápidas y de bajo costo para desarrollo multiplataforma.

---

## 5. Live Demo: "Hola Mundo"

La investigación concluyó con una demostración práctica para ilustrar la facilidad de uso.
