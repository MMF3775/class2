
class BaseValidation:

    def __init__(self):
        pass

    def length(self, text, length):
        return True if len(text) <= length else False

    def is_valid_email(self,email: str) -> bool:
        if len(email) < 5 or '@' not in email or '.' not in email:
            return False
        split_email = email.split('@')
        if len(split_email) != 2:
            return False
        else:
            if '.' not in split_email[1]:
                return False
            return True

    def card_id_validation(self,number) -> bool:
            card_number = number.strip()
            error_list = []

            if not card_number.isdigit():

                error_list.append("your card number is not digit")
            elif len(card_number) != 16:

                error_list.append("your card number length is not 16 digits")
            else:
                s = 0
                for i in range(len(card_number)):
                    if (i + 1) % 2 == 0:
                        result = int(card_number[i]) * 1
                    else:
                        if (int(card_number[i]) * 2) > 9:
                            result = (int(card_number[i]) * 2) - 9
                        else:
                            result = int(card_number[i]) * 2
                    s += result
                if s % 10 != 0:
                    error_list.append("Card number is not valid")
            print(error_list)
            return False if len(error_list) > 0 else True

    def idenntity_code(self,idcode):
        idcode = list(idcode)
        b = 0

        if len(idcode) == 10:
            control_num = int(idcode.pop())
            for i, value in enumerate(idcode):
                a = int(idcode[i]) * (10 - i)
                b = a + b

            c = b % 11

            if (c < 2) and (control_num == c) or ((c >= 2) and ((11 - c) == control_num)):
                return True

            else:
                return False
        else:
            return False
