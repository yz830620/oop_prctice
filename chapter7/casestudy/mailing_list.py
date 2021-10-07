from collections import defaultdict
from mail_service import send_email


class MailingList:
    def __init__(self, data_file):
        self.data_file = data_file
        self.email_map = defaultdict(set)

    def add_to_group(self, email, group):
        self.email_map[email].add(group)

    def emails_in_groups(self, *groups):
        groups = set(groups)
        emails = set()
        for e, g in self.email_map.items():
            if g & groups:
                emails.add(e)
        return emails

    def send_mailing(self, subject, message, from_addr, *groups, headers=None):
        emails = self.emails_in_groups(*groups)
        send_email(subject, message, from_addr, *emails, headers=headers)
        
    def save(self):
        with open(self.data_file, 'w') as file:
            for email, groups in self.email_map.items():
                file.write(
                    f"{email} {','.join(groups)}\n"
                )

    def load(self):
        self.email_map = defaultdict(set)
        try:
            with open(self.data_file, 'r') as file:
                for line in file:
                    print(line.strip().split(' '))
                    email, groups = line.strip().split(' ')
                    groups = set(groups.split(','))
                    self.email_map[email] = groups
                    print(f'adding {email} to {groups}')
        except IOError:
            pass

    def __enter__(self):
        self.load()
        return self

    def __exit__(self, type, value, tb):
        self.save()

        
    


if __name__ == "__main__":
    with MailingList('addresses.db') as m:
        print('initialized')

        m.add_to_group("friend1@example.com", 'friends')
        m.add_to_group("friend2@example.com", 'friends')
        m.add_to_group("family@example.com", 'family')
        m.add_to_group('pro1@example.com', 'professional')

        m.send_mailing('A Party', 'Friends and family only: a party', 'me@example.com', 'friends', 'family', headers={"Reply-To": "me2@example.com"})
        print("done")