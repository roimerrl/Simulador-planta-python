
# Simulador de gestión y control de una planta de producción (GCPP)

### Asignatura: Programación 1 (Unidad 1-4)
**Universidad de Margarita (UNIMAR)**  -  *Alma Mater del Caribe*  
**Decanato de Ingeniería y Afines**
**Carreras:** Ingeniería de Sistemas / Ingeniería Industrial  
**Control de versiones:** Git + GitHub  


## Descripción General

Este proyecto es una aplicación de línea de comandos (CLI) escrita en Python que simula el una planta industrial durante **5 jornadas de producción**. El usuario asume el rol de supervisor y debe tomar decisiones frente a incidencias (fallas mecánicas, retrasos de materia prima, etc.) para equilibrar la calidad, el cumplimiento del plan y los costos.

Toda la información se maneja en memoria mediante variables y retornos de funciones. 
---

## 2. Integrantes y Responsabilidades
El sistema está dividido en 7 módulos y más de 15 funciones:

| Integrante | Módulo(s) a cargo | Responsabilidad |
|---|---|---|
| **Roimer Rodríguez** | `main.py`, `reportes.py` | Coordinación del ciclo de 5 jornadas, reinicio, paneles de estado e informe final. |
| **Esteban Cen** | `incidencias.py`, `validaciones.py`, `mantenimiento.py` | Eventos imprevistos con decisiones,  lectura segura de datos con `try-except` y gestión del mantenimiento preventivo/correctivo. |
| **José Castillo** | `produccion.py` | Lógica matemática: planificación, consumos, defectos, indicadores y costos. |
| **José Hernández** | `configuracion.py` | Presentación inicial, selección de escenarios y dimensionamiento de recursos base (materia prima, horas y meta) .  |

---
## 3. Reglas de la Simulación
- **Producción:** 1 unidad consume 1.0 kg de materia prima y 0.03 horas de trabajo.
- **Estado de la máquina (3 niveles):** 
  - `2` = Óptima (0% defectos, 100% capacidad)
  - `1` = Operativa (4% defectos, 90% capacidad)
  - `0` = Averiada (14% defectos, 50% capacidad)
- **Mantenimiento:** Preventivo cuesta $80 (1 hora) y Correctivo cuesta $200 (2 horas). Ambos dejan la máquina en estado óptimo.
- **Costos base:** $5/kg de MP, $10/hora trabajada, $15/hora perdida, $2 por defecto.
- **Condiciones de resultado final (justificación):** 
  - *Cumplimiento satisfactorio:* ≥ 95% (se eligió este estándar industrial como meta de éxito).
  - *Crítico por calidad:* < 90% (límite de tolerancia antes de que el lote sea inservible).
  - *Crítico por recursos:* Falta de materia prima o tiempo.

## 4. Indicadores y Fórmulas
- **Calidad** = ((Producidas - Defectuosas) / Producidas) * 100
- **Cumplimiento** = (Producidas / Planificadas) * 100
- **Eficiencia** = (Cumplimiento * 0.5) + (Calidad * 0.5)

## 5. Estructura Modular
- `main.py`: Punto de entrada. Coordina las jornadas y el reinicio de la simulación.
- `configuracion.py`: Presentación inicial y valores base segun el escenario (Estable, Alta Demanda, Crítica).
- `produccion.py`: Fórmulas matemáticas, cálculo de costos e indicadores.
- `incidencias.py`: Las 5 incidencias y las decisiones del usuario.
- `mantenimiento.py`: Lógica de mantenimiento preventivo y correctivo.
- `reportes.py`: Impresión del panel de estado por jornada y balance final.
- `validaciones.py`: Funciones `leer_entero` y `leer_texto` con `try-except`.

## 6. Instrucciones de Ejecución
1. Asegúrate de tener Python 3.8 o superior instalado.
2. Clona el repositorio o descarga los archivos en una misma carpeta.
3. Abre la terminal en esa carpeta y ejecuta:
```bash
python main.py
```
### ¿Cómo interactuar con el simulador?
Una vez ejecutado `python main.py`, el programa te irá guiando paso a paso por la consola. Solo debes ingresar:
1. El nombre de tu planta y tu nombre como supervisor.
2. Un número del 1 al 3 para elegir el escenario de dificultad (Estable, Alta Demanda o Crítica).
3. Durante las 5 jornadas, el sistema te ofrecerá decisiones de mantenimiento (1 para aceptar, 2 para omitir) y te presentará incidencias imprevistas con 3 opciones de resolución. 
4. Al final de las 5 jornadas, verás tu informe final y podrás elegir si deseas reiniciar la simulación (1) o salir (2).

*(El programa te mostrará las opciones válidas en pantalla en todo momento y validará que tus respuestas sean correctas).*