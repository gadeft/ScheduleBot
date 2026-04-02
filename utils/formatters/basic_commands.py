def start_command(full_name):
    return f"Hello, {full_name}! I am a schedule bot. Run any command you want and you will see what I can do."


def help_command():
    return (
        "<b>Basic commands:</b>\n" 
        "/start - starting the bot\n"
        "/help - the list of commands\n"
        "\n<b>Getting the schedule:</b>\n" 
        "/week - get the schedule for the week\n"
        "/today - get the schedule for today\n"
        "/tomorrow - get the schedule for tomorrow\n"
        "/yesterday - get the schedule for yesterday\n"
        "/specific_day - get the schedule for a specific day\n"
    )