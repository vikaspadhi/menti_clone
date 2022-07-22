let groupname = JSON.parse(document.getElementById("room_name").textContent);

let ws = new WebSocket(`ws://${window.location.host}/ws/sc/${groupname}/`);

ws.onopen = (event) => {
  // console.log("Websocket connected...", event);
};

ws.onmessage = (event) => {
  data = JSON.parse(event.data);
  // console.log(data);
  active_users = data["users_joined"];
  document.getElementById("user_count").innerHTML = active_users;

  if (data["question"]) {
    let correct_answer = data["options"].filter((index) => {
      if (index[1]) {
        return index;
      }
    })[0][0];

    let template = `
    <p>1. ${data["question"]}</p><div>`;

    data["options"].map((index) => {
      template += `<div class="form-check border border-warning p-3 my-3">
                <input
                  class="form-check-input answers"
                  type="radio"
                  name="answers"
                  value = ${index[0]}
                />
                <label class="form-check-label">
                  ${index[0]}
                </label>
              </div>`;
    });

    template += `</div>`;
    document.getElementById("quiz_board").innerHTML = template;

    let timer = 10;
    $("#next").addClass("disabled");
    const interval = setInterval(() => {
      
      timer--;
      // console.log(timer);
      document.getElementById("timer").innerHTML = timer
      if (timer == 0) {
        clearInterval(interval);
        let answer = document.querySelector(
          'input[name="answers"]:checked'
        ).value;
        if(answer == correct_answer)
        {
          alert("Correct Answer")
          $("#next").removeClass("disabled");
        }
        else
        {
          alert("Worng Answer...")
        }
      }
    }, 1000);



  }
};

let start = () => {
  $.ajax({
    url: `/question_count/${groupname}/`,
    success: function (response) {
      localStorage.setItem("question_count", response.question_count);
      localStorage.setItem("click_count", 0);
      $("#start").addClass("disabled");
      $("#next").removeClass("disabled");
      get_question();
    },
  });
};

let get_question = () => {
  let question_count = localStorage.getItem("question_count");
  let click_count = localStorage.getItem("click_count");
  if (click_count <= question_count-1) {
    // console.log("click count",click_count)
    data = { room_name: groupname, q_no: click_count };
    ws.send(JSON.stringify(data));
    click_count++;
    localStorage.setItem("click_count", click_count);
  } else {
    $("#next").addClass("disabled");
    $("#end").removeClass("disabled");
  }
};


let end = () =>{
  alert("Game Over...")
  document.getElementById("quiz_board").innerHTML = (
    "<h1>Menti will start soon be ready...</h1>"
  ); 
  localStorage.removeItem("question_count");
  localStorage.removeItem("click_count");
  $("#end").addClass("disabled");
  $("#start").removeClass("disabled");
}