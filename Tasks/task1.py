import nltk
# nltk.download()

text = input("Enter some text: ")
choice = input("Please choose one of three choices :\n"
               "Choice number 1: print tokenized words\n"
               "Choice number 2: print tokenized sentences\n"
               "Choice number 3: print output using split function.\n"
               "Enter your choice (1, 2, or 3): ")

if choice == '1':
    # tokens = nltk.word_tokenize(text)
    print("Tokenized words:", nltk.word_tokenize(text))
elif choice == '2':
    sentences = nltk.sent_tokenize(text)
    print("Tokenized sentences:", sentences)
elif choice == '3':
    words = text.split()
    print("Output using split function:", words)
else:
    print("Invalid choice. Please enter 1, 2, or 3.")