import keyboard

def new_input(prompt):
    print(prompt + " : ", end ='', flush=True)
    user_input = []
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == 'space':
                break
            elif event.name == 'backspace':
                if user_input:
                    user_input.pop()
                    print('\b \b', end='', flush=True)
            else:
                user_input.append(event.name)
                print(event.name, end='', flush=True)
    return ''.join(user_input)


