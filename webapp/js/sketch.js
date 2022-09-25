
const s = (sketch) => {
  var capture;
  var url = "http://10.1.135.184:8080/video";
  let cv = window.cv;

  sketch.setup = () => {
    width = $("#screen-id")[0].clientWidth;
    height = $("#screen-id")[0].clientHeight;
    console.log(width);
    var canvas = sketch.createCanvas(width, height);
    canvas.parent("screen-id");
    sketch.background(sketch.color("white"));

    capture = new cv.VideoCapture(url);
  };
  
  sketch.draw = () => {
    [camera, frame] = capture.read();

    if (frame !== null)
      cv.imshow("Frame", frame);
  };
}

