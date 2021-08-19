const obj = {};
obj.lastName = 'Berry';


if (obj.hasOwnProperty('name')) {
    console.log(`obj.name is indeed a prop with value: ${obj.name}`);
} else {
    console.log('false')
}

const myMap = new Map();

myMap.set("Nathan", "555-0182");
myMap.set("Jane", "315-0322");
myMap.set('Blb', "941-3242");

for (let [key,value] of myMap) {
    console.log(`Key is: ${key} and value is: ${value} biatch`);
}

var a = 42;

var b = (a > 41) ? 'hello' : 'goodbye';
// tertiary operator above, basically a one line 'if...else' statement

function makeMultiplier(firstNumber) {
    // firstNumber is now scoped inside the function
    function multiply(secondNumber) {
        // multiply function can use 'firstNumber' because it has closure over it
        return secondNumber * firstNumber;
    }
    return multiply;
}

let multiply_x_7 = makeMultiplier(7);
// let var gets reference to inner function 
//with closure over its parameter of the outer function

let multiply_x_14 = makeMultiplier(14);


console.log(multiply_x_14 (23));
console.log(multiply_x_7 (7));


//consider
function User() {
    // this is private
    let username, password;
    // this is private
    function doLogin(user,pw) {
        username = user;
        password = pw;
        // when User is done running, doLogin still remembers 'username' and 'password'

        // other login work
    }


    let publicAPI = { // reference to the inner function
        login: doLogin
    };

    return publicAPI; // returned from User and becomes instance of function
    
}
// instantitate 'User' module 
let vlad = User();

vlad.login( 'admin', '1234Five*');
console.log(vlad);


// implemending my own hash table from https://www.freecodecamp.org/news/javascript-hash-table-associative-array-hashing-in-js/

class HashTable {
    constructor() {
        this.table = new Array(127); 
        this.size = 0;
    }
    
    _hash(key) {
        let hash = 0;
        for (let i = 0; i < key.length; i++) {
            console.log(`hash=${hash}:index=${i}`); //debug hash output
            hash += key.charCodeAt(i);
        }
        return hash % this.table.length;
    }     

    set(key, value) {
        const index = this._hash(key); // call hash to get index value
        if (this.table[index]) {
            for (let i = 0; i < this.table[index].length; i++) {
                if (this.table[index][i][0] === key) {
                    this.table[index][i][1] = value;
                    return;
                } 
            }
            this.table[index].push([key, value]);
        } else {
            this.table[index] = [];
            this.table[index].push([key, value]);
        }
        this.size++;
    }

    get(key) {
        const index = this._hash(key);
        if (this.table[index]) {
            for (let i = 0; i < this.table.length; i++) {
                if (this.table[index][i][0] === key) {
                    return this.table[index][i][1];
                }
            }
         }
        return undefined;
    }

    delete(key) {
        const index = this._hash(key);

        if (this.table[index] && this.size > this.table[index].length) {
            for (let i = 0; i < this.table.length; i++) {
                if (this.table[index][i][0] === key) {
                    this.table[index].splice(i, 1);
                    this.size--;
                    return true;
                }
            }
        } else {
            return false;
        }
    }

    display() {
        this.table.forEach((values, index) =>  {
            const chainedValues = values.map(
                ([key, value]) =>  `[${key}: ${value}]`
            );
            console.log(`${index}: ${chainedValues}`);
        });
    }

}

const ht = new HashTable();
ht.set("Vlad", true);
ht.set('names', 80);
ht.display();
console.log(ht.get("vlad"));
console.log(ht.get("Vlad"));
console.log(ht.get("names"));
ht.display();
console.log(ht.delete("names"));
console.log(ht.delete("Vlad"));
ht.display();
console.log(ht.get("Vlad"));