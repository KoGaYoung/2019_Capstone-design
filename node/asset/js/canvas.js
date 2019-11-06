var pos = {
  drawable: false,
  x: -1,
  y:-1
};
var canvas, ctx;

window.onload = function() {
  canvas = document.getElementById("canvas");
  trash_button = document.getElementById("trash_b");
  ctx = canvas.getContext("2d");

  // event type
  canvas.addEventListener("mousedown", listener);
  canvas.addEventListener("mouseup", listener);
  canvas.addEventListener("mousemove", listener);
  canvas.addEventListener("mouseout", listener);
};

function listener(event){
  switch (event.type) {
    case "mousedown":
      initDraw(event);
      break;
    case "mousemove":
      if(pos.drawable)
        draw(event);
      break;
    case "mouseout":
    case "mouseup":
      finishDraw();
      break;

  }
}

function initDraw(event){
  ctx.beginPath();
  pos.drawable = true;
  var coors = getPosition(event);
  pos.X = coors.X;
  pos.Y = coors.Y;
  ctx.moveTo(pos.X, pos.Y);
}

function draw(event){
  var coors = getPosition(event);
  ctx.lineTo(coors.X, coors.Y);
  pos.X = coors.X;
  pos.Y = coors.Y;
  ctx.stroke();
}

function finishDraw(){
  pos.drawable = false;
  pos.X = -1;
  pos.Y = -1;
}

function getPosition(event){
  var x = event.pageX - canvas.offsetLeft - 10;
  var y = event.pageY - canvas.offsetTop - 380;
  return {X: x, Y: y};
}
function clearCanvas()
{
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.beginPath();

    localStorage.removeItem('imgData');
}
