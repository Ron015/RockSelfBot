import discord
import requests

async def setup(bot):
    @bot.command()
    async def anime(ctx, *, query: str = None):
        if not query:
            await ctx.send("❗ Please provide an anime name to search, e.g., `!anime Naruto`", delete_after=5)
            return

        url = f"https://api.jikan.moe/v4/anime?q={query}&limit=1"
        response = requests.get(url)
        anime_data = response.json()

        if response.status_code == 200 and anime_data['data']:
            anime = anime_data['data'][0]
            title = anime.get("title", "N/A")
            synopsis = anime.get("synopsis", "No synopsis available")
            image_url = anime.get("images", {}).get("jpg", {}).get("image_url", "")
            score = anime.get("score", "No score available")
            url = anime.get("url", "#")

            await ctx.send(f"**Anime Search Result for '{query}':**\n"
                           f"**Title:** {title}\n"
                           f"**Score:** {score}\n"
                           f"**Synopsis:** {synopsis[:1500]}...\n"
                           f"**Link:** {url}\n"
                           f"**Image:** {image_url}")
        else:
            await ctx.send(f"No anime found for '{query}'.", delete_after=5)