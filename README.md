## Uploader

O projeto tem como objeto a transferência de arquivos de dispositivos moveis para o desktop, sem depender de cabos ou permissões do dispositivo.

O server roda localmente, usando uma pagina web para enviar os arquivos via **POST**.

### Como usar?

Na pasta raiz do projeto execute:
```shell
fastapi run uploader/main.py
```

### Como surgiu?

Surgiu como uma ideia de por em pratica o entendimento/aprendizado do modulo built-in **shutil**.

### Rotas

- Pagina raiz para abrir o explorador de arquivos.

>  GET  localhost:8000

#### Usando o uploader sem pagina web
-  Rota para salvar o arquivo no desktop. É necessario enviar o arquivo  no body da requisição.

- > POST /uploader
