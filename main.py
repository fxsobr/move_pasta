from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time


class GerenciadorArquivos(FileSystemEventHandler):
    def on_modified(self, event):
        for arquivo in os.listdir(pasta_inicio):
            src = pasta_inicio + "/" + arquivo
            destino = pasta_destino + "/" + arquivo
            os.rename(src, destino)


pasta_inicio = "C:/Users/Administrador/Desktop/Teste"
pasta_destino = "C:/Users/Administrador/Documents/teste1"
evento_gerenciamento = GerenciadorArquivos()
observador = Observer()
observador.schedule(evento_gerenciamento, pasta_inicio, recursive=True)
observador.start()

try:
    while True:
        print("Rodando....")
        time.sleep(10)
except KeyboardInterrupt:
    print("Processo Encerrado...")
    observador.stop()
observador.join()


