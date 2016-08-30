var Discord = require('discord.js');

var bot = new Discord.Client();

var photos = [
	'https://upload.wikimedia.org/wikipedia/commons/e/e9/DRG_bobber_caboose_at_CRM.jpg',
	'https://upload.wikimedia.org/wikipedia/commons/3/3d/Cupola_caboose.jpg',
	'http://s3.amazonaws.com/ClubExpressClubFiles/541047/graphics/caboose.jpg',
	'https://upload.wikimedia.org/wikipedia/commons/f/f8/C%26O_caboose_90776.jpg',
	'http://images.clipartpanda.com/train-caboose-clipart-nTEK4gbTA.jpeg',
    'http://www.ridgwayrailroadmuseum.org/RestoredCaboose.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/6/66/Caboose.JPG',
    'http://www.todayifoundout.com/wp-content/uploads/2015/06/caboose.jpg',
    'http://keyboardsforchrist.com/nyc_inside.jpg',
    'http://www.oregonpacificrr.com/images/Caboose25198header2.jpg',
    'http://www.richyodermodels.com/rym_images/ebt/600x331_caboose_top_of_order_form.JPG'
];

bot.on('message', function(message) {
	if (!message.author.bot) {
		if (message.content.toLowerCase().indexOf('aboos') !== -1 || message.content.toLowerCase().indexOf('abuse') !== -1) {
			bot.sendMessage(message, message.author + ' INVOKED THE _**__ABOOS CABOOSE__**_\n' + photos[parseInt(Math.random() * photos.length)]);
		}
	}
});

bot.loginWithToken('MjIwMTU4NjM4NzMwMzc5MjY1.CqcVrw.Fj2IMYmzt5CAzhotO-ZVBtU0DSc');