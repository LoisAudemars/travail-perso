class DocumentInfos:

    title = u'Le cryptosystème RSA'
    first_name = 'Loïs'
    last_name = 'Audemars'
    author = f'{first_name} {last_name}'
    year = u'2023'
    month = u'Avril'
    seminary_title = u'Travail personnel OCI'
    tutor = u"Cédric Donner"
    release = "(Version finale)"
    repository_url = "https://github.com/LoisAudemars/travail-perso"

    @classmethod
    def date(cls):
        return cls.month + " " + cls.year

infos = DocumentInfos()