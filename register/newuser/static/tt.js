var codeok=false
var idok=false
$(document).ready(function(){
	$('input').keyup(function(){
		$('#result').html('')
	})
	$('#uid').keyup(function(){
		var uid=$("#uid").val();
		$.get('/checkuid/',{'uid':uid},function(r){
			if(r=='ID可用'){idok=true}
			else {idok=false}
			$('#ruid').html(r)
		})
	})
	$('#submit').click(function(){   //单击提交按钮，先检查数据，通过后再将数据提交服务器
        if(!idok){
          $('#result').html('<span style="color:red">你输入的用户ID已被占用！</span>')
          return 1
        }
        var pwd1=$("#pwd1").val();
        var pwd2=$("#pwd2").val();
        if (pwd1!=pwd2){
          $('#result').html('<span style="color:red">两次输入的密码不一致！</span>')
          return 1}
        var reg=/^\w[0-9]+@[a-zA-Z0-9]{2,10}(\.[a-z]{2,4}){1,3}$/   //email的正则表达式，可匹配例如aa@bb.cc.dd.ee格式
        if (!reg.test($('#email').val())){
        $('#result').html('<span style="color:red">输入的Email地址无效！</span>')
         return 1
        }
        var uid=$("#uid").val()
        var pwd=$("#pwd1").val()
        var email=$('#email').val()
        $.get("/addnew/",{'uid':uid,'pwd':pwd,'email':email},function(r){  //调用doAddNew视图函数，存储到数据库，并告知结果
        $('#result').html(r)})
        idok=false   // 不加此代码，可以一个用户注册重复提交
        $('#ruid').html('')
    })
})

