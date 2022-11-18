#Write a Python program to print a long text, convert the string to a list and print all the words and their frequencies
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam urna elit, facilisis et erat vel, euismod eleifend diam. " \
       "Quisque arcu nisi, consequat sit amet sapien sit amet, tristique blandit eros. Maecenas interdum nunc sed consequat tempus. " \
       "Suspendisse pellentesque vulputate orci a elementum. Donec efficitur est turpis, id efficitur erat ullamcorper eget. " \
       "Donec sit amet laoreet est. Cras ut tellus pulvinar purus tincidunt tincidunt. " \
       "Aenean ut nisi turpis. Quisque laoreet metus et augue tincidunt, ac semper leo maximus. " \
       "Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam vitae mattis leo. " \
       "Vestibulum quis posuere nisi, vel posuere neque. " \
       "Ut nec mollis augue. Nam pharetra mi et leo ultricies scelerisque. " \
       "Donec elit augue, ullamcorper ac ultrices non, mollis et lectus. Nunc placerat ornare diam, sit amet vestibulum ex ornare quis."

#1
text_l = text.split()
counter = {}
for i in text_l:
    if i not in counter:
        counter[i] = 0
    if i in counter:
        counter[i] += 1
print(counter)


