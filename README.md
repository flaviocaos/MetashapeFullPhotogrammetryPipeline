**Projeto**
Este projeto é um pipeline completo de processamento fotogramétrico utilizando o Agisoft Metashape 2.1.
O objetivo é automatizar o fluxo de trabalho para imagens aéreas oblíquas sem georreferenciamento direto, utilizando pontos de controle (GCPs) para corrigir a orientação e gerar:

Alinhamento de câmeras

Nuvem de pontos densa

Modelo 3D (malha)

Modelos digitais de superfície (MDS/DSM) e terreno (MDT/DEM)

Ortomosaico georreferenciado

Exportação dos resultados em formatos como GeoTIFF, LAS e OBJ

**Funcionalidades**
Importação automática de imagens aéreas

Importação de pontos de controle externos (.txt)

Georreferenciamento via GCPs

Geração de nuvem de pontos, malha 3D, DEM e ortomosaico

Exportação automática dos produtos finais

Tratamento de erros e validações básicas

**Estrutura Esperada**
/caminho/para/imagens/
    - foto1.jpg
    - foto2.jpg
    - ...
/caminho/para/gcps.txt
/caminho/para/saida/

As imagens devem ser JPG, JPEG, TIF ou TIFF.

O arquivo gcps.txt deve conter os pontos de controle com o seguinte formato:

NomeDoPonto  Coordenada_E  Coordenada_N  Cota_Z
Ponto01      123456.78     9876543.21    500.50
Ponto02      123460.00     9876547.00    501.00
(Separados apenas por espaço, sem ponto e vírgula)

**Requisitos**
Agisoft Metashape Professional 2.1 (ou superior)

Python 3.x (já integrado no Metashape)

Licença válida do Metashape

**Como Usar**

1) Instale o Metashape e ative sua licença.

2) Edite o script:

Atualize as seguintes variáveis no início do código:
PHOTOS_PATH = "caminho/para/imagens"
GCP_FILE = "caminho/para/gcps.txt"
OUTPUT_FOLDER = "caminho/para/saida"
COORDINATE_SYSTEM = "EPSG:31983"  # Modifique para o EPSG do seu projeto

3) Execute o script via terminal do Windows:
   
"C:\\Program Files\\Agisoft\\Metashape Pro\\metashape.exe" -r caminho/para/seu_script.py

4) Resultados exportados:

ortomosaico.tif (GeoTIFF)

nuvem_densa.las

malha_3d.obj

dem.tif

**Observações**

Se algum GCP não for identificado corretamente, o Metashape emitirá avisos. Certifique-se de marcar os pontos manualmente se necessário.

O sistema de coordenadas EPSG precisa ser ajustado conforme o seu projeto.

O script foi desenvolvido para rodar no ambiente Windows.

**Licença**

Distribuído sob a licença MIT.
Consulte o arquivo LICENSE para mais informações.

**Exemplos Visuais**

Workflow:

Importar imagens → Importar GCPs → Alinhar Câmeras → Gerar Nuvem → Construir Malha → Construir DEM → Construir Ortomosaico → Exportar Resultados





