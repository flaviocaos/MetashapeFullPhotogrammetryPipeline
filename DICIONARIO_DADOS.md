
# Dicionário de Dados – Pipeline Fotogramétrico com Metashape

Este documento descreve os principais parâmetros, arquivos de entrada, saída e variáveis do script `metashape_full_pipeline.py`.

---

## 🔧 Parâmetros de Configuração

| Nome               | Tipo    | Descrição                                                                 |
|--------------------|---------|---------------------------------------------------------------------------|
| `PHOTOS_PATH`      | string  | Caminho para a pasta com as imagens (JPG, JPEG, TIF, TIFF)                |
| `GCP_FILE`         | string  | Caminho para o arquivo `.txt` com pontos de controle                      |
| `OUTPUT_FOLDER`    | string  | Caminho para a pasta de saída onde serão salvos os produtos gerados       |
| `COORDINATE_SYSTEM`| string  | Código EPSG do sistema de coordenadas utilizado no projeto                 |

---

## 📥 Arquivos de Entrada

| Nome               | Formato | Descrição                                                                 |
|--------------------|---------|---------------------------------------------------------------------------|
| Imagens            | .jpg/.jpeg/.tif/.tiff | Fotos aéreas do levantamento                                          |
| GCPs               | .txt    | Arquivo texto com nome e coordenadas dos pontos (E, N, Z), separados por espaço |

**Exemplo de linha no arquivo GCP:**

```
Ponto01 123456.78 9876543.21 500.50
```

---

## 📤 Arquivos de Saída

| Nome do Arquivo       | Formato  | Descrição                                       |
|------------------------|----------|-------------------------------------------------|
| `ortomosaico.tif`      | GeoTIFF  | Ortomosaico georreferenciado                    |
| `nuvem_densa.las`      | LAS      | Nuvem de pontos densa                           |
| `malha_3d.obj`         | OBJ      | Modelo 3D em malha                              |
| `dem.tif`              | GeoTIFF  | Modelo Digital de Elevação (DEM/MDT)           |

---

## ⚙️ Principais Funções do Código

| Função                  | Finalidade                                                        |
|--------------------------|-------------------------------------------------------------------|
| `criar_projeto()`        | Inicializa um novo projeto e chunk                                |
| `adicionar_fotos()`      | Adiciona imagens do diretório informado                           |
| `importar_gcps()`        | Lê os GCPs e adiciona ao chunk                                    |
| `definir_sistema_coordenadas()` | Define o sistema de referência com base no EPSG            |
| `alinhar_cameras()`      | Realiza a correspondência e o alinhamento das câmeras             |
| `otimizar_ajuste()`      | Otimiza a câmera com base nos GCPs                                |
| `gerar_nuvem_densa()`    | Gera o mapa de profundidade e a nuvem de pontos                   |
| `gerar_malha()`          | Constrói a malha 3D                                                |
| `gerar_dem()`            | Gera o DEM com base na nuvem densa                                |
| `gerar_ortomosaico()`    | Gera o ortomosaico a partir da superfície do DEM                  |
| `exportar_resultados()`  | Exporta todos os produtos para a pasta de saída                   |

---

## 📎 Observações

- O Metashape utiliza o sistema de coordenadas definido por EPSG.
- Os GCPs devem estar em coordenadas planas (UTM) e seguir o padrão especificado.
- O script é modular e pode ser adaptado para processamentos parciais (ex: só até o DEM).

