import nest_asyncio
from telethon import TelegramClient, events
import os
import logging
import csv

# Apply the nest_asyncio patch
nest_asyncio.apply()

# Set up logging
logging.basicConfig(filename='telegram_scraper.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Define API credentials (you need to get your own API ID and Hash from my.telegram.org)
# Your API ID and hash
api_id = '24556085'
api_hash = 'e9d6e1688506f4b2d8ac19d1b3492c09'
phone_number = '+251968861733'

# Create the client and connect
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    # Connect to the client
    await client.start(phone_number)
    
    # List of channels to scrape
    channels = [
        'https://t.me/DoctorsET',
        'https://t.me/lobelia4cosmetics',
    ]
    
    # Directory to save images
    image_dir = 'images'
    os.makedirs(image_dir, exist_ok=True)
    
    # CSV file to save the scraped data
    csv_file = 'scraped_data.csv'
    
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['channel title', 'channel username', 'ID', 'Message', 'Date', 'Media Path'])
        
        for channel in channels:
            async for message in client.iter_messages(channel):
                media_path = None
                
                # Save images from the message
                if message.media:
                    media_path = await message.download_media(file=image_dir)
                    logging.info(f"Downloaded image: {media_path}")
                
                # Write the message details to the CSV file
                writer.writerow([
                    message.chat.title,
                    message.chat.username,
                    message.id,
                    message.text,
                    message.date,
                    media_path
                ])
                
                # Log the message text
                logging.info(f"Message from {channel}: {message.text}")

async def run():
    async with client:
        await main()

client.loop.run_until_complete(run())

print("Scraping completed. Check the log file for details.")
