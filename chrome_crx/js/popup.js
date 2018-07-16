

console.log("run popup");
var bg = chrome.extension.getBackgroundPage();

//删除cookie
//$.cookie('capuser', '', { expires: -1 }); 




//如果存在cookie,就直接隐藏登录框，显示收藏框
if (!!($.cookie("capuser")) == true) {
	$("#logindiv").css("display","none");
	$("#favdiv").css("display","");
    console.log("存在");
	chrome.tabs.getSelected(null, function (tab) {
	        console.log(tab.url);
	        console.log(tab.title);
	        $('#urlname').val(tab.title)
	        $('#urllink').val(tab.url)


	});

	//赋值

}else{
	console.log("不存在")
	$("#logindiv").css("display","");
	$("#favdiv").css("display","none");
}


 $.cookie("rmbUser", "true", { expires: 30 }); 

chrome.tabs.getSelected(null, function (tab) {
        console.log(tab.url);
        console.log(tab.title);
    });

$("#login").click(function(){
		$.ajax({
			url : 'http://www.qsones.com/checklogin.php',
			type : 'post',
			data : {
				username : $('#inputusername').val(),
				password : $('#inputpassword').val(),
			},
			success : function (data, response, status) {
				
				if (data > 0) {
					var capuser = $("#inputusername").val();
					$.cookie("capuser", capuser, { expires: 180 });
					$("#logindiv").css("display","none");
					$("#favdiv").css("display","");
					$("#tips").text('登录成功');

					//location.href = 'web/home/home.php';
				} else {
					$("#tips").text('用户名或密码错误');
					//存cookie
					


				}
			},
		});
});


// $("#closepopup").click(function(){
// 	chrome.pageAction.hid("popup.html")
// });



console.log("popup is run");

