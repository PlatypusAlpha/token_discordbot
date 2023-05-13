# token_discordbot
Discord bot that scrapes a Cardano token from the public Minswap token pair API and updates every 5 mins.
This bot requires that you have already setup your discord development account and invited it to your discord server.


### How to find my minswap ID
1. Click this [link](https://api-mainnet-prod.minswap.org/coinmarketcap/v2/pairs)
2. cmd+f or ctrl+f to search in browser for ticker
3. The page is all in json, you will be looking for the key that starts your dictionary object
Video extra: https://share.getcloudapp.com/2Nub48zO

## Discord bot
Here is a [perfect tutorial](https://discordpy.readthedocs.io/en/stable/discord.html) that covers the creation process with referece to discord.py.


### Deployment
We used [digitalocean's](https://m.do.co/c/025c33555e29) App services to run our worker bots. Using our digital ocean link here will give you $200 in credits to use towards your bot deployment.
Digitalocean has lots of great documentation, here is the [python example docs](https://docs.digitalocean.com/products/app-platform/quickstart/sample-apps/python/#usage)


### Gotchas
1. Make sure to create you global environment variables. There are two for this bot. `TOKEN` & `MINSWAP_ID`
2. Always change your plan, digitalocean steps up your plan by default
3. Make sure to edit your run commands `python3 main.py`

