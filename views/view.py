#Mise en place des parametres de validation

class View:

    def get_user_entry(self, message_display, message_error, input_value, statement=None, default_value=None):
        while True:
            value = input(message_display)
            if input_value == "int":
                if value.isnumeric():
                    value = int(value)
                    return value
                else:
                    print(message_error)
                    continue
            if input_value == "sup_int":
                if value.isnumeric():
                    value = int(value)
                    if value >= default_value:
                        return value
                    else:
                        print(message_error)
                        continue
                else:
                    print(message_error)
                    continue
            if input_value == "str":
                try:
                    float(value)
                    print(message_error)
                    continue
                except ValueError:
                    return value
            elif input_value == "date":
                if self.verify_date(value):
                    return value
                else:
                    print(message_error)
                    continue
            elif input_value == "select":
                if value in statement:
                    return value
                else:
                    print(message_error)
                    continue

    @staticmethod
    def verify_date(value_to_test):
        if "-" not in value_to_test:
            return False
        else:
            splitted_date = value_to_test.split("-")
            for date in splitted_date:
                if not date.isnumeric():
                    return False
            return True

    @staticmethod
    def build_selection(iterable: list, display_msg: str, assertions: list) -> dict:
        display_msg = display_msg
        assertions = assertions

        for i, data in enumerate(iterable):
            display_msg = display_msg + f"{i+1} - {data['name']}\n"
            assertions.append(str(i + 1))

        return {
            "msg": display_msg,
            "assertions": assertions
            }
