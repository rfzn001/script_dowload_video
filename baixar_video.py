import yt_dlp
import os

video_url = 'https://www.youtube.com/watch?v=MoLsBEfl1SE'

output_directory = '/home/rfznn/Projetos/Scraping/Videos'

os.makedirs(output_directory, exist_ok=True)

ydl_opts = {
    'format': 'bestvideo+bestaudio/best',  # Melhor qualidade e áudio 
    'merge_output_format': 'mp4',  # Formato de saída combinado
    'outtmpl': os.path.join(output_directory, 'video_com_som.mp4'),
    'postprocessors': [{  # Combinar áudio e vídeo
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',  # Saída
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

print("Download concluído!")