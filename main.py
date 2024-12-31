import requests
import telebot,time
import time
from telebot import types
from gate import Tele
import os
token = '7902782706:AAE-IS88ujC2w8zb8CT0LAs25joNPFUw8mI' #bottoken
bot=telebot.TeleBot(token,parse_mode="HTML")
subscriber = '6318673920'
allowed_users = ['6318673920']  #Your ID
@bot.message_handler(commands=["start"])
def start(message):
    if str(message.chat.id) not in allowed_users:
        bot.reply_to(message, "ðŸš« ð˜ð¨ð® ðœðšð§ð§ð¨ð­ ð®ð¬ðž ð­ð¡ðž ð›ð¨ð­ ð­ð¨ ðœð¨ð§ð­ðšðœð­ ððžð¯ðžð¥ð¨ð©ðžð«ð¬ ð­ð¨ ð©ð®ð«ðœð¡ðšð¬ðž ðš ð›ð¨ð­ ð¬ð®ð›ð¬ðœð«ð¢ð©ð­ð¢ð¨ð§ @Awmteapolythene")
        return
    bot.reply_to(message, "ð’ðžð§ð ð­ð¡ðž ð­ð±ð­ ðŸð¢ð¥ðž ð§ð¨ð°")
@bot.message_handler(commands=["chk"])
def add_user(message):
    if str(message.chat.id) == '6318673920':  # Only bot owner can add new users
        try:
            new_user_id = message.text.split()[1]  # Extract new user ID from the command
            allowed_users.append(new_user_id)
            bot.reply_to(message, f"User ID {new_user_id} Has Been Added Successfully.âœ…\nCongratulations! Premium New UserðŸŽ‰âœ… ")
        except IndexError:
            bot.reply_to(message, "Please provide a valid user ID. Example: /add 123456789")
    else:
        bot.reply_to(message, "You do not have permission to add users.ðŸš«")
@bot.message_handler(content_types=["document"])
def main(message):
	if str(message.chat.id) not in allowed_users:
		bot.reply_to(message, "ðŸš« ð˜ð¨ð® ðœðšð§ð§ð¨ð­ ð®ð¬ðž ð­ð¡ðž ð›ð¨ð­ ð­ð¨ ðœð¨ð§ð­ðšðœð­ ððžð¯ðžð¥ð¨ð©ðžð«ð¬ ð­ð¨ ð©ð®ð«ðœð¡ðšð¬ðž ðš ð›ð¨ð­ ð¬ð®ð›ð¬ðœð«ð¢ð©ð­ð¢ð¨ð§ @Ownerxxxxx")
		return
	dd = 0
	live = 0
	incorrect = 0
	ch = 0
	ko = (bot.reply_to(message, "ðð«ð¨ðœðžð¬ð¬ð¢ð§ð  ð‚ðšð«ð ð‚ð¡ðžðœð¤ð¢ð§ð  ...âŒ›").message_id)
	ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
	with open("combo.txt", "wb") as w:
		w.write(ee)
	try:
		with open("combo.txt", 'r') as file:
			lino = file.readlines()
			total = len(lino)
			for cc in lino:
				current_dir = os.getcwd()
				for filename in os.listdir(current_dir):
					if filename.endswith(".stop"):
						bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='ð—¦ð—§ð—¢ð—£ð—£ð—˜ð—— âœ…\nð—•ð—¢ð—§ ð—•ð—¬ âžœ @Awmteapolythene')
						os.remove('stop.stop')
						return
				try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
				except: pass
				try:
					brand = data['brand']
				except:
					brand = 'Unknown'
				try:
					card_type = data['type']
				except:
					card_type = 'Unknown'
				try:
					country = data['country_name']
					country_flag = data['country_flag']
				except:
					country = 'Unknown'
					country_flag = 'Unknown'
				try:
					bank = data['bank']
				except:
					bank = 'Unknown'
				
				start_time = time.time()
				try:
					last = str(Tele(cc))
				except Exception as e:
					print(e)
					last = "Error"
				if 'Stripe Error: Your card was declined.' in last:
					last='Your Card Was Declined'
				elif 'Declined - Call Issuer' in last:
					last='Declined - Call Issuer'
				mes = types.InlineKeyboardMarkup(row_width=1)
				cm1 = types.InlineKeyboardButton(f"â€¢ {cc} â€¢", callback_data='u8')
				status = types.InlineKeyboardButton(f"â€¢ ð’ð“ð€ð“ð”ð’  : {last} ", callback_data='u8')
				cm3 = types.InlineKeyboardButton(f"â€¢ ð€ððð‘ðŽð•ð„ðƒ âœ… : [ {live} ] â€¢", callback_data='x')
				cm4 = types.InlineKeyboardButton(f"â€¢ ð…ð€ðŠð„ ð‚ð€ð‘ðƒ âš ï¸ : [ {incorrect} ] â€¢", callback_data='x')
				cm5 = types.InlineKeyboardButton(f"â€¢ ðƒð„ð‚ð‹ðˆðð„ðƒ âŒ : [ {dd} ] â€¢", callback_data='x')
				cm6 = types.InlineKeyboardButton(f"â€¢ ð“ðŽð“ð€ð‹ ðŸŽ‰       :  [ {total} ] â€¢", callback_data='x')
				stop=types.InlineKeyboardButton(f"[ ð’ð“ðŽð ðŸš« ]", callback_data='stop')
				mes.add(cm1,status, cm3, cm4, cm5, cm6, stop)
				end_time = time.time()
				execution_time = end_time - start_time
				bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''ð–ðšð¢ð­ ðŸð¨ð« ð©ð«ð¨ðœðžð¬ð¬ð¢ð§ð  
ðð² âžœ <a href='t.me/Approved_Raven'>ã€Žá¯×h××…Ö®êª±××…t××…êª€××…á§×ê«€××…Ü» ã€ã€ð‚ð‡ã€‘á¶œâ¿êªœ ðŸ’¤</a> ''', reply_markup=mes)
				msg = f'''
<a href='t.me/Approved_Raven'>-</a> ð€ð©ð©ð«ð¨ð¯ðžð âœ…
<a href='t.me/Approved_Raven'>â”â”â”â”â”â”â”â”â”â”â”â”âŸ</a>			
<a href='t.me/Approved_Raven'>â”ƒ</a>ð‚ð‚ <code>{cc}</code><a href='t.me/Approved_Raven'>â”—â”â”â”â”â”â”â”âŠ›</a>
<a href='t.me/Approved_Raven'>-</a> ð†ðšð­ðžð°ðšð²: <code>Stripe Charge 5$</code>		
<a href='t.me/Approved_Raven'>-</a> ð‘ðžð¬ð©ð¨ð§ð¬ðž: <code>Payment Successful ðŸŽ‰</code>

<a href='t.me/Approved_Raven'>-</a> ðˆð§ðŸð¨: <code>{cc[:6]}-{card_type} - {brand}</code>
<a href='t.me/Approved_Raven'>-</a> ð‚ð¨ð®ð§ð­ð«ð²: <code>{country} - {country_flag}</code>
<a href='t.me/Approved_Raven'>-</a> ððšð§ð¤: <code>{bank}</code>

<a href='t.me/Approved_Raven'>-</a> ð“ð¢ð¦ðž: <code>1{"{:.1f}".format(execution_time)} ð¬ðžðœð¨ð§ð</code> 
<a href='t.me/Approved_Raven'>-</a> ðð¨ð­ ð€ð›ð¨ð®ð­: <a href='t.me/Approved_Raven'>â¤ÍŸÍžð‘®ð‘ºð‘°ð‘¿ ð“†© ð‘ªð‘¯ð‘² ð“†ªêª¾á¶œâ¿êªœ</a>'''
				print(last)
				if 'success' in last or 'Processor Declined - Fraud Suspected' in last or 'Declined - Call Issuer' in last or 'Stripe Error: Your card does not support this type of purchase.' in last or "Stripe Error: Your card's security code is invalid." in last:
					live += 1
					bot.reply_to(message, msg)
				elif 'Card Not Activated' in last:
					incorrect+=1
				elif 'security code is incorrect.' in last:
					msg = f'''
<a href='t.me/Approved_Raven'>-</a> ð€ð©ð©ð«ð¨ð¯ðžð âœ… 
<a href='t.me/Approved_Raven'>â”â”â”â”â”â”â”â”â”â”â”â”âŸ</a>			
<a href='t.me/Approved_Raven'>â”ƒ</a>ð‚ð‚ <code>{cc}</code><a href='t.me/Approved_Raven'>â”—â”â”â”â”â”â”â”âŠ›</a>
<a href='t.me/Approved_Raven'>-</a> ð†ðšð­ðžð°ðšð²: <code>Stripe Charge 5$</code>		
<a href='t.me/Approved_Raven'>-</a> ð‘ðžð¬ð©ð¨ð§ð¬ðž: <code>AUTH Completed ðŸŸ¢</code>

<a href='t.me/Approved_Raven'>-</a> ðˆð§ðŸð¨: <code>{cc[:6]}-{card_type} - {brand}</code>
<a href='t.me/Approved_Raven'>-</a> ð‚ð¨ð®ð§ð­ð«ð²: <code>{country} - {country_flag}</code>
<a href='t.me/Approved_Raven'>-</a> ððšð§ð¤: <code>{bank}</code>

<a href='t.me/Approved_Raven'>-</a> ð“ð¢ð¦ðž: <code>1{"{:.1f}".format(execution_time)} ð¬ðžðœð¨ð§ð </code>
<a href='t.me/Approved_Raven'>-</a> ðð¨ð­ ð€ð›ð¨ð®ð­: <a href='t.me/Approved_Raven'>â¤ÍŸÍžð‘®ð‘ºð‘°ð‘¿ ð“†© ð‘ªð‘¯ð‘² ð“†ªêª¾á¶œâ¿êªœ</a>'''
					live += 1
					bot.reply_to(message, msg)
				elif 'Card Not Activated' in last:
					incorrect+=1
				elif 'security code is incorrect.' in last or 'Stripe Error: Your card has insufficient funds.' in last or 'tree_d' in last:
					msg = f'''
<a href='t.me/Approved_Raven'>-</a> ð€ð©ð©ð«ð¨ð¯ðžð âœ…!!
<a href='t.me/Approved_Raven'>â”â”â”â”â”â”â”â”â”â”â”â”âŸ</a>			
<a href='t.me/Approved_Raven'>â”ƒ</a>ð‚ð‚ <code>{cc}</code><a href='t.me/Approved_Raven'>â”—â”â”â”â”â”â”â”âŠ›</a>
<a href='t.me/Approved_Raven'>-</a> ð†ðšð­ðžð°ðšð²: <code>Stripe Charge 5$</code>		
<a href='t.me/Approved_Raven'>-</a> ð‘ðžð¬ð©ð¨ð§ð¬ðž: <code>Insufficient Funds âŽ</code>

<a href='t.me/Approved_Raven'>-</a> ðˆð§ðŸð¨: <code>{cc[:6]}-{card_type} - {brand}</code>
<a href='t.me/Approved_Raven'>-</a> ð‚ð¨ð®ð§ð­ð«ð²: <code>{country} - {country_flag}</code>
<a href='t.me/Approved_Raven'>-</a> ððšð§ð¤: <code>{bank}</code>

<a href='t.me/Approved_Raven'>-</a> ð“ð¢ð¦ðž: <code>2{"{:.1f}".format(execution_time)} ð¬ðžðœð¨ð§ð </code>
<a href='t.me/Approved_Raven'>-</a> ðð¨ð­ ð€ð›ð¨ð®ð­: <a href='t.me/Approved_Raven'>â¤ÍŸÍžð‘®ð‘ºð‘°ð‘¿ ð“†© ð‘ªð‘¯ð‘² ð“†ªêª¾á¶œâ¿êªœ</a>'''
					live += 1
					bot.reply_to(message, msg)
				elif 'Card Not Activated' in last:
					incorrect+=1
				else:
					dd += 1
					time.sleep(10)
	except Exception as e:
		print(e)
	bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='ð—•ð—˜ð—˜ð—¡ ð—–ð—¢ð— ð—£ð—Ÿð—˜ð—§ð—˜ð—— âœ…\nð—•ð—¢ð—§ ð—•ð—¬ âžœ @Ownerxxxxx')
@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
	with open("stop.stop", "w") as file:
		pass
logop = f'''â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”
'''
print(logop)
bot.polling()
