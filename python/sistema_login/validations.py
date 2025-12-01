validation_string = lambda x : len(x) > 0
validation_names = lambda x : len(x) > 0 and x.isalpha()
validation_number = lambda x: x>0

def validate_inputs(type_input, prompt, extra_validation = None):
    errors_messages = {
        validation_number: "Enter a number greater than 0",
        validation_string: "Do not enter empty text.",
        validation_names: "Enter a valid name, without numbers"
    }
    while True:
        try:
            validated_input = type_input(input(prompt))
            if extra_validation and not extra_validation(validated_input):
                print(f"\033[31m{errors_messages[extra_validation]}\033[0m")
                continue
            return validated_input
        except ValueError:
            print(f"\033[31m{errors_messages[extra_validation]}\033[0m")
