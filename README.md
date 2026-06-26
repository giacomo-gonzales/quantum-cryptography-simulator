# Quantum Cryptography Simulator

## 🚀 Live Demo

Play the game here:
👉 https://bb84-simulator-cv3byszshjvh4cg64firlh.streamlit.app/

🌍 Languages: 🇺🇸 English | 🇪🇸 Español 

---

## 🇺🇸 English

Educational simulator of the BB84 quantum cryptography protocol using Python.

This project demonstrates the core principles of quantum secure communication, showing how data can be exchanged and how eavesdropping attempts are detected.

---

## Characters

- **Photonzo**: The quantum sender (the "photons" source). 
- **Bitbert**: The player (receiver) who measures the incoming quantum bits.  
- **Evetron**: The eavesdropper trying to intercept the transmission. 

---

# 🧠 How it works
The simulator implements a version of the Six-State Protocol (an extension of BB84):

1- Preparation: Photonzo sends bits using three random bases (X, Y, Z).

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
python bb84_simulator_en.py
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
- BB84 protocol
- Bits
- Measurement bases
- Shared key
- Eavesdropping detection
- Random simulation

---

## ⚠️ Limitations

This is an educational simulation.

It does not implement real quantum cryptography or use quantum hardware.

Its purpose is to explain the basic behavior of BB84 in a simple way.

---

## 🇪🇸 Español

Simulador educativo del protocolo de criptografía cuántica BB84 usando Python.

Este proyecto muestra cómo Fotoncio y Bitberto pueden generar una clave compartida usando bases aleatorias, mientras Evetron intenta espiar la comunicación.

---

## Personajes

- **Fotoncio**: emisor de los bits.
- **Bitberto**: receptor que mide los bits.
- **Evetron**: espía que intenta interceptar la comunicación.

---

## ¿Qué simula?

El programa simula una versión sencilla del protocolo BB84:

1. Fotoncio genera bits aleatorios.
2. Fotoncio elige bases aleatorias: `Z` o `X`.
3. Bitberto también elige bases aleatorias.
4. Evetron puede intentar espiar.
5. Solo se conservan los bits donde Fotoncio y Bitberto usaron la misma base.
6. Esos bits forman una clave compartida.
7. Si hay errores, se detecta posible espionaje.

---

## ¿Por qué es importante?

BB84 demuestra una idea central de la criptografía cuántica:

> Si alguien intenta medir la información cuántica, puede alterar los resultados y ser detectado.

Este simulador no usa fotones reales, pero ayuda a entender la lógica del protocolo.

---

## Cómo ejecutar el programa

Necesitas tener Python instalado.

Ejecuta:

```bash
python bb84_simulator_es.py
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
- Protocolo BB84  
- Bits  
- Bases de medición  
- Clave compartida  
- Detección de espionaje  
- Simulación con números aleatorios  

---

## ⚠️ Limitaciones

Este proyecto es una simulación educativa.

No implementa criptografía cuántica real ni usa hardware cuántico.  

Su objetivo es explicar el funcionamiento básico de BB84 de forma sencilla.

---

## 👨‍💻 Autor

Created by **giiiacomobl** as an educational project on programming and quantum cryptography.

Creado por **giiiacomobl** como proyecto educativo de programación y criptografía cuántica.
