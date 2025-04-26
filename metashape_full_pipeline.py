
import Metashape
import os

# === CONFIGURACOES GERAIS ===
PHOTOS_PATH = "caminho/para/imagens"   # Pasta onde estao as imagens
GCP_FILE = "caminho/para/gcps.txt"      # Arquivo de pontos de controle (sem ';', apenas espacos)
OUTPUT_FOLDER = "caminho/para/saida"    # Pasta onde salvar resultados
COORDINATE_SYSTEM = "EPSG:31983"         # Exemplo: SIRGAS 2000 / UTM zone 23S

# === FUNCOES DO PROCESSO ===

def criar_projeto():
    doc = Metashape.Document()
    chunk = doc.addChunk()
    return doc, chunk

def adicionar_fotos(chunk, path):
    imagens = [os.path.join(path, f) for f in os.listdir(path) if f.lower().endswith(('jpg', 'jpeg', 'tif', 'tiff'))]
    if not imagens:
        raise FileNotFoundError("Nenhuma imagem encontrada no diretorio fornecido.")
    chunk.addPhotos(imagens)
    print(f"{len(imagens)} imagens adicionadas com sucesso.")

def importar_gcps(chunk, gcp_file):
    if not os.path.exists(gcp_file):
        raise FileNotFoundError("Arquivo de pontos de controle nao encontrado.")

    with open(gcp_file, 'r') as file:
        linhas = file.readlines()

    for linha in linhas:
        partes = linha.strip().split()
        if len(partes) != 4:
            raise ValueError(f"Formato incorreto na linha: {linha}")
        nome, x, y, z = partes
        marker = chunk.addMarker()
        marker.label = nome
        marker.reference.location = Metashape.Vector([float(x), float(y), float(z)])
    print(f"{len(linhas)} pontos de controle importados.")

def definir_sistema_coordenadas(chunk, epsg_code):
    chunk.crs = Metashape.CoordinateSystem(epsg_code)
    print(f"Sistema de coordenadas definido para {epsg_code}.")

def alinhar_cameras(chunk):
    chunk.matchPhotos(accuracy=Metashape.HighAccuracy, preselection_generic=True, preselection_reference=True)
    chunk.alignCameras()
    print("Alinhamento de camaras concluido.")

def otimizar_ajuste(chunk):
    chunk.optimizeCameras()
    print("Ajuste otimizado com pontos de controle.")

def gerar_nuvem_densa(chunk):
    chunk.buildDepthMaps(quality=Metashape.MediumQuality)
    chunk.buildDenseCloud()
    print("Nuvem de pontos densa gerada.")

def gerar_malha(chunk):
    chunk.buildModel(surface_type=Metashape.Arbitrary, interpolation=Metashape.EnabledInterpolation)
    print("Malha 3D gerada.")

def gerar_dem(chunk):
    chunk.buildDem(source_data=Metashape.DenseCloudData)
    print("Modelo Digital de Terreno (MDT/DEM) gerado.")

def gerar_ortomosaico(chunk):
    chunk.buildOrthomosaic(surface_data=Metashape.ElevationData)
    print("Ortomosaico gerado.")

def exportar_resultados(chunk, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    chunk.exportOrthomosaic(os.path.join(output_folder, "ortomosaico.tif"))
    chunk.exportPoints(os.path.join(output_folder, "nuvem_densa.las"))
    chunk.exportModel(os.path.join(output_folder, "malha_3d.obj"))
    chunk.exportDem(os.path.join(output_folder, "dem.tif"))
    print("Resultados exportados com sucesso.")

# === FLUXO PRINCIPAL ===

def main():
    try:
        doc, chunk = criar_projeto()
        adicionar_fotos(chunk, PHOTOS_PATH)
        importar_gcps(chunk, GCP_FILE)
        definir_sistema_coordenadas(chunk, COORDINATE_SYSTEM)
        alinhar_cameras(chunk)
        otimizar_ajuste(chunk)
        gerar_nuvem_densa(chunk)
        gerar_malha(chunk)
        gerar_dem(chunk)
        gerar_ortomosaico(chunk)
        exportar_resultados(chunk, OUTPUT_FOLDER)
        print("\n=== Processamento completo com sucesso! ===")
    except Exception as e:
        print(f"Erro durante o processamento: {e}")

if __name__ == "__main__":
    main()
