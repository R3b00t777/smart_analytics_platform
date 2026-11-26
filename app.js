// JavaScript source code
function calculatePrice(price, discount, tax, bonus, extra) {
    let result = price;

    if (discount > 0) result -= discount;
    if (tax > 0) result += tax;
    if (bonus > 0) result -= bonus;
    if (extra > 0) result += extra;

    return result;
}

function greetUser(name) {
    return 'Welcome, ' + name;
}

const finalPrice = calculatePrice(100, 10, 5, 2, 3);
const greeting = greetUser('Student');

process.stdout.write(greeting);
process.stdout.write('Final price: ' + finalPrice);

