class DocumentInfos:

    title = u'Chiffrement RSA'
    first_name = 'Loïs'
    last_name = 'Audemars'
    author = f'{first_name} {last_name}'
    year = u'2023'
    month = u'Février'
    seminary_title = u'Travail personnel OCI'
    tutor = u"Cédric Donner"
    release = "(Version intermédiaire)"
    repository_url = "https://github.com/LoisAudemars/travail-perso"

    @classmethod
    def date(cls):
        return cls.month + " " + cls.year

infos = DocumentInfos()