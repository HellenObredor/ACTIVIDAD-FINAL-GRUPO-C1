# 🥷 Sistema de Gestión de Shinobis (Naruto)

## 📌 Descripción

Este proyecto implementa un sistema orientado a objetos en Python basado en el universo de Naruto.
Permite representar ninjas (shinobis) con sus habilidades, técnicas y nivel de chakra, aplicando conceptos fundamentales de programación orientada a objetos.

---

## 🎯 Objetivo

Desarrollar una aplicación que permita:

* Modelar ninjas mediante clases
* Aplicar herencia múltiple
* Implementar encapsulamiento
* Utilizar polimorfismo
* Validar datos mediante setters

---

## 🧱 Estructura del Proyecto

### 🔹 Clase Abstracta: `Shinobi`

Define la estructura base de un ninja:

* `nombre`
* `clan`
* Métodos abstractos:

  * `atacar()`
  * `__str__()`

---

### 🔹 Clases Adicionales

#### ⚡ `Jutsu`

* Método: `usarJutsu()`
* Representa técnicas ninja

#### 🥷 `Destreza`

* Método: `usarDestreza()`
* Representa habilidades especiales

---

### 🔹 Clase Principal: `Jonin`

Hereda de:

* `Shinobi`
* `Jutsu`
* `Destreza`

#### Características:

* Atributo encapsulado: `_nivelChakra`
* Uso de `@property` y `@setter`
* Validación del chakra (0 - 1000)

#### Métodos:

* `atacar()` → acción ofensiva
* `__str__()` → representación del objeto
* `entrenar()` → aumenta el chakra
* `estadoChakra()` → evalúa el nivel de chakra
* `invocarBestia()` → depende del chakra disponible

---

## ⚙️ Funcionalidad Principal

El programa:

1. Crea varios objetos tipo `Jonin`
2. Los almacena en una lista
3. Recorre la lista aplicando:

   * Polimorfismo
   * Métodos heredados
   * Métodos propios
4. Demuestra encapsulamiento modificando el chakra
5. Valida valores incorrectos

---

## 🧪 Ejecución

Para ejecutar el programa:

```bash
python final.py
```

---

## 🧠 Conceptos Aplicados

* ✅ Programación Orientada a Objetos (POO)
* ✅ Clases abstractas
* ✅ Herencia múltiple
* ✅ Encapsulamiento (`@property` y `@setter`)
* ✅ Polimorfismo
* ✅ Uso de listas y ciclos (`for`)
* ✅ Validación de datos

---

## 🎮 Ejemplo de Salida

```
POLIMORFISMO EN ACCIÓN
----------------------------------------
Jonin: Naruto, Clan: Uzumaki, Nivel de Chakra: 500
Naruto ataca con un jutsu poderoso!
Usando jutsu...
Usando destreza...
Chakra medio
Naruto ha entrenado...
Naruto invoca una bestia poderosa
----------------------------------------
```

---

## 👨‍💻 Autores

* Sainner Solano
* Hellen Pimienta

---

## 🏁 Conclusión

Este proyecto demuestra la correcta aplicación de los principios de la programación orientada a objetos mediante una temática dinámica y comprensible, integrando lógica, validación y reutilización de código.

---
