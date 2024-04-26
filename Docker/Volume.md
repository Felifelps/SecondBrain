# Volume

[Anterior: Image](Image.md)
[Próximo: Network](Network.md)

Como sabemos, quando criamos um container, todos os arquivos são sempre os memos, baseados numa image. Após a remoção do mesmo, todos os arquivos são deletados permanetemente. Como poderíamos manter arquivos gerados num container para que outros containeres também possam acessar? Volumes. 

Volumes são baldes de dados que permitem armazenar arquivos no Docker. Sua principal utilização está no armazenamento de arquivos de containeres, mas também são usados em caches e builds de images. 

O ato de persistir dados no Docker é chamado de *mounting*. Há vários tipos de mounting:
- *volume*: armazena os arquivos num volume pré-criado (ou gerado na hora);
- *bind*: conecta arquivos/diretórios locais com containeres;
- *tmpfs*: temporário;
- *cache*: armazena dados para evitar duplicação (usado apenas em Dockerfiles).

Vamos colocar a mão na massa. Para isso, vamos fazer um exemplo. Primeiro, edite crie um arquivo chamado `app.py`, com o seguinte código:

```python
# app.py
from flask import *
from peewee import *

db = SqliteDatabase('data.db')

class Note(Model):
    text = CharField(max_length=50)
    marked = BooleanField(default=False)
    class Meta:
        database = db

db.connect()

db.create_tables([Note], safe=True)

TEMPLATE = """<h1> Ultra Simple ToDo App </h1><input type="text" id="text" placeholder="Crie uma nova nota"> <button onclick="window.open('/new/' + document.getElementById('text').value, '_self')">Criar</button>{% if notes %}<ul>{% for note in notes %}<li><input type="checkbox" id="{{note.text}}" onclick="window.open('/mark/{{note.id}}/' + document.getElementById('{{note.text}}').checked, '_self')" {% if note.marked %} checked {% endif %} >{% if note.marked %} <s> {% endif %} {{note.text}} {% if note.marked %} </s> {% endif %}<a href="/del/{{ note.id }}"><img src="https://cdn-icons-png.flaticon.com/128/542/542724.png"width="15px" height="15px"></a></li>{% endfor %}</ul>{% else %}<p> Nenhuma nota criada!</p>{% endif %}"""

app = Flask(__name__)

@app.route('/')
def main():
    return render_template_string(
        TEMPLATE,
        notes=Note.select()
    )
 
@app.route('/new/<text>')
def new(text):
    Note.create(text=text)
    return redirect('/')

@app.route('/del/<note_id>')
def delete(note_id):
    Note.get_by_id(int(note_id)).delete_instance()
    return redirect('/')

@app.route('/mark/<note_id>/<value>')
def mark(note_id, value):
    note = Note.get_by_id(int(note_id))
    note.marked = value == "true"
    note.save()
    return redirect('/')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
```

Esse código gera um todo app simples com Flask integrado, por meio da biblitoeca Peewee, com um banco de dados Sqlite3. No mesmo diretório, crie um arquivo chamado `requirements.txt` com o seguinte conteúdo:

```r
blinker==1.7.0
click==8.1.7
colorama==0.4.6
Flask==3.0.3
itsdangerous==2.2.0
Jinja2==3.1.3
MarkupSafe==2.1.5
peewee==3.17.3
Werkzeug==3.0.2
```

Esse arquivo especifica as dependências do projeto. Agora, vamos ao Dockerfile:

```Dockerfile
# Dockerfile
FROM python:3.11.6-slim as base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD python3 -m flask run --host=0.0.0.0
```

Após isso, gere a image:

```shell
docker build -t volume-example .
```

E rode um container baseado nela:

```shell
docker run -dp 127.0.0.1:5000:5000 --name my-container volume-example
```

Agora, acesse [esse link](http://localhost:5000), e crie algumas notas. Agora, delete o container que você criou:

```shell
docker rm -f my-container
```

Agora, recrie o mesmo container, e acesse o link acima. Viu algo de diferente? **Suas notas não estão mais lá.** Ao reiniciar o container, recriamos o arquivo `data.db` que armazenava suas notas. Para evitar isso, vamos criar um volume. **Lembre-se de deletar o container que criamos.** Execute o seguinte comando:

```shell
docker volume create data-db
```

Agora iremos recriar o container e conectá-lo ao volume:

```shell
docker run -dp 127.0.0.1:5000:5000 -v data-db:/app/data --name my-container volume-example
```

Pronto!! Associamos o diretório `/app/data` (criado automaticamente pelo peewee para armazenar os dados) ao volume `data-db`. Dessa forma, qualquer alteração feita nessa pasta será mantida pelo Docker e qualquer container pode acessá-la. Faça o teste: crie algumas notas, remova o container e o recrie novamente. 

## Mounting

Como dito, mounting é o ato de persistir dados no Docker. É possível realizar mounting em containers a partir da tag `-v`, como vimos, mas também com a tag `--mount`. Vamos ver a utilização de ambas.

### Volume Mounting

É o padrão. Apenas cria um espaço no Docker pra guardar certa pasta do container. 
- `-v volume-name:diretorio`
- `--mount src=volume-name,target=diretorio`

## Bind Mount

Nesse tipo de mounting, você seleciona uma pasta pra ser "compartilhada" com o container. Ele vai analisar toda e qualquer alteração na pasta escolhida e atualizar automaticamente dentro do container. Muito usado pra teste de aplicações.
- `-v dir-local:dir-equivalente`
- `--mount type=bind,src=dir-local,target=dir-equivalente`

## Temporary Mount

Só funcionam em Linux, e têm a mesma lógica do container: ficam disponíveis apenas na memória do host, e são apagados quando o container é removido. São úteis quando se precisam armazenar dados sensitivos brevemente.


![Bind mounts on the Docker host](https://docs.docker.com/storage/images/types-of-mounts-bind.webp?w=450&h=300)

Enfim, abaixo temos os comandos relacionados a volumes. E vamos ao próximo tópico.

[Anterior: Image](Image.md)
[Próximo: Network](Network.md)

## Comandos

Comandos importantes:
- `docker volume create <volume-name>`: cria um volume;
* `docker volume inspect <volume-name>`: devolve dados do volume
* `docker volume ls`: lista todos os volumes;
* `docker volume rm <volume-name>`: deleta um volume;