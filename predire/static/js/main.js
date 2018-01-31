/*---------------------------------------------| Show Hide Password filed |----------------------------------------------------------*/
function myFunction() {
    var appNumber = document.getElementById("app-selector").value;
    var userNumber = document.getElementById("user-selector").value;
    document.getElementById("password-holder").style.display = "block";

    if((appNumber == "App1") & (userNumber == "UserOne"))
    {
    	letsGo();
    }
    alert(appNumber +"  "+userNumber);
}
/*---------------------------------------------| Hitting GO Button |----------------------------------------------------------*/
function letsGo() {
    document.getElementById("login-button").style.display = "none";
    document.getElementById("password-holder").style.display = "none";
    document.getElementById("token-holder").style.display = "block";
    log(appNumber +"  "+userNumber);
}
/*---------------------------------------------| Hitting GO Button |----------------------------------------------------------*/
function logOut() {
	document.getElementById("dummyForm").reset();
    document.getElementById("token-holder").style.display = "none";
    document.getElementById("login-button").style.display = "block";
    document.getElementById("user-selector").selectedIndex = 0;
    document.getElementById("app-selector").selectedIndex = 0;
}