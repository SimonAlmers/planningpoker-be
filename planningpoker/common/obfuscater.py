import random
import string


class Obfuscater:

    FIRST_NAMES = [
        "John",
        "Michael",
        "Robert",
        "David",
        "James",
        "Mary",
        "William",
        "Richard",
        "Thomas",
        "Linda",
        "Mark",
        "Charles",
        "Joseph",
        "Patricia",
        "Barbara",
        "Jennifer",
        "Paul",
        "Maria",
        "Susan",
        "Daniel",
    ]

    LAST_NAMES = [
        "Smith",
        "Johnson",
        "Williams",
        "Brown",
        "Jones",
        "Davis",
        "Miller",
        "Anderson",
        "Wilson",
        "Garcia",
        "Taylor",
        "Thomas",
        "Moore",
        "Rodriguez",
        "Lee",
        "Jackson",
        "Martin",
        "White",
        "Martinez",
        "Thompson",
    ]

    CORPORATE_BUZZWORDS = [
        "Return on investment",
        "Synergy",
        "Customer journey",
        "Deep dive",
        "Impact",
        "Disruptive",
        "Startup",
        "Sustainability",
        "Pain point",
        "Quick win",
        "Next generation",
        "Holistic",
        "Logistics",
        "Alignment",
        "Freemium",
        "Quota",
        "Touchpoint",
        "Retargeting",
        "Content is king",
        "Big data",
        "Incentivize",
        "Move the needle",
        "Ecosystem",
    ]

    @classmethod
    def string(cls, length=24):
        characters = string.ascii_lowercase + string.digits + string.ascii_uppercase
        return "".join(random.choice(characters) for i in range(length))

    @classmethod
    def first_name(cls):
        return random.choice(cls.FIRST_NAMES)

    @classmethod
    def last_name(cls):
        return random.choice(cls.LAST_NAMES)

    @classmethod
    def email(cls, _first_name=None, _last_name=None, _domain=None):
        first_name = _first_name or cls.first_name()
        last_name = _last_name or cls.last_name()
        domain = _domain or "testuser.com"
        return f"{first_name}.{last_name}-{cls.string(5)}@{domain}"

    @classmethod
    def project_title(cls):
        return f"{random.choice(cls.CORPORATE_BUZZWORDS)} Project"