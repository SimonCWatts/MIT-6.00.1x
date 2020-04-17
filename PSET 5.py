import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object

        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class

        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.

        shift (integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''
        # create a list of all letters in the alphabet
        alphabet = string.ascii_letters
        # create a dictionary where each key and each value are corresponding letters of the alphabet
        shiftDict = dict(zip(alphabet, alphabet))

        # adjust the values of the dictionary by the shift value
        for k, v in shiftDict.items():
            if shiftDict[k] in string.ascii_lowercase:
                shiftDict[k] = chr ( ( (ord(shiftDict[v]) + shift - ord('a') ) % 26 ) + ord('a') )
            elif shiftDict[k] in string.ascii_uppercase:
                shiftDict[k] = chr ( ( (ord(shiftDict[v]) + shift - ord('A') ) % 26 ) + ord('A') )

        return shiftDict


    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        plainText = self.message_text[:]
        shiftDict = self.build_shift_dict(shift)
        cipherText = ''

        for char in plainText:
             if char in string.ascii_letters:
                 cipherText += shiftDict[char]
             else:
                 cipherText += char

        return cipherText


class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object

        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less
        code is repeated
        '''
        Message.__init__(self, text)
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class

        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class

        Returns: a COPY of self.encrypting_dict
        '''
        return dict(self.encrypting_dict)

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class

        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other
        attributes determined by shift (ie. self.encrypting_dict and
        message_text_encrypted).

        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        # reassignement within the plaintext class
        self.shift = shift
        # updating the other attributes by re-initialising
        PlaintextMessage.__init__(self, Message.get_message_text(self), shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object

        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - gets to be the best shift value
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        cipher_text = Message.get_message_text(self)
        # create a list of ciphertext words to interate over when decoding...
        list_of_ciphertext = cipher_text.split(' ')
        # a placeholder for where to store the final decoded message
        ans = ''
        # a dictionary to store the accuracy score for each shift value
        score = {}

        # shift can take any value: 1 <= shift <= 26
        for shift in range(1, 27):
            # create a file in the dictionary
            score[shift] = 0
            # decode the message
            plain_text = Message.apply_shift(self, 26 - shift)
            # turn the plain text message into a list of words
            list_of_plaintext = plain_text.split(' ')
            # for word in list_of_plaintext:
            for plain_word in list_of_plaintext:
                # if the decoded word is a real word then add one score to the dictionary
                if plain_word in self.valid_words:
                    score[shift] += 1

        # find the shift the produces the highest number of valid words
        bestShift = max(score, key=lambda i: score[i])
        # build a decode dictionary
        decodeDict = Message.build_shift_dict(self, 26 - bestShift)
        # decode the ciphertext using the best shift one character at a time
        for char in cipher_text:
            if char in string.ascii_letters:
                ans += decodeDict[char]
            else:
                ans += char

        return 26 - bestShift, ans



#Example test case (PlaintextMessage)
plaintext = PlaintextMessage('hello', 2)
print('Expected Output: jgnnq')
print('Actual Output:', plaintext.get_message_text_encrypted())

#Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('jgnnq ocp')
print('Expected Output:', (24, 'hello man'))
print('Actual Output:', ciphertext.decrypt_message())
