# Tutorial de Uso do Pipeline Metashape

Este tutorial explica como utilizar o script `metashape_full_pipeline.py` para processar imagens aéreas com o Agisoft Metashape.

---

## 📁 Estrutura Esperada

```
/projeto/
├── imagens/
│   ├── foto1.jpg
│   ├── foto2.jpg
│   └── ...
├── gcps.txt
├── metashape_full_pipeline.py
├── config_example.json
└── saida/
```

---

## ⚙️ Etapa 1 – Requisitos

- Agisoft Metashape Professional 2.1+ (licenciado e instalado)
- Python 3.x (já incluso no Metashape)
- Windows 10 ou superior

---

## 📝 Etapa 2 – Editar o Script

No início do `metashape_full_pipeline.py`, edite as seguintes variáveis:

```python
PHOTOS_PATH = "caminho/para/imagens"
GCP_FILE = "caminho/para/gcps.txt"
OUTPUT_FOLDER = "caminho/para/saida"
COORDINATE_SYSTEM = "EPSG:31983"
```

Você também pode usar o `config_example.json` como referência.

---

## ▶️ Etapa 3 – Executar o Pipeline

Via terminal do Windows:

```bat
"C:\Program Files\Agisoft\Metashape Pro\metashape.exe" -r caminho\para\metashape_full_pipeline.py
```

Ou utilize o script `run_pipeline.bat` para facilitar a execução.

---

## 📤 Etapa 4 – Resultados Exportados

Após a execução, os seguintes arquivos serão gerados em `OUTPUT_FOLDER`:

- `ortomosaico.tif`
- `nuvem_densa.las`
- `malha_3d.obj`
- `dem.tif`

---

## ⚠️ Observações

- Certifique-se de que o arquivo `gcps.txt` está no formato correto:
  ```
  Ponto01  123456.78  9876543.21  500.50
  Ponto02  123460.00  9876547.00  501.00
  ```
- O EPSG do projeto deve estar de acordo com a área de interesse.
- O Metashape pode requerer marcação manual dos GCPs se não forem reconhecidos automaticamente.

---

## 📚 Dúvidas Frequentes

**Q: Posso usar imagens inclinadas ou só nadirais?**  
A: O pipeline é compatível com imagens oblíquas.

**Q: Posso rodar fora do Windows?**  
A: O script foi testado apenas no ambiente Windows com Metashape.

---

## 🧪 Testado em:

- Metashape Professional 2.1.0
- Windows 11
- Projeto com 45 imagens JPG + 5 GCPs
