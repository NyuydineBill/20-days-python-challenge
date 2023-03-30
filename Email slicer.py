def email_slicer():
    print('Welcome to email slicer app')
    print('')
    email_input = input('enter your email address : ')
    (username , domain) = email_input.split('@')
    (domain , extension) = domain.split('.')
    print('Username: '+ username)
    print('Domain: ' + domain)
    print('Extension: ' + extension)
email_slicer()

