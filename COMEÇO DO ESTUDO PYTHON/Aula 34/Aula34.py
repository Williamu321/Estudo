# https://ffmpeg.org/ffmpeg.html
'''Concertendo videos com Python + FFMPEG'''

'''
ffmpeg -i "ENTRADA" -i "LEGENDA" -c:v libx264 -crf 23 -preset ultrafast -c:a aac -b:a 320k
-c:s srt -map v:0 -map a -map 1:0 -ss 00:00:00 -to 00:00:10 "SAIDA"
'''

from msilib.schema import CreateFolder
import os
import fnmatch
import sys
from ffmpeg import audio, video, image

if sys.platform == 'linux':
    comando_ffmpeg = 'ffmpeg'
else:
    comando_ffmepg = 'ffmpeg/ffmpeg.exe'

codec_video= 'libx264'
crf = '-crf 23'
preset = '-preset ultrafast' 
codec_audio = 'aac'
bitrate_audio = '-ba 320k'
debug = ' -ss 00:00:00 - to 00:00:10'

caminho_origem = r'C:\Users\Junior\Desktop\Media\Serie2'
caminho_destino = r'C:\Users\Junior\Desktop\Media\Serie'

for raiz,pastas, arquivos in os.walk(caminho_origem):
    for arquivo in arquivos:
        if not fnmatch.fnmatch(arquivo, '*.mkv'):
            continue

        caminho_completo = os.path.join(raiz, arquivo)
        nome_arquivo, extensao_arquivo = os.path.splitext(caminho_completo)
        caminho_legenda = nome_arquivo + '.srt'
        if os.path.isfile(caminho_legenda):
            input_legenda = f' -i "{caminho_legenda}"'
            map_legenda = ' -c:S srt -map v:0 -map a -map 1:0'
        else:
            input_legenda = ''
            map_legenda = ''

        nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
        
        nome_novo_arquivo = nome_arquivo + '_NOVO' + extensao_arquivo
        arquivo_saida = os.path.join(raiz, )

        comando = f' {comando_ffmepg} -i "{caminho_completo}" {input_legenda}'\
            f'{codec_video} {crf} {preset} {codec_audio} {bitrate_audio}'\
                f'{debug} {map_legenda} "{arquivo_saida}"'
        
        os.system(comando)


