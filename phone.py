# Submit a link to a GitHub Repo, with a file called phone.py, that includes the iPhone class.

# 1. Create 2 instances of the iPhone.

# 2. Change iPhone names through set_name()

# 3. Send a iMessage from phone1 to phone2

# 4. phone2 should be able to check messages. Print the messages on screen.



class iPhone:
    def __init__(self, name, phone_number, color, model): #constructor
        self.name = name
        # self.ios_version = version
        self.phone_number = phone_number
        self.color = color
        self.model = model
        self.files = []
        self.messages = []

    #set a new name for iphone
    def set_name(self, new_name):
        self.name = new_name


    #add a mssage to current iphone
    def send_to_me_message(self, message):
        self.messages = message
        print(f'Sending message to {self.name} (myself): {self.messages}')


    # send a message
    # self.message = 


    def send_messages(self, other_phone, message):
        other_phone.messages = message
        print(f'Sending message to {self.name}: {self.messages}')

    # check message
    def check_messages(self):
        print(f'Messages in {self.name} is\n: {self.messages}')

# Create 2 instances of the iPhone
chang_iphone = iPhone(
        name = "Chang's iphone", 
        # ios_version = "17,2", 
        phone_number = "1234-567-890",
        color = "white",
        model = "iPhone 14 Pro",
    )

william_iphone = iPhone(
        name = "iPhone 15", 
        # ios_version = "17.1", 
        phone_number = "0987-654-321",
        color = "blue",
        model = "iPhone 16",
    )

print(chang_iphone.name)


# Change iPhone names through set_name()
chang_iphone.set_name("Chang's iphone 14")
william_iphone.set_name("William's iphone")


# Senda iMessage from phone1 (Chang's) to phone2 (William's)
chang_iphone.send_messages(william_iphone, "Hey William - how are you doing today?")

# Senda iMessage from phone2 (Chang's) to phone1 (William's)
william_iphone.send_messages(chang_iphone, "Not bad, hbu")

# Phone 2 (William's phone) checks the messages
william_iphone.check_messages()
chang_iphone.check_messages()

# just sending a messag to myself
chang_iphone.send_to_me_message("adding something here")
print("\n\n")
chang_iphone.check_messages()

