
---

# 🌐 API de Tradução

Bem-vindo à API de Tradução! Esta API permite traduzir textos para diversos idiomas e consultar a lista de idiomas suportados. Desenvolvida com Flask, ela usa a biblioteca `googletrans` para processar traduções.

## ✨ Funcionalidades

- **Tradução de Texto**: Traduz um texto para o idioma desejado.
- **Consulta de Idiomas Suportados**: Retorna a lista de idiomas que podem ser utilizados na tradução.

---

## 🚀 Endpoints

### 📄 Sumário

1. [🎯 POST `/translate`](#1-translate-traduza-um-texto)
2. [🌐 GET `/languages`](#2-languages-idiomas-suportados)

---

### 1. 🎯 `/translate` (Traduza um texto)

- **Descrição**: Traduz um texto para o idioma especificado.
- **Método**: `POST`
- **Corpo da Requisição** (JSON):
  - `text` (string): Texto a ser traduzido. **Obrigatório**.
  - `target_lang` (string): Código do idioma de destino. Padrão: `"en"` (inglês).
  
#### Exemplo de Requisição

```json
POST /translate
Content-Type: application/json

{
  "text": "Olá, mundo!",
  "target_lang": "en"
}
```

#### Respostas

- **200 OK**: Retorna o texto traduzido.
  - **Exemplo**:
    ```json
    {
      "translated_text": "Hello, world!"
    }
    ```

- **400 Bad Request**: Erro quando o texto não é fornecido ou o idioma não é suportado.
  - **Exemplo**:
    ```json
    {
      "error": "Texto não fornecido para tradução"
    }
    ```

- **500 Internal Server Error**: Erro no processo de tradução.
  - **Exemplo**:
    ```json
    {
      "error": "Erro interno ao processar a tradução"
    }
    ```

---

### 2. 🌐 `/languages` (Idiomas Suportados)

- **Descrição**: Retorna a lista de idiomas suportados pela API.
- **Método**: `GET`

#### Exemplo de Requisição

```http
GET /languages
```

#### Respostas

- **200 OK**: Retorna um objeto JSON com os idiomas suportados.
  - **Exemplo**:
    ```json
    {
      "af": "afrikaans",
      "sq": "albanian",
      "ar": "arabic",
      ...
    }
    ```

---

## 📌 Códigos de Status HTTP

| Código | Descrição                         |
|--------|-----------------------------------|
| 200    | Requisição bem-sucedida           |
| 400    | Parâmetros inválidos              |
| 500    | Erro no servidor                  |

---

## 🛠️ Configuração

1. Instale as dependências:
   ```bash
   pip install flask googletrans==4.0.0-rc1
   ```
2. Execute o servidor:
   ```bash
   python app.py
   ```

## 🌍 Variáveis de Ambiente

- **PORT**: Define a porta em que a aplicação será executada. Padrão: `5000`.

---

## 📋 Exemplos de Uso

### Traduzir Texto
```bash
curl -X POST http://localhost:5000/translate \
-H "Content-Type: application/json" \
-d '{"text": "Olá, mundo!", "target_lang": "en"}'
```

### Obter Idiomas Suportados
```bash
curl http://localhost:5000/languages
```

---

## 📝 Observações

Esta API usa a biblioteca `googletrans`, que depende do serviço do Google Translate. Em caso de instabilidade no serviço, pode haver erros no processo de tradução.

---
