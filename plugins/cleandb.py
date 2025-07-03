from pyrogram import Client, filters
from pyrogram.types import *
from info import ADMINS  # ya jahan se aapka admin ID define hai
from database.ia_filterdb import col, sec_col, get_file_details, unpack_new_file_id, get_bad_files

@Client.on_message(filters.command("cleandb") & filters.user(ADMINS))
async def clean_database(client, message: Message):
    collection = db["MkMoviescollection"]  # ya aapke config se COLLECTION_NAME
    result = await collection.delete_many({ "file_id": { "$exists": False } })
    await message.reply_text(f"✅ Deleted {result.deleted_count} old entries without file_id.")
