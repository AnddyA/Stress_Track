# 🎨 Guía Técnica de Frontend - StressTrack

Este documento describe los principios de diseño, la arquitectura visual y las reglas de estilo implementadas en el frontend de **StressTrack**.

El objetivo principal de la interfaz es reducir la carga cognitiva del usuario, ofreciendo una experiencia visual **calmante y clara**, alineada con el propósito de la aplicación: la gestión del estrés académico.

---

## 1. Filosofía de Diseño UI/UX

El diseño de StressTrack se rige por tres pilares fundamentales:

1.  **Diseño Emocional & Calmante:** Se evitan colores saturados o agresivos. Se priorizan los tonos pastel y el espacio en blanco (espacio negativo) para transmitir tranquilidad.
2.  **Feedback Semántico:** El color no es decorativo; tiene una función. Cada tono comunica un estado del sistema (bienestar, alerta, peligro) de forma intuitiva.
3.  **Jerarquía por Contraste:** En lugar de variar excesivamente los tamaños de fuente, utilizamos escalas de grises para diferenciar la información crítica de la secundaria.

---

## 2. Paleta de Colores

Seguimos la regla de distribución **60-30-10** para equilibrar la interfaz visualmente:
* **60% Dominante:** Blanco (`#ffffff`) y fondos grisáceos muy claros (`.bg-inf`).
* **30% Secundario:** Grises de texto, bordes y la barra de navegación oscura (`.bg-dark`).
* **10% Acento:** Colores semánticos para estados y botones de acción.

### 🟢 Colores Semánticos (Estados)
Utilizamos colores desaturados para evitar la fatiga visual (*eye strain*).

| Clase CSS | Hex | Significado Semántico |
| :--- | :--- | :--- |
| `.bg-good` | `#dbffe4` | **Éxito / Bienestar.** Indica niveles bajos de estrés o tareas completadas. |
| `.bg-not-bad` | `#fff4db` | **Precaución.** Estado neutro o advertencia leve. |
| `.bg-dying` | `#ffcccc` | **Crítico.** Niveles altos de estrés o errores importantes. Usamos un rojo suave en lugar de uno puro para no alarmar visualmente. |
| `.bg-noti` | `#ff7171` | **Notificación.** Rojo salmón para destacar elementos no leídos en el header. |

### 🔵 Identidad de Marca
Colores institucionales adaptados para pantallas digitales.

| Clase CSS | Hex | Uso |
| :--- | :--- | :--- |
| `.text-azul` | `#031926` | Encabezados principales y elementos de alto contraste. |
| `.text-azulillo`| `#9DBEBB` | Tono *teal* desaturado para detalles sutiles y elementos decorativos. |

---

## 3. Tipografía y Jerarquía Visual

La jerarquía de la información se maneja mediante el color del texto para guiar el ojo del usuario sin saturarlo.

* **Texto Primario (`.text-dark`):** Para títulos y datos cruciales.
* **Texto Secundario (`.text-gris` - `#8f8f8f`):** Para metadatos, fechas y descripciones. Suaviza la interfaz al reducir el contraste de la información no esencial.
* **Texto Terciario (`.text-grisillo` - `#cacaca`):** Para etiquetas de menor importancia o placeholders.

---

## 4. Layout y Estructura (CSS Grid)

La aplicación utiliza un sistema de **CSS Grid** personalizado para mantener la estructura fija del dashboard mientras el contenido es dinámico.

**Definición del Grid Principal (`base.css`):**
```css
body {
  height: 100vh;
  display: grid;
  grid-template-columns: 4rem 1fr; /* Sidebar colapsado + Contenido */
  grid-template-rows: 4.5rem 1fr;  /* Header fijo + Contenido */
  grid-template-areas:
    "header header"
    "side   main";
}