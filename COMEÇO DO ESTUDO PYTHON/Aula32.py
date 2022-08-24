'''Como mover, copiar e apagar arquivos com Python'''

import os
import shutil

caminho_original = r'C:\Users\Junior\Desktop\Media\Serie'
caminho_novo = r'C:\Users\Junior\Desktop\Media\Serie2'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe.')

#for root, dirs, files in os.walk(caminho_original):
for root, dirs, files in os.walk(caminho_novo):#
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)
        
        if '.png' in file:
            os.remove(new_file_path) # os.remove para apagar a pasta citada dentro dos parenteses






       # if '.png' in file:
       #     shutil.copy(old_file_path, new_file_path) #shutil.move para mover, .copy para copiar.
        #    print(f'Arquivo {file} copiado com sucesso.')




