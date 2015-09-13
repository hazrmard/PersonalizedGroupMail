
import PersonalizedGroupMail as PGM

testClass = PGM.PersonalizedGroupMail('Test Group Email', 'me@me.me')
testClass.get_message_from_html('htmlEmailSample.html')
testClass.get_names_from_csv('testData.csv', 2)
testClass.get_salutations_from_csv('testData.csv', 1)
testClass.get_recipients_from_csv('testData.csv', 4)
testClass.get_personalized_messages_from_csv('testData.csv', 3)
testClass.common_salutation = 'I hope you are well.'
testClass.randomize_salutations()
# These functions work with valid connection/recipient data
# testClass.set_connection('host.host.com', 42)
# testClass.authenticate('mename', 'mepassword')
# testClass.send()


print 'Salutations'
print testClass.salutations
print 'Names'
print testClass.names
print 'Emails'
print testClass.recipients
print 'Personal Messages'
print testClass.personalmsgs

testClass.randomize_personalized_messages()
testClass.randomize_salutations()
print 'Randomized Salutations'
print testClass.salutations
print 'Randomized PMs'
print testClass.personalmsgs


