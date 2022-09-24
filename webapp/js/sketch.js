
const s = (sketch) => {
  sketch.setup = () => {
    width = $("#screen-id")[0].clientWidth;
    height = $("#screen-id")[0].clientHeight;
    console.log(width);
    var canvas = sketch.createCanvas(width, height);
    canvas.parent("screen-id");
    sketch.background(sketch.color("white"));

    var camera, cp, frame, q, url;
    url = "Your IP Address/video";
    cap = new cv2.VideoCapture(url);

    while (true) {
      [camera, frame] = cap.read();

      if (frame !== null)
        cv2.imshow("Frame", frame);

      q = cv2.waitKey(1);
      
      if (q === ord("q"))
        break;
    }

    cv2.destroyAllWindows();

  };
  
  sketch.draw = () => {
    video = true;
  };
}

