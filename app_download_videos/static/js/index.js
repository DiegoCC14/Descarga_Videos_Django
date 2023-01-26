
$(document).ready(function(){
	$("#div_resultados").hide(true);
});

function mostrar_resultados(){
}

function borrar_items_resultados(){
	$(".item").remove()	
}

function obtener_mb_enteros( str_mb ){
	str_mb_entero = ""
	for( let i=0 ; i<str_mb.length ; i++ ){
		console.log( str_mb[i] )
		if (str_mb[i] == "."){
			break
		}
		str_mb_entero += str_mb[i]	
	}
	return str_mb_entero
}

function post_busqueda_videos(){
	let url_ingresado = $("#url_ingresado_busqueda").val()
	
	$.ajax({
		headers : {
            'X-CSRFToken' : CSRF_TOKEN
        },
		url: $("#form_info_url").attr('action'),
		type : 'POST',
		data : { 'url' : url_ingresado , 'tipo': "video" },
		dataType : 'json',

		success : function( json ) {
			
			borrar_items_resultados()

			if ( json['resolucion_videos'].length > 0 ){
				
				inf_video = json['resolucion_videos'][0]
				
				$("#div_resultados_videos").append( div_item_video_info );

				$("#item_video_info").find('h5').text( json['titulo'] ) 	
				$("#item_video_info").find('img').attr("src", json['img'] )
				$("#item_video_info").find('a').text( inf_video['resolution'] + " - " + obtener_mb_enteros( String(inf_video['filesize']) ) + "mb" )
				$("#item_video_info").find('a').attr("id", String( inf_video['itag'])+ "-" + url_ingresado )

				for (let i=1; i<json['resolucion_videos'].length ; i++ ){
					
					inf_video = json['resolucion_videos'][i]
					
					let new_div = $("#item_video_info").clone()

					new_div.find('h5').text( json['titulo'] ) 					
					new_div.find('img').attr("src", json['img'] )
					new_div.find('a').text( inf_video['resolution'] + " - " + obtener_mb_enteros( String(inf_video['filesize']) ) + "mb" )
					new_div.find('a').attr("id", String( inf_video['itag'])+ "-" + url_ingresado )
					
					$("#div_resultados_videos").append( new_div );

				}

			}

			$("#div_resultados").show(true);

    	},
    	error : function( xhr , status ) {
			alert('Disculpe, existió un problema');
    	},
	})
}

function descargar_video( event ){
	itag = event.id.substring(0,2)
	url = event.id.substring(3,event.id.length)
	$.ajax({
		headers : {
            'X-CSRFToken' : CSRF_TOKEN
        },
		url: $("#form_download_video").attr("action"),
		type : 'POST',
		data : { 'url' : url , 'itag': itag },
		dataType : 'json',
		success : function( json ) {
			console.log( json )
			let url_video = document.URL + json['url_descarga']
			console.log( url_video )
			let url_descarga = json['url_descarga']
			window.open( url_video , '_blank');
			//window.location.replace("http://www.w3schools.com");
    	},
    	error : function( xhr , status ) {
			alert('Disculpe, existió un problema');
    	},
	})
	
}


var div_item_video_info = '<div class="item features-image сol-12 col-md-6 col-lg-4" id="item_video_info"><div heigth="60%"><div class="element-wrapper"><img src="https://i.ytimg.com/vi/MPLN1ahXgcs/sddefault.jpg?v=601d6e64" width="100%"><h5 class="item-title mbr-fonts-style">Nombre Video Nombre Video Nombre Video Nombre Video Nombre Video Nombre Video</h5><a class="btn btn-success item-btn display-5" target="_blank" onclick="descargar_video( this )" >Descargar</a></div></div> </div>'
