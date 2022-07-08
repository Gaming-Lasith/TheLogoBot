@bot.on_message(filters.command("mask") & ~filters.forwarded)
async def logomake(_, message: Message):
    if len(message.command) != 2:
        return await message.reply_text("Please give a text.\nEx:`/logo Name` ")
    else:
        pass
    m = await message.reply('Designing your logo...wait!')
    await m.edit("Logo in processing...\n░░░░░░░░░░ 0%")
    await m.edit("Logo in processing...\n▇▇░░░░░░░░ 20%")
    await m.edit("Logo in processing...\n▇▇▇▇░░░░░░ 40%")
    await m.edit("Logo in processing...\n▇▇▇▇▇▇░░░░ 60%")
    await m.edit("Logo in processing...\n▇▇▇▇▇▇▇▇░░ 80%")
    await m.edit("Logo in processing...\n▇▇▇▇▇▇▇▇▇▇ 100%")
    await m.edit("📤Uploading...")
    text = message.text.split(None, 1)[1]
    Image_STD = Image.open("./bot/resources/maskbg.jpg")
    Image_font = ImageFont.truetype("./bot/resources/Flashing.otf", 220)
    Image_font2 = ImageFont.truetype("./bot/resources/Flashing.otf", 100)
    Image_text = f"ItsMeSithija"
    Image_edit = ImageDraw.Draw(Image_STD)
    image_width, image_height = Image_STD.size
    Image_edit.text((600, 600), text, (255, 255, 255), anchor="mt", font = Image_font)
    Image_STD.save("masklogo.jpg")
    await message.reply_photo(
                photo=f"masklogo.jpg",
                caption=f"Created by @AmazingLogosBot",
            )
    await m.delete()
