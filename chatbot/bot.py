import discord
import responses

async def send_message(message,user_massege,is_private):
    try:
        response = responses.get_response(user_massege)
        if response:
            if is_private:
                await message.author.send(response)
            else:
                await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_dot():
    TOKEN = 'MTE2MTI3OTY3MDUzMzI0NzEyNw.GBku0K.z080u3uzptvaqJU_9NomsMbnt1amFgu8IciOO8'
    intent = discord.Intents.default()
    intent.message_content = True
    client = discord.Client(intents=intent)

    @client.event
    async def on_read():
        print(f'{client.user} is noe running!')


    @client.event
    async def on_message(message):
        if message.author ==client.user:
            return
        username = str(message.author)
        user_massage =str(message.content)
        channel = str(message.channel)

        print(f'{username}said:"{user_massage}"({channel}')

        if user_massage[0] == '?':
            user_massage = user_massage[1:] 
            await send_message(message,user_massage,is_private=True)
        else:
            await send_message(message,user_massage,is_private=False)

    client.run(TOKEN)

