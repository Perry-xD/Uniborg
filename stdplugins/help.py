from telethon import events, client
from uniborg import CMD_HELP




@events.register(events.NewMessage(pattern="!help"))
async def helphandler(event):
  args = event.pattern_match.group(1).lower()
  if args:
    if args in CMD_HELP:
      await event.edit(str(CMD_HELP[args]))
    else:
      await event.edit("`Unknown module type !help to see all modules`")
  else:
    await event.edit(" Support Group for help & report bugs @simpleUserBot ")
    string = (f"`Use !help <module_name>`\n\n**Currently Loaded [{len(CMD_HELP)}] Modules **\n")
    for i in CMD_HELP:
      string += f" `{str(i)} `{str(i)}` `{str(i)}` "
      await event.reply(string)
