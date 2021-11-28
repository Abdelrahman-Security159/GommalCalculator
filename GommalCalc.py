class GommalCalculator():
    def __init__(self):
        self.input_value = ''
        self.sentance = ''
        self.output_value = 0

    def calculate(self, sentance, word_list):
        self.output_value = 0
        itr = 0
        try:
            while itr < len(sentance):
                if sentance[itr] == ' ':
                    pass
                else:
                    self.output_value += int(word_dict[sentance[itr]])
                itr += 1
        except Exception:
            return "Unknown"
        return self.output_value

    def show_help(self):
        sentance = """

        [!] Use online python interpreter for full profit.

        The Gommal is the numeric system in ancient arabic civilization.
        All what you need is write the arabic word to gain its gommal.
        example :
        When we calculate word "محمد""mohammed" we'll get 92
        So, when we write word "محمد""mohammed" we'll get its gommal
        For onfo :
        https://www.ihseb.net/%D8%AD%D9%8E%D8%A7%D8%B3%D9%90%D8%A8%D9%8E%D8%A9%D9%8F-%D8%A7%D9%84%D8%AC%D9%8F%D9%85%D9%8E%D9%84%D9%92/

        """
        return sentance

word_dict = {
    'ا':'1',
    'أ':'1',
    'إ':'1',
    'ب': '2',
    'ج': '3',
    'د': '4',
    'ه': '5',
    'ة':'5',
    'و': '6',
    'ز': '7',
    'ح': '8',
    'ط': '9',
    'ي': '10',
    'ى':'10',
    'ك': '20',
    'ل': '30',
    'م': '40',
    'ن': '50',
    'س': '60',
    'ع': '70',
    'ف': '80',
    'ص': '90',
    'ق': '100',
    'ر': '200',
    'ش': '300',
    'ت': '400',
    'ث': '500',
    'خ': '600',
    'ذ': '700',
    'ض': '800',
    'ظ': '900',
    'غ': '1000',
}
calculate = GommalCalculator()
while True:
    sentance = input("\n[!] Please Enter Your Arabic Sentance 'help for helping': ")
    if sentance == "help":
        print(calculate.show_help())
    else:
        print(f"[+] The Gommal of this sentance is : {calculate.calculate(sentance, word_dict)}")
