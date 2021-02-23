const adjectives = [
    'Engaging',
    'Gregarious',
    'Amorous',
    'Svelte',
    'Alert',
    'Earnest'
];

const animals = [
    'Badger',
    'Platypus',
    'Komono Dragon',
    'Camel',
    'Pufferfish',
    'Babyshark'
];

export const generateName = () => {
    const adjective = adjectives[Math.floor(Math.random() * adjectives.length)];
    const animal = animals[Math.floor(Math.random() * animals.length)];
    return `${adjective} ${animal}`;
};
