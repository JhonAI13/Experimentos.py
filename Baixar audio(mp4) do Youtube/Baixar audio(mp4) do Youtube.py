from pytube import YouTube

# digite o link do video e o local que deseja salvar o audio do video
link = "https://www.youtube.com/watch?v=xlVaNMdBP24"
path = input("aqui")
yt = YouTube(link)

# Mostrar os detalhes do video
print("Titulo: ", yt.title)
print("Número de views: ", yt.views)
print(f"Tamanho do vídeo: {yt.length} segundos")
print("Avaliação do vídeo: ", yt.rating)

# Configurando para audio
ys = yt.streams.filter(only_audio=True)[0]


# Começa o Dowload do Audio
print("Baixando...")
ys.download(path)
print("Download completo!")
