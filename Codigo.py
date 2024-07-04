import discord
import asyncio

TOKEN = 'TU_TOKEN_DE_DISCORD'
CHANNEL_ID = TU_ID_DEL_CANAL  # Reemplaza con el ID de tu canal

# Lista de videos de YouTube
videos = [
    "https://www.youtube.com/ejemplo1",
    "https://www.youtube.com/ejemplo2",
    # Añade más enlaces aquí, hasta llegar a 50
]

client = discord.Client()

# Variable para llevar la cuenta del índice de video
current_index = 0

@client.event
async def on_ready():
    print(f'Bot conectado como {client.user}')
    global current_index
    channel = client.get_channel(CHANNEL_ID)
    while True:
        if current_index < len(videos):
            await channel.send(videos[current_index])
            current_index += 1
        else:
            current_index = 0  # Reinicia la lista si ya se mandaron todos los videos
        await asyncio.sleep(86400)

client.run(TOKEN)
