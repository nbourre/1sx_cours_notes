# Communication série via Bluetooth <!-- omit in toc -->
Document décrivant comment utiliser le module du robot MakeBlock Ranger pour communiquer avec un appareil externe via Bluetooth.

# Table des matières <!-- omit in toc -->
- [Introduction](#introduction)
- [Bluetooth Low Energy (BLE)](#bluetooth-low-energy-ble)
- [Python](#python)
  - [Installation de Thonny](#installation-de-thonny)
    - [Exercices - Installation de Thonny](#exercices---installation-de-thonny)
  - [Les scripts Python](#les-scripts-python)
  - [Le script Python](#le-script-python)
    - [Fonctionnement du script](#fonctionnement-du-script)
- [Code rapide du robot](#code-rapide-du-robot)
- [Exercices](#exercices)
- [Références](#références)

---

# Introduction
La communication série via Bluetooth est une méthode de communication sans fil qui permet de transmettre des données entre deux appareils. Dans le cas du robot MakeBlock Ranger, il est possible de communiquer avec un appareil externe via le module Bluetooth intégré.

Pour le robot, la communication Bluetooth n'est pas différente de la communication série classique. Il suffit de configurer le module Bluetooth pour qu'il établisse une connexion série avec l'appareil externe. Une fois la connexion établie, il est possible de transmettre des données entre les deux appareils.

Le module Bluetooth est connecté sur le port série 0 du robot. Ainsi, il s'agit des commandes `Serial` qui sont utilisées pour communiquer avec le module.

> **Note :** Un des points négatifs de la connexion avec le port série 0 est que le module Bluetooth ne peut pas être utilisé en même temps que le moniteur série de l'IDE Arduino. Il est donc nécessaire de débrancher le module Bluetooth pour pouvoir utiliser le moniteur série.

---

# Bluetooth Low Energy (BLE)
Le module Bluetooth du robot MakeBlock Ranger est un module Bluetooth Low Energy (BLE). Cette technologie permet de réduire la consommation d'énergie des appareils connectés. Elle est particulièrement adaptée pour les appareils qui ont une faible consommation d'énergie, comme les capteurs ou les objets connectés.

La plupart des nouveaux appareils électroniques Bluetooth sont équipés de la technologie BLE. Elle est devenue la norme pour les appareils connectés, car elle permet de prolonger la durée de vie de la batterie des appareils. Par exemple, les tags de localisation Bluetooth peuvent avoir une autonomie de plusieurs mois, voire de plusieurs années sur une pile de montre grâce à la technologie BLE.

---

# Python
Je vous fournis un script Python qui permet de communiquer avec le module Bluetooth du robot MakeBlock Ranger.

L'objectif du cours n'étant pas d'enseigner Python et étant donné que vous n'avez jamais utilisé ce langage, je vais utiliser plusieurs raccourcis pour être capable de vous montrer rapidement comment communiquer avec le module Bluetooth.

## Installation de Thonny
Au lieu d'installer Python de façon traditionnelle, je vous propose d'installer Thonny. C'est un IDE Python qui est très simple d'utilisation et qui est parfait pour débuter.

### Exercices - Installation de Thonny
1. Télécharger Thonny à l'adresse suivante : [https://thonny.org/](https://thonny.org/)
2. Écoutez la vidéo de 35 secondes suivantes

<a href="https://www.youtube.com/watch?feature=player_embedded&v=jYAvJqxHs5E" target="_blank"><img src="https://img.youtube.com/vi/jYAvJqxHs5E/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="320" height="240" border="10" /></a>

## Les scripts Python
J'ai réalisé quelques scripts utilitaire pour vous permettre de communiquer avec le module Bluetooth du robot MakeBlock Ranger ainsi que de trouver l'adresse MAC du module.

Ils sont disponibles sur mon compte GitHub à l'adresse suivante : [https://github.com/nbourre/auriga_bluetooth_python_comm]()

Les scripts actifs sont les suivants :
- `scan_robots.py` : Permet de scanner les appareils Bluetooth à proximité et d'afficher les noms et adresses MAC des appareils MakeBlock Ranger.
  - Lors de l'exécution de ce script, il sauvegardera les adresses MAC des appareils MakeBlock Ranger dans un fichier nommé `makeblock_robots.csv`.
- `makeblock_bluetooth.py` : Permet de communiquer avec le module Bluetooth du robot MakeBlock Ranger.

## Le script Python
Le script Python général est disponible à l'adresse suivante : https://github.com/nbourre/auriga_bluetooth_python_comm/blob/main/makeblock_bluetooth.py

<details><summary>Voici le contenu du script au moment de l'écriture de ce document</summary>

```python
import asyncio
import struct
import sys
import platform
import json
from bleak import BleakClient, BleakScanner, BleakError

# Configuration Bluetooth
DEVICE_NAME = "Makeblock_LE001b10fafb43"
DEVICE_FILE = "last_connected_device.json"
CHARACTERISTIC_NOTIFY_UUID = "0000ffe2-0000-1000-8000-00805f9b34fb"  # UUID for notifications
CHARACTERISTIC_WRITE_UUID = "0000ffe3-0000-1000-8000-00805f9b34fb"  # UUID for writing
CHARACTERISTIC_READ_UUID = "0000ffe5-0000-1000-8000-00805f9b34fb"  # Example for read characteristic
CHARACTERISTIC_INDICATE_UUID = "0000ffe4-0000-1000-8000-00805f9b34fb"  # Example for indication characteristic
DISCONNECTION_TIMEOUT = 10

# Options de données de fin
END_DATA_OPTIONS = {
    'NL': b'\n',  # Nouvelle ligne (0x0A)
    'CR': b'\r',  # Retour chariot (0x0D)
    'BOTH': b'\r\n',  # CR + NL
    'NONE': b''  # Pas de données de fin
}

# Global variables
is_user_input_active = False
incomplete_message = ""
last_received_time = None

def load_last_device():
    """Load the last connected device from a JSON file."""
    try:
        with open(DEVICE_FILE, 'r') as f:
            data = json.load(f)
            return data.get("device_address")
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def save_last_device(device_address):
    """Save the last connected device to a JSON file."""
    with open(DEVICE_FILE, 'w') as f:
        json.dump({"device_address": device_address}, f)

def calculate_crc(data):
    """Calcule le CRC en effectuant un XOR de tous les octets."""
    crc = 0
    for byte in data:
        crc ^= byte
    return crc

def parse_data(data):
    """Handle and concatenate fragmented messages."""
    global incomplete_message

    try:
        # Update the last received time to the current time when data is received
        last_received_time = asyncio.get_event_loop().time()
        
        # Decode the received data to string
        message = data.decode('utf-8', errors='ignore')
        incomplete_message += message
        
        # Look for complete messages that end with a newline character
        if '\n' in incomplete_message:
            # Split the message on newline to get complete chunks
            lines = incomplete_message.split('\n')
            
            # Process all but the last (possibly incomplete) part
            for line in lines[:-1]:
                #print(f"Message série complet : {line.strip()}")
                print(f"{line.strip()}")
            
            # Keep the last segment as incomplete if it doesn't end with a newline
            incomplete_message = lines[-1]
    except UnicodeDecodeError:
        print(f"Données brutes reçues : {data.hex()}")



async def notification_handler(sender, data):
    """Gère les notifications entrantes en envoyant les données à parseData."""
    global is_user_input_active

    if is_user_input_active:
        return  # Skip handling if user input is active
  
    parse_data(data)

async def find_device():
    """Scan and find the MakeBlock Ranger based on the OS."""
    devices = await BleakScanner.discover()
    for device in devices:
        if platform.system() == "Darwin":  # Check if it's macOS
            if device.name == DEVICE_NAME:
                print(f"Device found on macOS: {device.name}, UUID: {device.address}")
                return device.address
        else:
            if device.name == DEVICE_NAME and ":" in device.address:  # Match MAC address on Windows
                print(f"Device found on Windows: {device.name}, MAC: {device.address}")
                return device.address

    print("Device not found.")
    return None

async def handle_disconnect(client: BleakClient):
    """Handle the peripheral disconnection and attempt to reconnect."""
    print("Peripheral device disconnected unexpectedly.")
    attempt = 1
    max_attempts = 5
    connected = False
    reconnect_timeout = 10  # Timeout duration in seconds
    
    # Attempt to reconnect a few times
    while attempt <= max_attempts:
        print(f"Attempting to reconnect... (Attempt {attempt} of {max_attempts})")
        try:
            await asyncio.wait_for(client.connect(), timeout=reconnect_timeout)
            if client.is_connected:
                print("Reconnected successfully.")
                connected = True
                await client.start_notify(CHARACTERISTIC_NOTIFY_UUID, notification_handler)
                break
        except asyncio.TimeoutError:
            print(f"Reconnection attempt {attempt} timed out.")
        except BleakError as e:
            print(f"Reconnection attempt {attempt} failed: {e}")
        except Exception as e:
            print(f"Unexpected error during reconnection attempt {attempt}: {e}")

        attempt += 1
        await asyncio.sleep(1)  # Small delay between attempts

    if not connected:
        print("Failed to reconnect after several attempts. Exiting...")

async def check_connection(client: BleakClient):
    """Periodically check the connection status."""
    try:
        while True:
            await asyncio.sleep(5)
            if not client.is_connected:
                raise BleakError("Device disconnected")
    except BleakError:
        await handle_disconnect(client)


async def check_connection(client: BleakClient):
    """Periodically check the connection status."""
    try:
        while True:
            # Attempt a simple read or write operation to verify connection
            await asyncio.sleep(5)  # Check every 5 seconds
            if not client.is_connected:
                raise BleakError("Device disconnected")
    except BleakError:
        await handle_disconnect(client)

async def check_disconnection(client):
    """Periodically check for disconnection based on data reception time."""
    global last_received_time

    while True:
        await asyncio.sleep(1)
        
        if last_received_time and (asyncio.get_event_loop().time() - last_received_time) > DISCONNECTION_TIMEOUT:
            print(f"No data received for {DISCONNECTION_TIMEOUT} seconds. Disconnecting...")
            await client.disconnect()
            break

async def send_data(client, data, end_data='BOTH'):
    """Envoie des données au robot avec un en-tête et un CRC."""
    if end_data not in END_DATA_OPTIONS:
        end_data = 'BOTH'
    
    packet = bytearray([0xFF, 0x55])
    packet.extend(data)
    crc = calculate_crc(packet)
    packet.append(crc)
    packet.extend(END_DATA_OPTIONS[end_data])

    await client.write_gatt_char(CHARACTERISTIC_WRITE_UUID, packet)
    print(f"Envoyé : {packet.hex()}")

async def listen_for_user_input(client):
    """Écouter les entrées utilisateur sans bloquer la réception des notifications."""
    global is_user_input_active

    while True:
        # Prompt the user to activate input mode
        activation_input = await asyncio.get_event_loop().run_in_executor(None, input, "Tapez ':' puis Entrée pour entrer des données (ou 'quit' pour quitter) :\n")
        
        if activation_input.lower() == 'quit':
            break

        if activation_input == ':':
            is_user_input_active = True

            # Demander l'entrée de l'utilisateur
            user_input = await asyncio.get_event_loop().run_in_executor(None, input, "Entrez des données à envoyer (ou 'quit' pour quitter) : ")
            
            if user_input.lower() == 'quit':
                break

            is_user_input_active = False

            # Envoyer les données saisies par l'utilisateur au robot
            data_to_send = bytearray(user_input, 'utf-8')
            await send_data(client, data_to_send)

async def main():
    print("Tapez ':' pour activer l'entrée utilisateur.")
    
    device_address = load_last_device()
    if not device_address:
        device_address = await find_device()
        if not device_address:
            print("Unable to find the device.")
            return
        save_last_device(device_address)

    try:
        async with BleakClient(device_address, timeout=30.0) as client:
            print(f"Connecté à {device_address}")
            
            global last_received_time
            last_received_time = asyncio.get_event_loop().time()

            await client.start_notify(CHARACTERISTIC_NOTIFY_UUID, notification_handler)

            # Créer une tâche pour vérifier la connexion
            user_input_task = asyncio.create_task(listen_for_user_input(client))

            connection_check_task = asyncio.create_task(check_connection(client))

            # Garder la connexion active en attendant les notifications et la déconnexion
            await user_input_task

    except BleakError as e:
        print(f"An error occurred: {str(e)}")
    except KeyboardInterrupt:
        print("\nDéconnexion en cours...")


# Exécuter la fonction principale
asyncio.run(main())


```

</details>

Pour pouvoir exécuter le script, vous devez installer les librairies manquantes. Dans Thonny, vous pouvez le faire en cliquant sur `Outils` > `Gérer les paquets...` et en ajoutant les librairies suivantes :
- `bleak`
- `asyncio`

---

### Fonctionnement du script
Le script Python permet de communiquer avec le module Bluetooth du robot MakeBlock Ranger.

- En lançant le script, il va rechercher le module Bluetooth avec l'adresse indiquée à la variable `DEVICE_NAME`.
- Une fois la connexion établie, le script va afficher les messages reçus du module Bluetooth comme le ferait le moniteur série de l'IDE Arduino.
- La touche ":" permet d'activer l'entrée utilisateur. Cela permet d'envoyer des données au module Bluetooth.
- La commande `quit` permet de quitter le script.
- <keyb>CTRL</keyb> + <keyb>C</keyb> permet de quitter le script.

---

# Code rapide du robot
Pour tester le fonctionnement rapidement du robot, vous pouvez utiliser le code suivant :

```cpp
unsigned long currentTime = 0;

String serialMessage;

void setup() {
  Serial.begin(115200);

}

void loop() {
  currentTime = millis();
  
  serialPrintTask(currentTime);

}

void serialPrintTask(unsigned long ct) {
  static unsigned long lastTime = 0;
  const unsigned int rate = 500;
  
  if (ct - lastTime < rate) return;
  
  lastTime = ct;
  
  Serial.println(ct);
  
}

void serialEvent() {
  if (!Serial.available()) return;
  
  serialMessage = Serial.readString();
  
  if (serialMessage.length() > 2) {
    // Retrait de l'entête 0xFF55
    serialMessage.remove(0, 2);
  }
  
  Serial.print ("Robot a reçu : ");
  Serial.println(serialMessage);
}
```

---

# Exercices
1. Installez Thonny sur votre ordinateur.
   - Installez les librairies `bleak` et `asyncio` dans Thonny.
2. Mettez le code Arduino de la section 'Code rapide du robot' dans votre robot MakeBlock Ranger.
3. Téléchargez les scripts Python sur votre ordinateur.
4. Exécutez le script `scan_robots.py` pour trouver l'adresse MAC de votre robot.
5. Exécutez le script `makeblock_bluetooth.py` pour communiquer avec votre robot.

---
# Références
- TODO : Ajouter les références...