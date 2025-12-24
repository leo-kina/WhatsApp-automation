# 📄 WhatsApp Document Reader — QI Tech




Este projeto foi desenvolvido para uso interno no trabalho da **QI Tech**.  
A aplicacao automatiza a leitura de mensagens de grupos do **WhatsApp Web**, identifica **CPFs e CNPJs** enviados por comando e salva os dados em um arquivo **Excel**, evitando duplicidade de registros.

O script utiliza automacao via **Selenium** e exige interacao manual do usuario durante a execucao.

---

## 🚀 Tecnologias Utilizadas

- **Python 3**
- **Selenium**
- **Pandas**
- **Google Chrome + ChromeDriver**
- **WhatsApp Web**

---

## 📂 Estrutura do Projeto


```text
project/
│
├── main.py
├── services/
│   ├── whatsapp_service.py
│   └── excel_service.py
│
├── utils/
│   └── parsers.py
│
├── config/
│   └── settings.py
│
└── requirements.txt
└── README.md
```
# Como Utilizar
### 1. Clone o repositório

```bash
git clone https://github.com/seu-repo/exemplo
cd nomedoprojeto

```
### 2. Instale as dependências
```bash
pip install -r requirements.txt
```
### 3. Execute 
```bash
python main.py
```
### 4. WhatsApp
```bash
Escanei o QR Code e abra o grupo desejado
```
### 4. WhatsApp
```bash
Use o scroll do mouse para scan novas msg
Quando desejar acabar, clique no ENTER no terminal
```
---