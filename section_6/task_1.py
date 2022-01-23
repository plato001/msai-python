import random
from itertools import count
from datetime import datetime
from typing import List
from itertools import combinations, product
from nltk.corpus import names, brown, webtext


def load_usernames_from_nltk(n=10):
    all_names = names.words('male.txt') + names.words('female.txt')
    random.shuffle(all_names)
    return all_names[:n]


def load_chatnames_from_nltk(n=50):
    all_words = list(map(str, map(lambda x: x.lower(), brown.words())))
    random.shuffle(all_words)
    return all_words[:n]


def load_random_text():
    i = random.randint(0, 1720000)
    j = random.randint(100, 500)
    res = webtext.raw()[i:(i + j)]
    return res


def add_cls_attr(cls, attr_name, val):
    if getattr(cls, attr_name) is None:
        setattr(cls, attr_name, {val.id: val})
    else:
        attr_val = getattr(cls, attr_name)
        attr_val[val.id] = val
        setattr(cls, attr_name, attr_val)


class DirectMessage:
    id_iter = count()
    message_type = 'direct'

    def __init__(self, sender: 'User', recipient: 'User',
                 text: str, time=datetime.now().strftime('%d/%m/%Y %H:%M:%S')):
        self.id = f'dmid-{next(self.id_iter)}'
        self.sender = sender
        self.recipient = recipient
        self.text = text
        self.time = time

    def get_bag_of_words(self):
        return set(list(map(lambda x: x.lower(), self.text.split())))


class ChatMessage:
    id_iter = count()
    message_type = 'chat'

    def __init__(self, sender: 'User', chat: 'Chat',
                 text: str, time=datetime.now().strftime('%d/%m/%Y %H:%M:%S')):
        self.id = f'сmid-{next(self.id_iter)}'
        self.sender = sender
        self.chat = chat
        self.text = text
        self.time = time

    def get_bag_of_words(self):
        return set(self.text.split())


class User:
    id_iter = count()

    def __init__(self, username: str):
        self.id = f'uid-{next(self.id_iter)}'
        self.username = username
        self.contacts = None
        self.chats = None
        self.outgoing_direct_messages = None
        self.incoming_direct_messages = None
        self.chat_messages = None

    def add_contact(self, user: 'User'):
        add_cls_attr(self, 'contacts', user)

    def add_chat(self, chat: 'Chat'):
        add_cls_attr(self, 'chats', chat)

    def _add_direct_message(self, message: 'DirectMessage'):
        if self.id == message.sender.id:
            add_cls_attr(self, 'outgoing_direct_messages', message)
        else:
            add_cls_attr(self, 'incoming_direct_messages', message)

    def _add_chat_message(self, message: 'DirectMessage'):
        add_cls_attr(self, 'chat_messages', message)

    def add_message(self, mtype: str, message: 'DirectMessage'):
        if mtype == 'direct':
            self._add_direct_message(message)
        else:
            self._add_chat_message(message)

    def __repr__(self):
        return f'User({self.username})'


class Chat:
    id_iter = count()

    def __init__(self, chatname: str):
        self.id = f'cid-{next(self.id_iter)}'
        self.chatname = chatname
        self.users = None
        self.messages = None

    def _add_user(self, user: 'User'):
        add_cls_attr(self, 'users', user)

    def add_users(self, *users):
        for user in users:
            self._add_user(user)

    def add_message(self, message: 'ChatMessage'):
        add_cls_attr(self, 'messages', message)

    def __repr__(self):
        return f'Chat({self.chatname})'


class Messenger:
    def __init__(self):
        # users
        self.users = None
        # chats
        self.chats = None
        # messages
        self.messages = None

    def create_user_account(self, username: str):
        user = User(username)
        add_cls_attr(self, 'users', user)

    def create_chat(self, chatname: str):
        chat = Chat(chatname)
        add_cls_attr(self, 'chats', chat)

    def add_messages(self, message):
        add_cls_attr(self, 'messages', message)

    def find_msg_with_word_comb(self, words: List[str]):
        res = []
        for msg in self.messages.values():
            set_words = set(list(map(lambda x: x.lower(), words)))
            set_txt = msg.get_bag_of_words()
            if set_words.issubset(set_txt):
                if msg.message_type == "direct":
                    info = {
                        "message_type": "direct",
                        "sender": msg.sender,
                        "recipient": msg.recipient,
                        "text": msg.text
                    }
                else:
                    info = {
                        "message_type": "chat",
                        "sender": msg.sender,
                        "chat": msg.chat,
                        "text": msg.text
                    }
                res.append(info)
        return res

    def find_shared_chats(self, users_lst: List[str]):
        # create User objects
        users = []
        for uname in users_lst:
            for usr in self.users.values():
                if usr.username == uname:
                    users.append(usr)
                    break
        return set.intersection(*list(map(lambda x: {*x.chats}, users)))


if __name__ == '__main__':
    # random
    random.seed(1001)
    # Messenger
    m = Messenger()
    # create users
    username_lst = load_usernames_from_nltk()
    for u in username_lst:
        m.create_user_account(username=u)
    messenger_users = m.users.values()
    # create chats
    chatname_lst = load_chatnames_from_nltk()
    for c in chatname_lst:
        m.create_chat(chatname=c)
    messenger_chats = m.chats.values()
    # 1. Add users to a chat
    print('1. Add users to a chat')
    for m_chat in messenger_chats:
        # sample of users
        sample = random.sample(list(messenger_users), 5)
        m_chat.add_users(*sample)
        for u in sample:
            u.add_chat(m_chat)
    print('Chat name: ', m.chats['cid-0'].chatname)
    print('Users in chat: ', m.chats['cid-0'].users)
    print('***********************************************')
    # add messages
    # direct messages
    users_pairs = list(combinations(list(messenger_users), 2))[:500]
    for u1, u2 in users_pairs:
        # create message
        txt = load_random_text()
        dmsg = DirectMessage(u1, u2, text=txt)
        # add to users info
        u1.add_message(mtype='direct', message=dmsg)
        u2.add_message(mtype='direct', message=dmsg)
        # add message to Messenger
        m.add_messages(dmsg)
    # chat messages
    user_chat_pairs = list(
        random.sample(
            list(product(list(messenger_users), list(messenger_chats))),
            500
        )
    )
    for u, c in user_chat_pairs:
        # create message
        txt = load_random_text()
        cmsg = ChatMessage(u, c, text=txt)
        # add to user info
        u.add_message(mtype='chat', message=cmsg)
        # add to chat info
        c.add_message(cmsg)
        # add to Messenger
        m.add_messages(cmsg)
    # 2. Find messages with some word combination
    print('2. Find messages with some word combination')
    target_words_comb = [
        ['Hi', 'mister', 'you'],
        ['work', 'love'],
        ['who', 'is'],
        ['python', 'class']
    ]
    for w in target_words_comb:
        print('Words: ', ','.join(w))
        print('Messages:')
        for el in m.find_msg_with_word_comb(w):
            print(el)
        print('--------------------')
    print('***********************************************')
    # 3. Display shared chats of several users
    print('3. Display shared chats of several users')
    users_1 = ['Meryl', 'Mirella', 'Bentley']
    users_2 = ['Bentley', 'Kirstie', 'Gipsy', 'Marjory']
    users_3 = ['Jilli', 'Colene']
    for el in [users_1, users_2, users_3]:
        print("Users: ", ','.join(el))
        print("Shared chats: ", m.find_shared_chats(el))
        print('--------------------')
    print('***********************************************')
