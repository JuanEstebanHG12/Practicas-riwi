validation_string = lambda x : len(x) > 0

def validate_inputs(type_input, prompt, extra_validation = None):
    errors_messages = {
        int : "Enter a number greater than 0",
        float: "Enter a number greater than 0",
        str: "Do not enter empty text."
    }
    while True:
        try:
            validated_input = type_input(input(prompt))
            if extra_validation and not extra_validation(validated_input):
                print(f"\033[31m{errors_messages[type_input]}\033[0m")
                continue
            return validated_input
        except ValueError:
            print(ValueError)
