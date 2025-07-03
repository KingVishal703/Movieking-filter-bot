from pyrogram import Client, filters
from pyrogram.types import Message
from config import OWNER_ID  # ya jahan se aapka admin ID define hai
from plugins.database import db  # yeh wahi db hai jo aap use kar rahe ho

@Client.on_message(filters.command("cleandb") & filters.user(OWNER_ID))
async def clean_database(client, message: Message):
    collection = db["MkMoviescollection"]  # ya aapke config se COLLECTION_NAME
    result = await collection.delete_many({ "file_id": { "$exists": False } })
    await message.reply_text(f"✅ Deleted {result.deleted_count} old entries without file_id.")
