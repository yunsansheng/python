console.log("run bg");
function test()
{
    alert('我是background！');
}



chrome.browserAction.setBadgeText({text: 'new'});
//获取cookie
function getCookie(c_name)
{
if (document.cookie.length>0)
  {
  c_start=document.cookie.indexOf(c_name + "=")
  if (c_start!=-1)
    { 
    c_start=c_start + c_name.length+1 
    c_end=document.cookie.indexOf(";",c_start)
    if (c_end==-1) c_end=document.cookie.length
    return unescape(document.cookie.substring(c_start,c_end))
    } 
  }
return ""
}


function iscookie(){
	if (getCookie("rmbUser")!=""){
		console.log("cookie is exists")
		return 1
	}else{
		console.log("cookie is not exists")
		return 0

	}
}

