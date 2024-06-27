def send_email(message, recipient, sender="university.help@gmail.com"):

    for i in recipient:
        if i.endswith('.com') or i.endswith('.ru') or i.endswith('.net') and '@' in i:
                print(f'{'Письмо успешно отправлено с адреса'}, {sender},  {'на адрес'}, {recipient}')
        else:
            print(f'{'Невозможно отправить письмо с адреса'}, {sender}, {'на адрес'}, {recipient}')
            return i


        for j in sender:
            if j.endswith('.com') or j.endswith('.ru') or j.endswith('.net') and '@' in j:
                print(f'{'Письмо успешно отправлено с адреса'}, {sender},  {'на адрес'}, {recipient}')
            else:
                print(f'{'Невозможно отправить письмо с адреса'}, {sender}, {'на адрес'}, {recipient}')
                return j


    # if recipient == sender:
    #     print(f'{'Нельзя отправить письмо самому себе!'}')
    # if sender == 'university.help@gmail.com':
         #print(f'{'Письмо успешно отправлено с адреса'}, {sender},  {'на адрес'}, {recipient}')
    # else:
    #     print(f'{'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса'}, {sender}, {'на адрес'}, {recipient}')



send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
#send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
#send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
#send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')