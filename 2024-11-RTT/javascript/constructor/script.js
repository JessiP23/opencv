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