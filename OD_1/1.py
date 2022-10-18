import matplotlib.pyplot as plt

latin_probabilities ={'a':8.89,'b':1.58,'c':3.99,'d':2.77,'e':11.38,'f':0.93,'g':1.21,'h':0.69,'i':11.44,'j':0,'k':0.01,'l':3.15,'m':5.38,'n':6.28,'o':5.4,'p':3.03,'q':1.51,'r':6.67,'s':7.6,'t':8,'u':8.46,'v':0.96,'w':0,'x':0.6,'y':0.06,'z':0.01}
latin_letters = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
english_probabilities ={'a':8.4966,'b':2.0720,'c':4.5388,'d':3.3844,'e':11.1607,'f':1.8121,'g':2.4705,'h':3.0034,'i':7.5448,'j':0.1965,'k':1.1016,'l':5.4893,'m':3.0129,'n':6.6544,'o':7.1635,'p':3.1671,'q':0.1962,'r':7.5809,'s':5.7351,'t':6.9509,'u':3.6308,'v':1.0074,'w':1.2899,'x':0.2902,'y':1.779,'z':0.2722}
english_letters = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
polish_probabilities ={'a':9.16,'b':1.93,'c':4.49,'d':3.35,'e':9.81,'f':0.26,'g':1.46,'h':1.25,'i':8.83,'j':2.28,'k':3.01,'l':4.62,'m':2.28,'n':5.85,'o':8.32,'p':2.87,'q':0,'r':4.15,'s':4.85,'t':3.85,'u':2.06,'v':0,'w':4.11,'x':0,'y':4.03,'z':6.34}
polish_letters = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
def get_probabilities(text, letters):
    text = text.lower()
    letters_count = 0
    for i in text:
        if i in letters.keys():
            letters[i] = letters[i] + 1
            letters_count += 1
    for i in letters:
        letters[i] = letters[i]/letters_count*100
    return letters
def encrypt(file):
    table = str.maketrans("abcdefghijklmnopqrstuvwxyz", "nopqrstuvwxyzabcdefghijklm")
    file = open(file)
    text = file.read()
    output = ""
    for i in text:
        output += str.translate(i,table)
    return output

def get_shift(shited_probabilities, normal_probabilities, title):
    shited_probabilities_ordered = dict(sorted(shited_probabilities.items(), key=lambda item: item[1], reverse=True))
    normal_probabilities_ordered = dict(sorted(normal_probabilities.items(), key=lambda item: item[1], reverse=True))
    f, (p1,p2) = plt.subplots(1,2)
    p1.bar(*zip(*shited_probabilities.items()))
    p1.set_title("Shifted")
    p2.bar(*zip(*normal_probabilities.items()))
    p2.set_title("Normal")
    f.suptitle(title)
    plt.show()
    print(title+":")
    print(ord(list(shited_probabilities_ordered.keys())[0])-ord(list(normal_probabilities_ordered.keys())[0]))
get_shift(get_probabilities(encrypt('./latin.txt'),latin_letters), latin_probabilities, "Latin")
get_shift(get_probabilities(encrypt('./polish.txt'),polish_letters), polish_probabilities, "Polish")
get_shift(get_probabilities(encrypt('./english.txt'),english_letters), english_probabilities, "English")
