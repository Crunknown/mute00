from pyrogram import Client,filters

from pyrogram.types import Message

import time
api_id = 18792984
api_hash = "68c28ffb97b439f6e99160eb63eea5fd"
bot = Client("newpup2",api_id,api_hash)
lis = []
username = "Cr_unknown"#without @
helper_list = """/mute
/unmute
 mlist(list mute ha)
/clear(clear mute list)"""
@bot.on_message()
def action(cli:Client, m:Message):
    word = m.text
    grop = m.chat.id
    ch_id = m.from_user.username
    ch_mute = m.from_user.id
    
    if ch_id == username:
        if word == "/help":
            m.edit(helper_list)
        if "/mute" in word:
            m.reply("set in...")
            if "list" in lis:
                lis.remove("list")
            if "_list" in lis:
                lis.remove("_list")
            edired = word.replace("/mute", "").replace(" ", "")
            lis.append(edired)
        if "/unmute" in word:
            m.reply("ok!")
            if "list" in lis:
                lis.remove("list")
            if "_list" in lis:
                lis.remove("_list")
            edired2 = word.replace("/unmute", "").replace(" ", "").replace("@", "")
            lis.remove(edired2)            
        if word == "/mlist":
            if "list" in lis:
                lis.remove("list")
            if "_list" in lis:
                lis.remove("_list")            
            m.reply(lis)
        if word == "/clear":
            m.reply("mute list cleaned!")
            lis.clear()
    
    if str(ch_mute) in lis:
        m.delete()
    else:
        pass
    
                
                
        
        
bot.run()
