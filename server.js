//expree를 사용하여 http서버 생성
var express = require('express');
var app = express();
var http = require('http').Server(app);
//생성된 sever를 socket.io 서버로 업그레이드
var io = require('socket.io')(http);

//모든 request는 cleint를 responce하도록 라우터임
app.get('/',function(req, res){
  res.sendFile(__dirname + '/FrontEnd/chattingPage.html');
  // res.sendFile(__dirname + '/FrontEnd/draw.html');
});
app.get('/draw',function(req, res){
  res.sendFile(__dirname + '/FrontEnd/draw.html');
});

//io.on(EVENT,함수)는 서버에 전달된 EVENT를 인식하여 함수를 실행시키는 event listener
var count = 1;
io.on('connection', function(socket){

  console.log('user connected: ', socket.id);
  var name = "user" + count++;
  io.to(socket.id).emit('change name', name);

  // var enter = name+ '님이 입장하셨습니다.<br/>';
  // io.emit('enter user', enter);

  socket.on('disconnect', function(){
      console.log('user disconnect : '+ socket.id);
      // io.emit('disconnected message', name);
  });

  socket.on('send message', function(name,text){
    var msg = name + ': ' + text+ '<br/>';
    io.emit('receive message', msg);
    console.log(msg);
  });
});

http.listen(3000, function(){
  console.log('server on!');
});

app.use(express.static(__dirname +'/public'));
