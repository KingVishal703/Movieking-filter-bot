from pyrogram import Client, filters
from pyrogram.types import *
from info import ADMINS  # ya jahan se aapka admin ID define hai
from plugins.database import db  # yeh wahi db hai jo aap use kar rahe ho


from database.ia_filterdb import col, sec_col, get_file_details, unpack_new_file_id, get_bad_files
from database.users_chats_db import db, delete_all_referal_users, get_referal_users_count, get_referal_all_users, referal_add_user
from database.join_reqs import JoinReqs



@Client.on_message(filters.command("cleandb") & filters.user(ADMINS))
async def clean_database(client, message: Message):
    collection = db["MkMoviescollection"]  # ya aapke config se COLLECTION_NAME
    result = await collection.delete_many({ "file_id": { "$exists": False } })
    await message.reply_text(f"✅ Deleted {result.deleted_count} old entries without file_id.")
