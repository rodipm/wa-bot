function SendMessage(message) {
  // Select the input div
  let messageInput = document
    .getElementsByClassName("_3u328 copyable-text selectable-text")
    .item(0);

  // Change its text
  messageInput.textContent = message;

  // Force Input Event
  let event = document.createEvent("UIEvents");
  event.initUIEvent("input", true, true, window, 1);
  messageInput.dispatchEvent(event);

  // Select the send button
  let sendButton = document.getElementsByClassName("_3M-N-").item(0);
  sendButton.click();
}

function DetectMessages(callback) {
  let lastLength = document.getElementsByClassName(
    "selectable-text invisible-space copyable-text"
  ).length;

  setInterval(() => {
    let messages = document.getElementsByClassName(
      "selectable-text invisible-space copyable-text"
    );
    let currentLength = messages.length;
    if (currentLength > lastLength) {
      lastLength = currentLength + 1;
      let message = messages.item(currentLength - 1).innerHTML;
      callback(message);
    }
  }, 500);
}

DetectMessages(message => {
  SendMessage(message);
});

function selectChat() {
  let event = document.createEvent("MouseEvents");
  event.initMouseEvent(
    "click",
    true,
    true,
    window,
    0,
    0,
    0,
    0,
    0,
    false,
    false,
    false,
    false,
    0,
    null
  );
  temp2.dispatchEvent(event);
}
selectChat();
