
jQuery(document).ready(function($) {
	var xhr = new XMLHttpRequest();
	xhr.open("POST", "https://api.levelmoney.com/api/v2/hackathon/login", true);
	xhr.setRequestHeader('Content-Type', 'application/json');
	xhr.setRequestHeader('Accept', 'application/json');
	xhr.onloadend = function() {
	    var parsed = JSON.parse(this.response);
	    var pretty = JSON.stringify(parsed, null, 2);
	    document.getElementById('uname').textContent = "WELCOME!";
	};
	xhr.onerror = function(err) {
	    document.getElementById('uname').textContent = "ugh an error. i can't handle this right now.";
	};
	args = {"email": "hackdoc@levelmoney.com", "password": "hackathon1"};
	xhr.send(JSON.stringify(args));
});

$("#get_transactions").click(function()
{
	var xhr = new XMLHttpRequest();
	xhr.open("POST", "https://api.levelmoney.com/api/v2/hackathon/get-all-transactions", true);
	xhr.setRequestHeader('Content-Type', 'application/json');
	xhr.setRequestHeader('Accept', 'application/json');
	xhr.onloadend = function() {
	    var parsed = JSON.parse(this.response);
	    var pretty = JSON.stringify(parsed, null, 2);
	    $.getJSON('/_transactions', {
        transaction_list: pretty
      	}, function(data) {
        // $("#result").text(data.result);
      	});
	    document.getElementById('trans_list').textContent = pretty;
	};
	xhr.onerror = function(err) {
	    document.getElementById('trans_list').textContent = "ugh an error. i can't handle this right now.";
	};
	args = {"args": {"uid":  1110568334, "token":  "209E16DD45691753346973B767432F93", "api-token":  "HackathonApiToken"}};
	xhr.send(JSON.stringify(args));
});