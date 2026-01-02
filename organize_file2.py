import shutil
from pathlib import Path

dir = Path("/storage/emulated/0/organizador")
imagenes = {"imagenes":[".jpg",".jpeg",".png",".gif",".webp",".svg"],}
videos ={"videos":[".mp4",".mkv",".avi",".mov"],}
documentos={ "documentos":[".pdf",".docx",".doc",".txt",".pptx",".xlsx"],}
codigo= {"codigo":[".py",".js",".java",".cpp",".c",".html",".css"],}
archivos = {"archivos":[".zip",".rar",".7z",".tar",".gz"],}
audio= {"audio":[".mp3",".wab",".aac",".wma"]
}
cat = imagenes

def organize_files(folder):
    for file in folder.iterdir():
        if file.is_file():
            print(file,"is_file")

            moved = False
            for category, extensions in cat.items():
                for ext in extensions:
                   if file.suffix.lower() == ext:
                       target_dir = Path(dir / category / ext)#C:/organizador/imagenes /.jpg
                       target_dir.mkdir(parents = True, exist_ok= True)
                       shutil.move(str(file),Path(target_dir/file.name))
                       moved = True
                       break
"""
        if not moved:
            other_dir = Path(dir / "other")
            other_dir.mkdir(parents = True,exist_ok = True)
            shutil.move(str(file),Path(other_dir/file.name))
"""
if __name__=="__main__":
    organize_files(Path("/storage/emulated/0/Pictures/Twitter"))# ruta existente
    print("Files organized  successfully!")
#Como Path aplica las rutas segun sea el SO es valido para cualquier sistema operativo
# Al ejecutar el codigo el directorio donde inicialmente se encuentran todos los archivos se queda vacio. los archivos no van a la carpeta definida por el diccionario se mueven  a la carpeta "other" tambien en la ruta dir

