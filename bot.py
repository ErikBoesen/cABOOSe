import discord
import re
from random import randint

photos = [
    'https://upload.wikimedia.org/wikipedia/commons/e/e9/DRG_bobber_caboose_at_CRM.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/3/3d/Cupola_caboose.jpg',
    'http://s3.amazonaws.com/ClubExpressClubFiles/541047/graphics/caboose.jpg',
    'http://images.clipartpanda.com/train-caboose-clipart-nTEK4gbTA.jpeg',
    'http://www.ridgwayrailroadmuseum.org/RestoredCaboose.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/6/66/Caboose.JPG',
    'http://www.todayifoundout.com/wp-content/uploads/2015/06/caboose.jpg',
    'http://keyboardsforchrist.com/nyc_inside.jpg',
    'http://www.oregonpacificrr.com/images/Caboose25198header2.jpg',
    'http://www.richyodermodels.com/rym_images/ebt/600x331_caboose_top_of_order_form.JPG'
]


class Bot(discord.Client):
    def __init__(self):
        """
        Initialize bot.

        :param token: Bot account token.
        """
        super().__init__()

        print('Starting Caboose...')

    async def on_ready(self):
        """Run when the bot is ready."""
        print('READY 2 FITE ABOOS!!')

    async def on_message(self, message):
        """Catch a user's messages and figure out what to return."""
        try:
            contains_aboos = bool(re.search(r'abo*se?', message.content, re.IGNORECASE).group(0))
        except AttributeError:
            contains_aboos = False

        if contains_aboos and not message.author.bot:
            photo_id = randint(0, len(photos)-1)
            print('THERE IS ABOOS SO SENDING PHOTO #%s' % photo_id)
            await self.send_message(message.channel, '_**__ABOOS CABOOSE ACTIVATED__**_\n%s' % photos[photo_id])


if __name__ == '__main__':
    token = open('token.txt', 'r').read().replace('\n', '')

    bot = Bot()
    bot.run(token)
