$(document).ready(function(){
    $.get("https://api.adderou.cl/tyaas/", function(data){
        $.each(data.titulo, function(i,item){
            var fecha = "<h2>"+item.titulo+"</h2>"

            $("#fecha-horoscopo").append(fecha);
            // console.log(item.titulo)
        })
    })
})



$(document).ready(function(){
    $.get("https://api.adderou.cl/tyaas/",function (data){
        
        $.each(data.horoscopo , function(i, item){
            var lista = "<ul><li>"+"Fecha del Signo: "+item.fechaSigno+"</li><li>"+ "Amor: "+item.amor + "</li><li>" +"Salud: "+ item.salud + "</li><li>" +"Dinero: "+item.dinero + "</li><li>" +"Color: "+ item.color +"</li></ul>"

            $("#card-"+item.nombre).append(lista);
            console.log(item.nombre)
        })
    })
})














// $(document).ready(function () {
//     $("#btn-obtener").click(function () {
//         // hacemos la solicitud http
//         $.get("https://www.themealdb.com/api/json/v1/1/categories.php", function (data) {
//             // leemos el Json
//             $.each(data.categories, function (i, item) {
//                 var fila = "<tr><td>" + item.idCategory + "</td><td>" + item.strCategory +
//                     "</td><td><img src='" + item.strCategoryThumb + "'>" +
//                     "</td><td>" + item.strCategoryDescription + "</td></tr>"
                
//                 $("#tabla-categorias").append(fila);

//             })
//         })
//     })
// })