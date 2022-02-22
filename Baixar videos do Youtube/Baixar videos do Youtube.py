from pytube import YouTube

# digite o link do video e o local que deseja salvar o video
link = input("digite o link do video que deseja baixar: ")
path = input("digite o diretório que deseja salvar o video: ")
yt = YouTube(link)

# Mostrar os detalhes do video
print("Titulo: ", yt.title)
print("Número de views: ", yt.views)
print(f"Tamanho do vídeo: {yt.length} segundos")
print("Avaliação do vídeo: ", yt.rating)

# Usa a maior resolução
ys = yt.streams.get_highest_resolution()

# Começa o Dowload do vídeo
print("Baixando...")
ys.download(path)
print("Download completo!")
