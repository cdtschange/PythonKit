var Login = function () {
    
    return {
        //main function to initiate the module
        init: function () {
        	
           $('.login-form').validate({
	            errorElement: 'label', //default input error message container
	            errorClass: 'help-inline', // default input error message class
	            focusInvalid: false, // do not focus the last invalid input
	            rules: {
	                username: {
	                    required: true
	                },
	                password: {
	                    required: true
	                },
	                remember: {
	                    required: false
	                }
	            },

	            messages: {
	                username: {
	                    required: "用户名不能为空"
	                },
	                password: {
	                    required: "密码不能为空"
	                }
	            },

	            invalidHandler: function (event, validator) { //display error alert on form submit 
	                $('.alert-error', $('.login-form')).show();
	            },

	            highlight: function (element) { // hightlight error inputs
	                $(element)
	                    .closest('.control-group').addClass('error'); // set error class to the control group
	            },

	            success: function (label) {
	                label.closest('.control-group').removeClass('error');
	                label.remove();
	            },

	            errorPlacement: function (error, element) {
	                error.addClass('help-small no-left-padding').insertAfter(element.closest('.input-icon'));
	            },

	            submitHandler: function (form) {
        			Login.remember();
	            	form.submit();
	            },
	        });

	        $('.login-form input').keypress(function (e) {
	            if (e.which == 13) {
	                if ($('.login-form').validate().form()) {
	                	Login.remember();
	            		$('.login-form').submit();
	                }
	                return false;
	            }
	        });

        },


	    remember: function () { 
			if ($("#remember").attr("checked")) { 
				var username = $("#username").val(); 
				var password = $("#password").val(); 
				$.cookie("rmbUser", "true", { expires: 7 }); //存储一个带7天期限的cookie 
				$.cookie("username", username, { expires: 7 }); 
				$.cookie("password", password, { expires: 7 }); 
			}else{ 
				$.cookie("rmbUser", "false", { expire: -1 }); 
				$.cookie("username", "", { expires: -1 }); 
				$.cookie("password", "", { expires: -1 }); 
			} 
		}

    };

}();