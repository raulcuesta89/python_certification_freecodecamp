employee_email = 'alice.johnson@company.com'

print(f'Email: {employee_email}')

at_position = employee_email.find('@')

print(f'Position of @: {at_position}')

username = employee_email[:at_position]

print(f'Username: {username}')