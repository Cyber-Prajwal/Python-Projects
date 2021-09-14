def process_message(msg):
    raw_msg = msg.lower()

    if raw_msg == 'hello':
        return 'Hi dude , my name is beetle the bot'
    elif raw_msg == 'how are you ??':
        return 'I am binary.....got it !!'
    elif 'ok' in raw_msg:
        return 'Nice to talk to you human you will surely not die....you will surely make a nice pet !!'
    else:
        return 'I did not understand what you wrote.'
