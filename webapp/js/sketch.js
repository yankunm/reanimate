const s = (sketch) => {
  var detector, context;
  sketch.setup = () => {
    width = $("#screen-id")[0].clientWidth;
    height = $("#screen-id")[0].clientHeight;
    var canvas = sketch.createCanvas(width, height);
    canvas.parent("screen-id");
    sketch.background(sketch.color("white"));
    var canv = $("#canvas");
    context = canv.getContext("2d");
    detector = new AR.Detector();
  };
  
  sketch.draw = () => {
    img = cv.imread("livestream");
    var markers = detector.detect(img);
    drawCorners(markers);
  };

         
  function drawCorners(markers){
    var corners, corner, i, j;
  
    context.lineWidth = 3;

    for (i = 0; i !== markers.length; ++ i){
      corners = markers[i].corners;
      
      context.strokeStyle = "red";
      context.beginPath();
      
      for (j = 0; j !== corners.length; ++ j){
        corner = corners[j];
        context.moveTo(corner.x, corner.y);
        corner = corners[(j + 1) % corners.length];
        context.lineTo(corner.x, corner.y);
      }

      context.stroke();
      context.closePath();
      
      context.strokeStyle = "green";
      context.strokeRect(corners[0].x - 2, corners[0].y - 2, 4, 4);
    }
  }
}
 