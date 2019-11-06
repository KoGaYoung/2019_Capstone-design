//clients
var socket = io();

$('#chat').on('submit', function(e){
  socket.emit('send message', $('#name').val(), $('#message').val());
  $('#message').val('');
  $("#message").focus();
  e.preventDefault();
});

socket.on('receive message', function(msg){
  $('#chatLog').append(msg+'\n');
  var JSAlert = require('js-alert');
  JSAlert.alert(msg);
  $('#chatLog').scrollTop($('#chatLog')[0].scrollHeight);
});

socket.on('change name', function(name){
  $('#name').val(name);
});


function showPopUp(){
  var ifram = document.getElementById('side');
  if(ifram.style.visibility=='hidden'){
    ifram.style.visibility = 'visible';
  }else{
    ifram.style.visibility='hidden';
  }
}

// socket.on('enter user', function(enter){
//   $('#chatLog').append(enter+'\n');
//   var JSAlert = require('js-alert');
//   JSAlert.alert(enter);
//   $('#chatLog').scrollTop($('#chatLog')[0].scrollHeight);
// });
//
// socket.on('disconnected message', function(name){
//   $('#chatLog').append(name+'님이 나가셨습니다.'+'\n');
//   var JSAlert = require('js-alert');
//   JSAlert.alert(enter);
//   $('#chatLog').scrollTop($('#chatLog')[0].scrollHeight);
// });
