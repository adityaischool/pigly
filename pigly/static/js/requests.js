//***************** ALL BACK BUTTONS ******************//

$('#fin_overview_back').click(function()
{
	$('#fin_overview').hide();
	$('#login').show();
});


//****************** LOGIN PAGE ***********************//
jQuery(document).ready(function($) {
	$('#fin_overview').hide();
	var xhr = new XMLHttpRequest();
	xhr.open("POST", "https://api.levelmoney.com/api/v2/hackathon/login", true);
	xhr.setRequestHeader('Content-Type', 'application/json');
	xhr.setRequestHeader('Accept', 'application/json');
	xhr.onloadend = function() {
	    var parsed = JSON.parse(this.response);
	    var pretty = JSON.stringify(parsed, null, 2);
	    document.getElementById('login_caption').textContent = "WELCOME!";
	};
	xhr.onerror = function(err) {
	    document.getElementById('login_caption').textContent = "ugh an error. i can't handle this right now.";
	};
	args = {"email": "hackdoc@levelmoney.com", "password": "hackathon1"};
	xhr.send(JSON.stringify(args));
	// alert("1234567890".replace(/(.{3})/g,",$1"));
});


//****************** FIN OVERVIEW ***********************//
function separate_comma(ip_str){
	var ret_str = ip_str.split('').reverse().join('');
	ret_str = ret_str.replace(/(.{3})/g,",$1").split('').reverse().join('');
	ret_str = ret_str.replace(/,$/, "");
	return ret_str;
}
$("#login_next").click(function()
{
	var xhr = new XMLHttpRequest();
	xhr.open("POST", "https://api.levelmoney.com/api/v2/hackathon/get-accounts", true);
	xhr.setRequestHeader('Content-Type', 'application/json');
	xhr.setRequestHeader('Accept', 'application/json');
	xhr.onloadend = function() {
		var accounts = JSON.parse(this.response)['accounts'];
		$('#login').hide();
		var total_balance = 0;
		$('#fin_overview_accounts').empty();
		for(i=0; i < accounts.length; i++){
			var balance = parseFloat(accounts[i]['balance'])/1000;
			balance_str = separate_comma(balance.toString());			
			total_balance += balance;
			$('<div>\
				<p> Checkings Account </p>\
	        	<p> xxxx-xxxx-xxxx-'+accounts[i]["last-digits"]+'</p>\
	        	<p> $'+balance_str+'</p>\
	  		</div>').appendTo('#fin_overview_accounts');
		}
		document.getElementById('fin_overview_total_balance').textContent = "Total Balance: $" + separate_comma(total_balance.toString());
	};
	xhr.onerror = function(err) {
	    // document.getElementById('accounts_list').textContent = "ugh an error. i can't handle this right now.";
	};
	args = {"args": {"uid":  1110568334, "token":  "209E16DD45691753346973B767432F93", "api-token":  "HackathonApiToken"}};
	xhr.send(JSON.stringify(args));
	$('#fin_overview').show();
});

//****************** AGE ***********************//
$("#get_age").click(function()
{
	$('#login').hide();
	$("#age").show();
	$('.demo-btn').hover(function() {
          $(this).addClass("animated pulse");
        }, function() {
          $(this).removeClass("animated pulse");
        });
      
        $('.demo-btn').click(function() {
          if ($(this).find(".goal-img").hasClass("add-btn-checked") || $(this).hasClass("custom-btn")){
            $(this).removeClass("btn-checked");
            $(this).find(".goal-img").removeClass("add-btn-checked")
          } else {
            $(this).addClass("btn-checked");
            $(this).find(".goal-img").addClass("add-btn-checked");
          }
        });
      
        $('.cc-loan-btn').click(function(){
          console.log("loan or cc btn clicked");
          $(".cc-loan-btn").addClass("demo-btn-checked");
        });
      
        $('.custom-btn').click(function(){
          console.log("custom button");
          $(".goals-questions").removeClass("show").addClass("hide");
          $(".custom-goal").addClass("animated fadeInRight show");
        });
      
        $('.goal-back').click(function(){
          console.log("goal back button click");
          $(".goals-questions").addClass("animated fadeInLeft show");
          $(".custom-goal").removeClass("show").addClass("hide");
        });
});

//****************** GENDER ***********************//
$("#age_next").click(function()
{
	$("#age").hide();
	$('#gender').show();

    $('.gender-icon').hover(function() {
      $('.gender-icon').innerHTML("eh");
    });
  
  
    $('.demo-btn').hover(function() {
      $(this).addClass("animated pulse");
    }, function() {
      $(this).removeClass("animated pulse");
    });
  
    $('.demo-btn').click(function() {
      if ($(this).find(".goal-img").hasClass("add-btn-checked") || $(this).hasClass("custom-btn")){
        $(this).removeClass("btn-checked");
        $(this).find(".goal-img").removeClass("add-btn-checked")
      } else {
        $(this).addClass("btn-checked");
        $(this).find(".goal-img").addClass("add-btn-checked");
      }
    });
  
    $('.cc-loan-btn').click(function(){
      console.log("loan or cc btn clicked");
      $(".cc-loan-btn").addClass("demo-btn-checked");
    });
  
    $('.custom-btn').click(function(){
      console.log("custom button");
      $(".goals-questions").removeClass("show").addClass("hide");
      $(".custom-goal").addClass("animated fadeInRight show");
    });
  
    $('.goal-back').click(function(){
      console.log("goal back button click");
      $(".goals-questions").addClass("animated fadeInLeft show");
      $(".custom-goal").removeClass("show").addClass("hide");
    });
});

//****************** GOALS ***********************//
$("#gender_next").click(function()
{
	$('#gender').hide();
	$('#goals').show();

	$('.demo-btn').hover(function() {
        $(this).addClass("animated pulse");
      }, function() {
        $(this).removeClass("animated pulse");
      });
    
      $('.demo-btn').click(function() {
        if ($(this).find(".goal-img").hasClass("add-btn-checked") || $(this).hasClass("custom-btn")){
          $(this).removeClass("btn-checked");
          $(this).find(".goal-img").removeClass("add-btn-checked")
        } else {
          $(this).addClass("btn-checked");
          $(this).find(".goal-img").addClass("add-btn-checked");
        }
      });
    
      $('.cc-loan-btn').click(function(){
        console.log("loan or cc btn clicked");
        $(".cc-loan-btn").addClass("demo-btn-checked");
      });
    
      $('.custom-btn').click(function(){
        console.log("custom button");
        $(".goals-questions").removeClass("show").addClass("hide");
        $(".custom-goal").addClass("animated fadeInRight show");
      });
    
      $('.goal-back').click(function(){
        console.log("goal back button click");
        $(".goals-questions").addClass("animated fadeInLeft show");
        $(".custom-goal").removeClass("show").addClass("hide");
      });
});


//****************** YET TO BE USED ***********************//
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

$("#get_projected_transactions").click(function()
{
	var xhr = new XMLHttpRequest();
	xhr.open("POST", "https://api.levelmoney.com/api/v2/hackathon/projected-transactions-for-month", true);
	xhr.setRequestHeader('Content-Type', 'application/json');
	xhr.setRequestHeader('Accept', 'application/json');
	xhr.onloadend = function() {
	    var parsed = JSON.parse(this.response);
	    var pretty = JSON.stringify(parsed, null, 2);
	    $.getJSON('/_projected_transactions', {
        proj_transaction_list: pretty
      	}, function(data) {
        // $("#result").text(data.result);
      	});
	    document.getElementById('projected_trans').textContent = pretty;
	};
	xhr.onerror = function(err) {
	    document.getElementById('projected_trans').textContent = "ugh an error. i can't handle this right now.";
	};
	args = {"args": {"uid":  1110568334, "token":  "209E16DD45691753346973B767432F93", "api-token":  "HackathonApiToken"}, "year":  2015, "month":  3};
	xhr.send(JSON.stringify(args));
});
