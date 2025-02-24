const WebSocket = require('ws')
var os = require('os');
var pty = require('node-pty');

const wss1 = new WebSocket.Server({ port: 6061 })

console.log("Socket is up and running...")

var shell = os.platform() === 'win32' ? 'powershell.exe' : 'bash';
var ptyProcess = pty.spawn(shell, [], {
    name: 'xterm-color',
    //   cwd: process.env.HOME,
    env: process.env,
});
wss1.on('connection', ws => {
    console.log("new session")

    // Catch incoming request
    ws.on('message', command => {
        var processedCommand = commandProcessor(command)
        // console.log(processedCommand, "incoming command");
        ptyProcess.write(processedCommand);
    })

    // Output: Sent to the frontend
    ptyProcess.on('data', function (rawOutput) {
        var processedOutput = outputProcessor(rawOutput);
        ws.send(processedOutput);
        console.log(processedOutput);

    });
})

const commandProcessor = function(command) {
    return command;
}

const outputProcessor = function(output) {
    return output;
}
