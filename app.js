let number = 52
let firstName = 'Artyom'
const isProgrammer = true 
alert("SDdsdsdsds")
// console.log('qwe',  isProgrammer)
// console.log(number + 100)
// console.log(number * 10)
// console.log(number / 10)
// console.log(number % 45)
// let zxc = firstName + ' Tsvetkov'
// console.log(zxc)

const resultElement = document.getElementById('result')
const input1 = document.getElementById('input1')
const input2 = document.getElementById('input2')
const submitBtn = document.getElementById('submit')
const plusBtn = document.getElementById('plus')
const minusBtn = document.getElementById('minus')

// console.log(input1.value)
// console.log(resultElement.textContent)
// resultElement.textContent = 42


// console.log(typeof sum)

// submitBtn.onclick = function() {
//     console.log('Hello click')
//     const sum = Number(input1.value) + Number(input2.value)
//     resultElement.textContent = sum
// }

// plusBtn.onclick = function() {
//     console.log('Hello click')
//     const sum = Number(input1.value) + Number(input2.value)
//     resultElement.textContent = sum
// }

// minusBtn.onclick = function() {
//     console.log('Hello click')
//     const sum = Number(input1.value) - Number(input2.value)
//     resultElement.textContent = sum
// }

plusBtn.onclick = function() {
    action = '+'
}

minusBtn.onclick = function() {
    action = '-'
}

function printResult (result) {
    if (result < 0) {
        resultElement.style.color = 'red'
    } else {
        resultElement.style.color = 'green'
    }
    resultElement.textContent = result
}

function computeCalculation (inp1, inp2, actionSymbol) {
    const num1 = Number(inp1.value)
    const num2 = Number(inp2.value)
    // if (actionSymbol == '+') {
    //     return num1 + num2
    // } else {
    //     return num1 - num2
    // }
    return actionSymbol == '+' ? num1 + num2 : num1 - num2
}

submitBtn.onclick = function() {
    const result = computeCalculation(input1, input2, action)
    printResult(result)
}
b = 52
n = '52'
console.log(b === n)