import discord
from discord.ext import commands

#creacion de permisos para el bot
permisos = discord.Intents.default()
permisos.message_content = True

#creacion del bot, para que el bot funcione necesitamos una llave
loradillo = commands.Bot(command_prefix="!", intents=permisos)

@loradillo.event
async def on_ready():
    print(f'Bot conectado como {loradillo.user}')

@loradillo.command()
async def hola(ctx):
    await ctx.send("¡Hola! soy Loradillo, ¡tu asistente contra la contaminacion!")

@loradillo.command()
async def ayuda(ctx):
    ayuda_mensaje = """
    Comandos disponibles:
    !hola - El bot te saludará.
    !ayuda - Muestra este mensaje de ayuda.
    !ambiente - Proporciona consejos para cuidar el medio ambiente.
    !reciclar - Muestra una lista de materiales reciclables y no reciclables.
    """
    await ctx.send(ayuda_mensaje)  

@loradillo.command()
async def ambiente(ctx):
    consejos = """
    Aquí tienes algunos consejos para cuidar el medio ambiente de una manera más ecológica 🌍♻️:

    1. Recicla y reutiliza materiales siempre que sea posible ♻️🔁 (utiliza el comando !reciclar para mostrarte cuáles son reciclables y cuáles no).
    2. Ahorra agua y energía en tu hogar 💧⚡🏠.
    3. Usa transporte sostenible como bicicletas o transporte público 🚲🚌
    4. Planta árboles y cuida las áreas verdes 🌳🌿.
    5. Reduce el consumo de plásticos de un solo uso 🚫🧴.
    si quieres saber mas dirigete a la pagina oficial!!: http://127.0.0.1:5000/
    
    """
    await ctx.send(consejos)


@loradillo.command()
async def reciclar(ctx):
    reciclar_mensaje = """
    🗑️ Objetos que puedes tirar a la basura
    (residuos que no se reciclan)

    -Restos de comida 🍌🍗
    -Servilletas y papel higiénico usados
    -Pañales y toallas sanitarias
    -Colillas de cigarrillo
    -Cerámica rota (platos, tazas)
    -Papel o cartón muy sucio (con grasa o comida)
    -Esponjas, trapos viejos
    -Chicles
    ♻️ Objetos que debes reciclar
    (limpios y secos, importante)

    🧻 Papel y cartón
    -Hojas de cuaderno
    -Periódicos y revistas
    -Cajas de cartón
    -Bolsas de papel

    🥤 Plásticos
    -Botellas de agua o gaseosa
    -Envases de shampoo o detergente
    -Bolsas plásticas limpias
    -Tapas plásticas

    🍾 Vidrio
    -Botellas
    -Frascos de mermelada o salsa

    🥫 Metales
    -Latas de gaseosa o atún
    -Tapas metálicas
    """
    await ctx.send(reciclar_mensaje)

loradillo.run("MTQ0MzM4NTMzNDc0OTQ2Njc1NA.G5GHnD.y0HbVtNbC8QRV4qXyQXuOWEOzQGO2zpoYj_VmA")
