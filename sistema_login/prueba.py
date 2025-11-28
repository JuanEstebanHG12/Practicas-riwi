from validations import validate_inputs, validation_names, validation_number

n = validate_inputs(float, "number: ", validation_number)
print(n)