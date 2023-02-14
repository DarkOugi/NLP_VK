import vk_api

# данные моего аккаунта являются базовыми, если пользователь опасается вводить данные на сайте
# или у объекта проверки открыта странница - вместо ввода своих данных, он может воспользоваться моей учетной записью
admin_auth = open('base_auth.txt').read().split()
base_login, base_password = admin_auth[2], admin_auth[-1]


class Api_Vk:
    def __init__(self, login=base_login, password=base_password):
        self.user = vk_api.VkApi(login, password)
        self.user.auth()
        self.user = self.user.get_api()

    def get_id(self, user_name):
        object_id = self.user.users.get(user_ids=user_name)[0]['id']
        return object_id

    def get_n_post(self, user_name, n=1):
        object_id = self.get_id(user_name)
        comments = self.user.wall.get(owner_id=object_id)['items']
        text = []
        size = 0
        for i in comments:
            if n == size:
                break
            else:
                if i['text'] != '':
                    text.append(i['text'])
                    size += 1
        return text


if __name__ == '__main__':
    print(Api_Vk().get_n_post('dimyasha',n=10))

