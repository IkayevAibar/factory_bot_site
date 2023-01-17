# Factory_bot + site
Привет, попытаюсь кратко и ясно всё обьяснить.

## Этапы юзер флоу

0. **Регистрация** -> POST http://factory-bot-site.herokuapp.com/auth/users/  with body  {username, password, first_name}
1. **Авторизация** -> POST https://factory-bot-site.herokuapp.com/api/token/ with body  {username, password}  Этот token для авторизаций JWT
2. **Заходим в бота в тг** @the_factory_task_bot
3. **Пишем /generate_token**  :black_square_button: Возможно из за heroku придётся пару раз попытаться
    1. Пишем логин
    2. Пишем пароль
    3. Видем результат
    4. И если всё окей, то теперь мы можем отправлять сообщение через сайт
4. **Получаем свой token в**  -> https://factory-bot-site.herokuapp.com/api-token-auth/  with body  {username, password}  Remark///Этот token для 5 пункта
5. **Находим айди бота в**  -> POST https://factory-bot-site.herokuapp.com/api/bots/get_bots_id_by_token/   with body  {token}
6. **Теперь мы можем отправить сообщение через API в чат** -> POST https://factory-bot-site.herokuapp.com/send_message_to_chat/ with body  {bot(айди бота), user(айди юзера), message_body}
7. **Вы должны будете получить сообщение**
8. **Получаем все сообщения** -> POST https://factory-bot-site.herokuapp.com/get_all_messages/ with body  {bot(айди бота), user(айди юзера)

____
- [X] ссылка на реп бота https://github.com/IkayevAibar/factory_bot

- [X] Это весь функционал вроде, есть еще лист юзеров, ботов и всё такое, ну это всё лишнее,

- [X] Все эти эндпоинты есть в файле для постмана factory.postman_collection.json(https://github.com/IkayevAibar/factory_bot_site/blob/master/factory.postman_collection.json)

- [ ] Не тестил 4 и 5 пункт пока что

____
# Спасибо за внимание!
