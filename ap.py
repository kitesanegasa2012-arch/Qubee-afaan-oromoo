from flask import Flask, render_template

app = Flask(__name__)

# Data Qubee Afaan Oromoo guutuu
QUBEE_DATA = [
    # Dubbachiiftuu (Vowels)
    {"qubee": "A a", "fakkeenya": "Adaadaa", "hiika": "Aunt", "gosa": "Dubbachiiftuu"},
    {"qubee": "E e", "fakkeenya": "Eeboo", "hiika": "Spear", "gosa": "Dubbachiiftuu"},
    {"qubee": "I i", "fakkeenya": "Ija", "hiika": "Eye", "gosa": "Dubbachiiftuu"},
    {"qubee": "O o", "fakkeenya": "Obboleessa", "hiika": "Brother", "gosa": "Dubbachiiftuu"},
    {"qubee": "U u", "fakkeenya": "Ummata", "hiika": "People", "gosa": "Dubbachiiftuu"},

    # Dubbifamaa (Consonants)
    {"qubee": "B b", "fakkeenya": "Bara", "hiika": "Year", "gosa": "Dubbifamaa"},
    {"qubee": "C c", "fakkeenya": "Caama", "hiika": "Sunshine", "gosa": "Dubbifamaa"},
    {"qubee": "D d", "fakkeenya": "Dachee", "hiika": "Earth", "gosa": "Dubbifamaa"},
    {"qubee": "F f", "fakkeenya": "Farda", "hiika": "Horse", "gosa": "Dubbifamaa"},
    {"qubee": "G g", "fakkeenya": "Gaala", "hiika": "Camel", "gosa": "Dubbifamaa"},
    {"qubee": "H h", "fakkeenya": "Harma", "hiika": "Breast", "gosa": "Dubbifamaa"},
    {"qubee": "J j", "fakkeenya": "Jirbii", "hiika": "Cotton", "gosa": "Dubbifamaa"},
    {"qubee": "K k", "fakkeenya": "Kallattii", "hiika": "Direction", "gosa": "Dubbifamaa"},
    {"qubee": "L l", "fakkeenya": "Laga", "hiika": "River", "gosa": "Dubbifamaa"},
    {"qubee": "M m", "fakkeenya": "Mana", "hiika": "House", "gosa": "Dubbifamaa"},
    {"qubee": "N n", "fakkeenya": "Namticha", "hiika": "Man", "gosa": "Dubbifamaa"},
    {"qubee": "P p", "fakkeenya": "Phaappasiyaa", "hiika": "Papaya", "gosa": "Dubbifamaa"},
    {"qubee": "Q q", "fakkeenya": "Qeerransa", "hiika": "Tiger/Leopard", "gosa": "Dubbifamaa"},
    {"qubee": "R r", "fakkeenya": "Risaa", "hiika": "Eagle", "gosa": "Dubbifamaa"},
    {"qubee": "S s", "fakkeenya": "Saree", "hiika": "Dog", "gosa": "Dubbifamaa"},
    {"qubee": "T t", "fakkeenya": "Tulluu", "hiika": "Mountain", "gosa": "Dubbifamaa"},
    {"qubee": "V v", "fakkeenya": "Vaayirasii", "hiika": "Virus", "gosa": "Dubbifamaa"},
    {"qubee": "W w", "fakkeenya": "Waaqa", "hiika": "God/Sky", "gosa": "Dubbifamaa"},
    {"qubee": "Y y", "fakkeenya": "Yeroo", "hiika": "Time", "gosa": "Dubbifamaa"},
    {"qubee": "Z z", "fakkeenya": "Zeebiraa", "hiika": "Zebra", "gosa": "Dubbifamaa"},

    # Qubee Dachaa (Double Consonants)
    {"qubee": "CH ch", "fakkeenya": "Chala", "hiika": "Name", "gosa": "Qubee Dachaa"},
    {"qubee": "DH dh", "fakkeenya": "Dhagaa", "hiika": "Stone", "gosa": "Qubee Dachaa"},
    {"qubee": "NY ny", "fakkeenya": "Nyaata", "hiika": "Food", "gosa": "Qubee Dachaa"},
    {"qubee": "PH ph", "fakkeenya": "Phaaphii", "hiika": "Bishop", "gosa": "Qubee Dachaa"},
    {"qubee": "SH sh", "fakkeenya": "Shan", "hiika": "Five", "gosa": "Qubee Dachaa"},
    {"qubee": "TS ts", "fakkeenya": "Tseessuu", "hiika": "Transition", "gosa": "Qubee Dachaa"}
]

@app.route('/')
def home():
    return render_template('index.html', qubee_list=QUBEE_DATA)

if __name__ == '__main__':
    app.run(debug=True)
