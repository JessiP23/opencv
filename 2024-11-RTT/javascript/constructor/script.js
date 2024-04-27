const adventurer = {
    name: 'Robin',
    health: 10,
    inventory: ['sword', 'potion', 'artifact'],
    companion: {
        name: 'Leo',
        type: 'cat',
        companion: {
            name: 'Frank',
            type: 'Flea',
            belongings: ['small hat', 'sunglasses'],
        }
    },
    roll (mod = 0) {
        const result = Math.floor(Math.random() * 20) + 1 + mod;
        console.log(`${this.name} rolled a ${result}`);
    }
}

class Character {
    constructor (name) {
        this.name = name;
        this.health = 100;
        this.inventory = [];
    }
}

const robin = new Character('Robin');
robin.inventory = ['sword', 'potion', 'artifact'];
robin.companion = new Character('Leo');
robin.companion.type = 'Cat';
robin.companion.companion = new Character('Frank');
robin.companion.companion.type = 'Flea';
robin.companion.companion.inventory = ['small', 'hat', 'sunglasses'];

//child class inherits all properties of its parents, so in this case we dont accont name, health, inventory, or roll.

class adventure extends Character {
    constructor (name, role) {
        super(name);
        this.role = role;
        this.inventory.push('bedroll', '50 gold coins');
    }
    scout() {
        console.log(`${this.name} is scouting ahead...`);
        super.roll();
    }
}