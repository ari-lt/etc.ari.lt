"use strict";

function log(msg) {
    let data = document.createElement("h3");
    data.innerText = msg;

    document.body.appendChild(data);
}

function main() {
    let peer = new Peer();

    let your_id = document.getElementById("your-id");
    let send = document.getElementById("send");

    peer.on("open", (id) => {
        your_id.innerText = `Your ID: ${id}`;
    });

    peer.on("connection", (conn) => {
        conn.on("data", (data) => {
            log(`[peer] Recieved data from ${conn.peer}: ${data}`);
            conn.send(`Got your message, ${conn.peer}: ${data}`);
        });

        conn.on("open", () => log(`[peer] Connected to ${conn.peer}`));
    });

    send.addEventListener("click", () => {
        let conn = peer.connect(prompt("ID"));

        conn.on("data", (data) => {
            log(`[send] Recieved data back from ${conn.peer}: ${data}`);
        });

        conn.on("open", () => {
            log(`[send] Connected to ${conn.peer}`);
            conn.send(prompt(`What to send to ${conn.peer}`));
        });
    });
}

document.addEventListener("DOMContentLoaded", main);
