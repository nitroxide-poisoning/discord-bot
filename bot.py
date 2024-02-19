BOT_TOKEN = "MTIwOTIzNzE2NjQ1NTAwMTE3OA.GOVcWF.2jDhvx5p90tHgUrOFxnm5TmhuVnnGj6XKMuzvA"

# This example requires the 'message_content' intent.

import discord
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    
    for guild in client.guilds:
        print("connected to server")

        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )

        print(f'Guild Members:\n - {guild.members}')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    print(message.content)

    if message.author == client.user:
        return

    if message.content[:7] == '!pickup':
        if '<@' in message.content:
            begin = message.content.index('<')
            end = message.content.index('>')
            print(message.content[begin:end+1])
            await message.channel.send(pickupgen(message.content[begin:end+1]))
        else:
            await message.channel.send(pickupgen("<@" + str(message.author.id) + ">"))

def pickupgen(name):
    quotes = [
        "When " + name + " walks with his dog outside, the dog says: \"He doesn't bite\".",
        name + " is the type of guy to bring a mattress to a pillow fight.",
        "Young " + name + ": arrives late \nTeacher: punishes every student for coming early",
        "When " + name + " goes swimming at the beach, the lifeguard blows the whistle and tells the sharks to get out of the water.",
        "When " + name + " goes to sleep, his nightmares are scared of him.",
        name + " looks like he cuts his hair with a shotgun",
        name + " never flushes the toilet, he scares the shit out of it",
        "One time " + name + " had a near-death experience, death will never forget the horror they felt that day.",
        name + " is the only one who can pause an online game.",
        "When the bell rings the teacher says \"the bell doesn't dismiss you, " + name + " does.\"",
        name + " won a staring contest against Medusa.",
        "The reason why we have time zones is because " + name + " told each place he travelled to what time it was",
        name + " is the only man that 6ix9ine wouldn't snitch on...",
        "Ghosts sit around camps and tell scary stories about " + name,
        "Once " + name + " arrived an hour late at school. That's why the world came up with daylight saving.",
        name + " played Russian roulette with a fully loaded gun and won.",
        name + "'s electronic devices didn’t die from low charge, they died from being so petrified of him.",
        "When " + name + " washes his hands, the water gets clean.",
        "When " + name + " gets stabbed, the knife gets rushed to the hospital.",
        name + " is the type of person that wears sunglasses to protect the sun from his eyes.",
        name + " is not in danger, he is the danger.",
        name + " once visited the Virgin Islands. They are now called, simply, The Islands.",
        "When " + name + " cheats on his GF, she apologizes for not being hot enough.",
        name + " was once bitten by a venomous snake. After 3 days of excruciating pain, the snake died.",
        "When " + name + " was born he taught his parents their first words",
        "When " + name + " calls the wrong number, the person apologizes for being the wrong person.",
        "When " + name + " stubbed his toe on a piece of furniture, the furniture got splinters.",
        "When " + name + " attends a concert, the guards shows him their entry tickets.",
        "When " + name + " don't win on the lottery, they change the numbers.",
        name + " looks like the .01% of germs that Lysol doesn’t kill.",
        "The doctor that slapped " + name + " on the day he was born was never seen again.",
        "When Graham Bell invented the phone, he noticed two missed calls from " + name + ".",
        "A freezer said that " + name + " was the only person to have more ice than itself.",
        name + " is the only man who can slip in the shower and grab the water",
        "When " + name + " sits in Santa's lap on Christmas, Santa asks him for presents.",
        "People get out of their wheelchairs to help " + name + " up the stairs.",
        "When " + name + " gets pulled over, he gives the cops a warning.",
        "When " + name + "’s phone rings in a movie theater, they put the movie on pause.",
        "When Joker said \"you know how I got these scars,\" he was cosplaying " + name + ".",
        "When " + name + " showed up in hell, Lil Nas X and the Devil started climbing back up the pole.",
        "When " + name + " goes to the airport he makes the officers go through the metal detectors"

    ]
    return random.choice(quotes)

client.run(BOT_TOKEN)
