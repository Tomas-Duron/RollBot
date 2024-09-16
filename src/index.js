import dotenv from 'dotenv';
dotenv.config()

import { Client, Events, GatewayIntentBits } from 'discord.js';

var token = process.env.DISCORD_TOKEN;

const client = new Client({ intents: [GatewayIntentBits.Guilds] });

client.once(Events.ClientReady, readyClient => {
	console.log(`Ready! Logged in as ${readyClient.user.tag}`);
});

client.login(token);