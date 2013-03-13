$(document).ready(function(){
	$(".loginForm").hide("fast");
//	$(".signinbuttontxt").html("Sign in?");
	$("#signinbutton").click(function(){
		var oldtxt=$("#signinbutton").text();
//		$("#signinbutton").html(oldtxt);
		if(oldtxt.match("Sign in?")){
			$(".loginForm").show("fast");
			$(".registerForm").hide("fast");
			$("#signinbutton").html("New User?");
		}
		else if(oldtxt.match("New User?")){
			$(".loginForm").hide("fast");
			$(".registerForm").show("fast");
			$("#signinbutton").html("Sign in?");
		}
		else{
//			$("#signinbutton").html(oldtxt);
			$("#signinbutton").html("ERROR");
		}
	});
});