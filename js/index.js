

// solicitar variables con prompt
let nombre = "Juan"
let edad = 25
// let nombre = prompt("Ingresa tu nombre")
// let edad = Number(prompt("Ingresar edad"))

// crear elementos
let nombreText = document.createElement('p')
let edadText = document.createElement('p')
// darles valor al texto de los elementos
nombreText.textContent = nombre
edadText.textContent = edad

//agregar los elementos al body
document.body.appendChild(nombreText)
document.body.appendChild(edadText)


//obtener boton
const multiplicarEdad = document.querySelector('#multedad')
multiplicarEdad.addEventListener('click', ()=> {
    edadText.textContent = edad*2
})


//crear elementos en base a una lista
let frutas = ["Manzana", "Pera", "Uva", "Melocotón","Sandia"]
const lista = document.getElementById('lista')
frutas.forEach((fruta => {
    const li = document.createElement('li')
    li.textContent = fruta
    // li.className = "fruta"
    li.classList.add('fruta')
    lista.appendChild(li)
}))

