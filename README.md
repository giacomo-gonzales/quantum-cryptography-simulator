# Quantum Cryptography Simulator

## 🚀 Live Demo

Play the game here:
👉 https://bb84-simulator-cv3byszshjvh4cg64firlh.streamlit.app/

🌍 Languages: 🇺🇸 English | 🇪🇸 Español 

---

## 🇺🇸 English

Educational simulator of a Quantum Key Distribution (QKD) protocol using Python.

While inspired by the classic BB84 protocol, this simulator implements the Six-State Protocol, which utilizes three measurement bases (Z, X, and Y) instead of two. This increases the sensitivity of eavesdropping detection, as any measurement by an intruder introduces more detectable noise into the transmission.

This project demonstrates the core principles of quantum secure communication, showing how data can be exchanged and how eavesdropping attempts are detected.

---

## Characters

- **Photonzo**: The quantum sender (the "photons" source). 
- **Bitbert**: The player (receiver) who measures the incoming quantum bits.  
- **Evetron**: The eavesdropper trying to intercept the transmission. 

---

# 🧠 How it works

The simulator implements a version of the Six-State Protocol (an extension of BB84):

1- Preparation: Photonzo sends bits using three random bases (Z, X, Y).

2- Measurement: Bitbert chooses bases to measure the incoming bits.

3- Eavesdropping: If active, Evetron intercepts and measures the bits. In this protocol, this causes even more disturbances, making eavesdropping easier to detect.

4- Sifting: Bits are kept only if sender and receiver bases match.

5- Security Check: Errors in matching bits suggest that an eavesdropper was present.

---

ℹ️ Protocol Note

This simulator is based on the Six-State Protocol (1998). While it shares the fundamental logic of BB84, it uses three bases (X, Y, and Z) and six possible states. This approach increases the sensitivity for detecting eavesdropping compared to the original two-base BB84 protocol.

Note: This is an educational implementation and may not perfectly replicate the full physical complexity of the Six-State protocol.

---

## How to run

You need Python installed.

Run:

```bash
python six-state_simulator_en.py
```
You can also copy the code and run it in Google Colab.

---

## Example usage

Choose your role:
1. Play as Fotoncio
2. Play as Bitberto
3. Play as Evetron

How many bits do you want to simulate? (e.g., 10, 20, 50): 20

The program will display:

- Bases used by Fotoncio
- Bases used by Bitberto
- Shared key
- Detected errors
- Whether Evetron was detected or not

---

## Concepts used

- Quantum cryptography
- Six-State protocol
- Bits
- Measurement bases
- Shared key
- Eavesdropping detection
- Random simulation

---

## ⚠️ Limitations

This is an educational simulation. It does not use real quantum hardware or physical photons.

Its purpose is to demonstrate the logical principles of QKD and the impact of the No-Cloning Theorem in a simplified environment.

---

## 🇪🇸 Español

Simulador educativo de un protocolo de Distribución Cuántica de Claves (QKD) desarrollado en Python.

Aunque está inspirado en el clásico protocolo BB84, este simulador implementa el Protocolo de Seis Estados (Six-State Protocol), el cual utiliza tres bases de medición (Z, X e Y) en lugar de dos. Esto incrementa la sensibilidad en la detección de espionaje, ya que cualquier medición realizada por un intruso introduce una mayor cantidad de ruido detectable en la transmisión.

Este proyecto demuestra los principios fundamentales de la comunicación cuántica segura, mostrando cómo pueden intercambiarse datos y cómo se detectan los intentos de interceptación o espionaje.

---

## Personajes

- **Fotoncio**: El emisor cuántico (la fuente de los "fotones").
- **Bitberto**: El jugador (receptor) que mide los bits cuánticos entrantes.
- **Evetron**: El espía que intenta interceptar la transmisión.

---

## 🧠 Cómo funciona

El simulador implementa una versión del Protocolo de Seis Estados (Six-State Protocol), una extensión de BB84:

1. Preparación: Photonzo envía bits utilizando tres bases aleatorias (Z, X e Y).

2. Medición: Bitbert elige bases para medir los bits cuánticos recibidos.

3. Intercepción: Si está activo, Evetron intercepta y mide los bits. En este protocolo, esto provoca aún más perturbaciones, haciendo que la presencia de un espía sea más fácil de detectar.

4. Depuración (Sifting): Los bits se conservan únicamente cuando las bases del emisor y del receptor coinciden.

5. Verificación de seguridad: Los errores en los bits coincidentes sugieren que hubo un espía presente durante la transmisión.

---
## ℹ️ Nota sobre el protocolo

Este simulador está basado en el Protocolo de Seis Estados (1998). Aunque comparte la lógica fundamental del protocolo BB84, utiliza tres bases (X, Y y Z) y seis estados posibles. Este enfoque aumenta la sensibilidad para detectar intentos de espionaje en comparación con el protocolo BB84 original, que emplea únicamente dos bases.

Nota: Esta es una implementación educativa y puede no reproducir perfectamente toda la complejidad física del Protocolo de Seis Estados.

--- 

## Cómo ejecutar el programa

Necesitas tener Python instalado.

Ejecuta:

```bash
python six-state_simulator_es.py
```
También puedes copiar el código y probarlo en Google Colab.

---

## Ejemplo de uso

Elige tu rol:
1. Ser Fotoncio
2. Ser Bitberto
3. Ser Evetron

¿Cuántos bits quieres simular? Ejemplo 10, 20, 50: 20

El programa mostrará:

- Bases usadas por Fotoncio
- Bases usadas por Bitberto
- Clave compartida
- Errores detectados
- Si Evetron fue detectado o no

---

## Conceptos usados

- Criptografía cuántica  
- Protocolo de Seis Estados 
- Bits  
- Bases de medición  
- Clave compartida  
- Detección de espionaje  
- Simulación con números aleatorios  

---

## ⚠️ Limitaciones

Esta es una simulación educativa. No utiliza hardware cuántico real ni fotones físicos.

Su propósito es demostrar los principios lógicos de la distribución cuántica de claves (QKD) y el impacto del teorema de no clonación en un entorno simplificado.

---

## 👨‍💻 Autor

Created by **giacomo-gonzales** as an educational project on programming and quantum cryptography.

Creado por **giacomo-gonzales** como proyecto educativo de programación y criptografía cuántica.
