

// let nombre = "Juan"
// let edad = 25

let edadLocal = localStorage.getItem("edad");
let nombreLocal = localStorage.getItem("nombre");
if (!nombreLocal) {
    do {
        nombreLocal = prompt("Ingresa tu nombre")
        localStorage.setItem("nombre", nombreLocal) 
    } while (nombreLocal == "");
}

if (!edadLocal) {
    do {
        edadLocal = Number(prompt("Ingresar edad"))  
        localStorage.setItem("edad", edadLocal)  
    } while (edadLocal == false || isNaN(edadLocal));
}


// solicitar variables con prompt
// let nombre = prompt("Ingresa tu nombre")
// let edad = Number(prompt("Ingresar edad"))

// crear elementos
let nombreText = document.createElement('p')
let edadText = document.createElement('p')
// darles valor al texto de los elementos
nombreText.textContent = nombreLocal
edadText.textContent = edadLocal

//agregar los elementos al body
document.body.appendChild(nombreText)
document.body.appendChild(edadText)


//obtener boton
const multiplicarEdad = document.querySelector('#multedad')
multiplicarEdad.addEventListener('click', ()=> {
    edadText.textContent = edadLocal*2
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

// Obtener info de formilario
localStorage.setItem("listaProductos", JSON.stringify([{
    name : "jugo",
    precio : 1000
}]))
const formulalrio = document.getElementById('product-form')

formulalrio.addEventListener('submit', (e) =>{
    e.preventDefault()
    let listaProductos = JSON.parse(localStorage.getItem("listaProductos"))
    const nombreProducto = document.getElementById('nombre-producto').value
    const precioProducto = document.getElementById('precio-producto').value
    console.log(listaProductos);
})


