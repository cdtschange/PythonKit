var FormUserValidation = function () {


    return {
        //main function to initiate the module
        init: function () {

            // for more info visit the official plugin documentation: 
            // http://docs.jquery.com/Plugins/Validation

            var form1 = $('.form-horizontal');
            var error1 = $('.alert-error', form1);
            var success1 = $('.alert-success', form1);

            form1.validate({
                errorElement: 'label', //default input error message container
                errorClass: 'help-inline', // default input error message class
                focusInvalid: false, // do not focus the last invalid input
                ignore: "",
                rules: {
                    username: {
                        minlength: 2,
                        maxlength: 20,
                        required: true
                    },
                    password: {
                        required: true,
                        minlength: 5,
                        maxlength: 20
                    },
                    password2: {
                        required: true,
                        minlength: 5,
                        maxlength: 20,
                        equalTo: "#password"
                    },
                    email: {
                        required: true,
                        email: true
                    },
                    mobile: {
                        required: true,
                        number: true
                    }
                },
                messages: { // custom messages for radio buttons and checkboxes
                    username: {
                        required: "用户名不能为空",
                        minlength: "用户名长度不能小于2个字符",
                        maxlength: "用户名长度不能大于20个字符"
                    },
                    password: {
                        required: "密码不能为空",
                        minlength: "密码长度不能小于5个字符",
                        maxlength: "密码长度不能大于20个字符"
                    },
                    password2: {
                        required: "密码不能为空",
                        minlength: "密码长度不能小于5个字符",
                        maxlength: "密码长度不能大于20个字符",
                        equalTo: "密码两次输入不一致"
                    },
                    email: {
                        required: "邮箱不能为空",
                        email: "邮箱地址无效"
                    },
                    mobile: {
                        required: "手机号不能为空",
                        number: "手机号无效"
                    }
                },

                invalidHandler: function (event, validator) { //display error alert on form submit    
                    error1.show();
                },

                highlight: function (element) { // hightlight error inputs
                    $(element)
                        .closest('.help-inline').removeClass('ok'); // display OK icon
                    $(element)
                        .closest('.control-group').removeClass('success').addClass('error'); // set error class to the control group
                },

                unhighlight: function (element) { // revert the change dony by hightlight
                    $(element)
                        .closest('.control-group').removeClass('error'); // set error class to the control group
                },

                success: function (label) {
                    label
                        .addClass('valid').addClass('help-inline ok') // mark the current input as valid and display OK icon
                    .closest('.control-group').removeClass('error').addClass('success'); // set success class to the control group
                },

                submitHandler: function (form) {
                    error1.hide();
                    form.submit();
                }
            });

            $('#btnSubmit').on('click', function(){
                if ($('.form-horizontal').validate().form()) {
                    $('.form-horizontal').submit();
                }
            }
         );

        }

    };

}();