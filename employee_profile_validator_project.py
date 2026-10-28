employee_email = 'alice.johnson@company.com'
print(f'Email: {employee_email}') # Output: Email: alice.johnson@company.com

at_position = employee_email.find('@')
print(f'Position of @: {at_position}') # Output: Position of @: 13

username = employee_email[:at_position]
print(f'Username: {username}') # Output: Username: alice.johnson

has_at = '@' in employee_email
print(f'Has @ symbol: {has_at}') # Output: Has @ symbol: True

has_com = '.com' in employee_email
print(f'Has .com: {has_com}') # Output: Has .com: True