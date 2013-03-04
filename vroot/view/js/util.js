function ajaxHandler(target, method, errorDiv) {
	errorDiv.html("&nbsp");
	$.ajax({
		type: method,
		dataType: "json",
		url: target,
		success: function(response) {
			window.location.href = response.target;
		}
	});
}

function ajaxFormHandler(target, method, form, errorDiv) {
	errorDiv.html("&nbsp");
	$.ajax({
		type: method,
		dataType: "json",
		url: target,
		data: form.serialize(),
		success: function(response) {
			if(response.success == true) {
				window.location.href = response.target;
			}
			else {
				errorDiv.html(response.error);
			}
			
		}
	});
}