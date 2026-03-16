from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        nome = request.form.get('nome')
        nome2 = request.form.get('nome2')
        
        if nome2 != "nicolas":
            return f"""
            <style>
                body {{
                    background-color: #001a4d;
                    color: white;
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }}
                .container {{
                    background-color: #cc0000;
                    padding: 30px;
                    border-radius: 10px;
                    box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
                    text-align: center;
                }}
                a {{
                    color: #ffff99;
                    text-decoration: none;
                    margin-top: 20px;
                    display: inline-block;
                }}
            </style>
            <div class="container">
                <h1>Senha incorreta!</h1>
                <p>Tente novamente</p>
                <a href="/">← Voltar</a>
            </div>
            """
        
        return f"""
        <style>
            body {{
                background: linear-gradient(135deg, #001a4d 0%, #003d99 50%, #001a4d 100%);
                background-attachment: fixed;
                color: white;
                font-family: Arial, sans-serif;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                margin: 0;
                position: relative;
                overflow-x: hidden;
            }}
            body::before {{
                content: '';
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: 
                    radial-gradient(circle at 20% 50%, rgba(0, 100, 200, 0.1) 0%, transparent 50%),
                    radial-gradient(circle at 80% 80%, rgba(0, 150, 255, 0.1) 0%, transparent 50%);
                pointer-events: none;
                z-index: 0;
            }}
            .container {{
                background-color: #003d99;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
                text-align: center;
                position: relative;
                z-index: 1;
                margin: 20px 0;
            }}
            .game-container {{
                background-color: #003d99;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
                position: relative;
                z-index: 1;
                margin: 20px 0;
            }}
            canvas {{
                border: 3px solid white;
                display: block;
                background-color: #87CEEB;
                margin: 10px auto;
            }}
            .game-info {{
                color: white;
                font-size: 1.1em;
                font-weight: bold;
            }}
            a {{
                color: #66b3ff;
                text-decoration: none;
                margin-top: 20px;
                display: inline-block;
            }}
            a:hover {{
                color: #99ccff;
            }}
            .welcome-message {{
                text-align: center;
                margin-top: 20px;
                font-size: 1.2em;
                position: relative;
                z-index: 1;
                color: white;
                font-weight: bold;
            }}
            .welcome-message .highlight {{
                color: red;
                -webkit-text-stroke: 1px black;
                text-stroke: 1px black;
            }}
        </style>
        <div class="container">
            <h1>Olá {nome}!</h1>
            <p>Senha correta! Bem-vindo ao jogo!</p>
        </div>
        <div class="game-container">
            <div class="game-info">
                <div style="font-size: 1.5em; margin-bottom: 10px;">
                    🍕 PLACAR: <span id="score">0</span> pontos
                </div>
                <div style="margin-top: 10px; font-size: 0.9em;">Use SETAS para mover e ESPAÇO para pular</div>
            </div>
            <canvas id="gameCanvas" width="600" height="400"></canvas>
        </div>
        <div class="welcome-message">
            Nois exclui ele, Nois odeia ele, bem vindo pessoal do <span class="highlight">Sem Ele</span>
        </div>
        <a href="/">← Voltar</a>
        
        <script>
            const canvas = document.getElementById('gameCanvas');
            const ctx = canvas.getContext('2d');
            
            // Player
            const player = {{
                x: 50,
                y: canvas.height - 60,
                width: 30,
                height: 40,
                velocityY: 0,
                velocityX: 0,
                jumping: false,
                speed: 5,
                jumpPower: -12,
                gravity: 0.4
            }};
            
            // Game variables
            let score = 0;
            let gameOver = false;
            let foods = [];
            let enemies = [];
            
            // Create food (cai de cima)
            function createFood() {{
                foods.push({{
                    x: Math.random() * (canvas.width - 20),
                    y: -20,
                    width: 20,
                    height: 20,
                    velocityY: 2 + score / 50
                }});
            }}
            
            // Create enemies (caem de cima reto)
            function createEnemy() {{
                enemies.push({{
                    x: Math.random() * (canvas.width - 30),
                    y: -30,
                    width: 30,
                    height: 30,
                    velocityX: 0,
                    velocityY: 0.3 + score / 200
                }});
            }}
            
            // Initialize game
            for (let i = 0; i < 2; i++) {{
                createFood();
            }}
            createEnemy();
            
            // Keyboard controls
            const keys = {{}};
            window.addEventListener('keydown', (e) => {{
                keys[e.key] = true;
                if (e.key === ' ' && !player.jumping) {{
                    player.velocityY = player.jumpPower;
                    player.jumping = true;
                }}
            }});
            window.addEventListener('keyup', (e) => {{
                keys[e.key] = false;
            }});
            
            // Update game
            function update() {{
                if (gameOver) return;
                
                // Player movement
                if (keys['ArrowLeft']) player.velocityX = -player.speed;
                else if (keys['ArrowRight']) player.velocityX = player.speed;
                else player.velocityX = 0;
                
                player.x += player.velocityX;
                player.velocityY += player.gravity;
                player.y += player.velocityY;
                
                // Boundaries
                if (player.x < 0) player.x = 0;
                if (player.x + player.width > canvas.width) player.x = canvas.width - player.width;
                
                // Ground collision
                if (player.y + player.height >= canvas.height - 10) {{
                    player.y = canvas.height - player.height - 10;
                    player.velocityY = 0;
                    player.jumping = false;
                }}
                
                // Check food collision
                for (let i = foods.length - 1; i >= 0; i--) {{
                    // Fazer comida cair
                    foods[i].y += foods[i].velocityY;
                    
                    if (player.x < foods[i].x + foods[i].width &&
                        player.x + player.width > foods[i].x &&
                        player.y < foods[i].y + foods[i].height &&
                        player.y + player.height > foods[i].y) {{
                        score += 10;
                        foods.splice(i, 1);
                        createFood();
                        document.getElementById('score').textContent = score;
                    }} else if (foods[i].y > canvas.height) {{
                        foods.splice(i, 1);
                        createFood();
                    }}
                }}
                
                // Update enemies
                for (let enemy of enemies) {{
                    // Legume cai e persegue
                    enemy.y += enemy.velocityY;
                    enemy.velocityY += 0.1; // gravidade
                    
                    // Perseguir o jogador no eixo X
                    if (player.x < enemy.x) {{
                        enemy.velocityX = -2.5;
                    }} else if (player.x > enemy.x) {{
                        enemy.velocityX = 2.5;
                    }}
                    
                    enemy.x += enemy.velocityX;
                    
                    // Bounds
                    if (enemy.x < 0) enemy.x = 0;
                    if (enemy.x + enemy.width > canvas.width) enemy.x = canvas.width - enemy.width;
                    
                    // Check enemy collision
                    if (player.x < enemy.x + enemy.width &&
                        player.x + player.width > enemy.x &&
                        player.y < enemy.y + enemy.height &&
                        player.y + player.height > enemy.y) {{
                        gameOver = true;
                        alert('Game Over! Pontuação final: ' + score);
                    }}
                    
                    // Remover legume se sair da tela
                    if (enemy.y > canvas.height) {{
                        enemies.splice(enemies.indexOf(enemy), 1);
                        createEnemy();
                    }}
                }}
                
                // Spawn aleatório de pizzas e legumes
                if (Math.random() < 0.02) createFood();
                if (Math.random() < 0.005) createEnemy();
            }}
            
            // Draw game
            function draw() {{
                // Clear canvas
                ctx.fillStyle = '#87CEEB';
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                
                // Draw ground
                ctx.fillStyle = '#228B22';
                ctx.fillRect(0, canvas.height - 10, canvas.width, 10);
                
                // Draw player (gordinho)
                ctx.fillStyle = '#FFD700';
                ctx.beginPath();
                ctx.arc(player.x + player.width/2, player.y + player.height/2, 20, 0, Math.PI * 2);
                ctx.fill();
                
                // Draw eyes
                ctx.fillStyle = 'black';
                ctx.beginPath();
                ctx.arc(player.x + player.width/2 - 8, player.y + player.height/2 - 5, 4, 0, Math.PI * 2);
                ctx.fill();
                ctx.beginPath();
                ctx.arc(player.x + player.width/2 + 8, player.y + player.height/2 - 5, 4, 0, Math.PI * 2);
                ctx.fill();
                
                // Draw food (🍕 Pizza melhorada)
                for (let food of foods) {{
                    // Base da pizza (triângulo)
                    ctx.fillStyle = '#CD7F32';
                    ctx.beginPath();
                    ctx.moveTo(food.x + 10, food.y);
                    ctx.lineTo(food.x, food.y + 20);
                    ctx.lineTo(food.x + 20, food.y + 20);
                    ctx.closePath();
                    ctx.fill();
                    
                    // Queijo (amarelo)
                    ctx.fillStyle = '#FFD700';
                    ctx.beginPath();
                    ctx.moveTo(food.x + 10, food.y + 2);
                    ctx.lineTo(food.x + 2, food.y + 18);
                    ctx.lineTo(food.x + 18, food.y + 18);
                    ctx.closePath();
                    ctx.fill();
                    
                    // Pepperoni (círculos vermelhos)
                    ctx.fillStyle = '#FF3333';
                    ctx.beginPath();
                    ctx.arc(food.x + 10, food.y + 8, 2.5, 0, Math.PI * 2);
                    ctx.fill();
                    ctx.beginPath();
                    ctx.arc(food.x + 6, food.y + 14, 2, 0, Math.PI * 2);
                    ctx.fill();
                    ctx.beginPath();
                    ctx.arc(food.x + 14, food.y + 14, 2, 0, Math.PI * 2);
                    ctx.fill();
                    
                    // Sombra do pepperoni
                    ctx.fillStyle = 'rgba(200, 0, 0, 0.3)';
                    ctx.beginPath();
                    ctx.arc(food.x + 10.5, food.y + 8.5, 2.5, 0, Math.PI * 2);
                    ctx.fill();
                }}
                
                // Draw enemies (legumes MUITO mais raivosos e detalhados)
                for (let enemy of enemies) {{
                    // Sombra do legume
                    ctx.fillStyle = 'rgba(0, 0, 0, 0.2)';
                    ctx.beginPath();
                    ctx.ellipse(enemy.x + 15, enemy.y + 32, 18, 4, 0, 0, Math.PI * 2);
                    ctx.fill();
                    
                    // Corpo do legume - formato ondulado (pepino)
                    ctx.fillStyle = '#2d8a2d';
                    ctx.beginPath();
                    ctx.ellipse(enemy.x + 15, enemy.y + 12, 16, 13.5, 0, 0, Math.PI * 2);
                    ctx.fill();
                    
                    // Pele com textura (pequenos picos)
                    ctx.fillStyle = '#1a5a1a';
                    for (let i = 0; i < 12; i++) {{
                        let angle = (i / 12) * Math.PI * 2;
                        let x = enemy.x + 15 + Math.cos(angle) * 16;
                        let y = enemy.y + 12 + Math.sin(angle) * 13.5;
                        ctx.beginPath();
                        ctx.arc(x, y, 2, 0, Math.PI * 2);
                        ctx.fill();
                    }}
                    
                    // Olhos HUGELY raivosos - mais para fora
                    // Branco dos olhos
                    ctx.fillStyle = 'white';
                    ctx.beginPath();
                    ctx.ellipse(enemy.x + 6, enemy.y + 8, 6, 8, -0.3, 0, Math.PI * 2);
                    ctx.fill();
                    ctx.beginPath();
                    ctx.ellipse(enemy.x + 24, enemy.y + 8, 6, 8, 0.3, 0, Math.PI * 2);
                    ctx.fill();
                    
                    // Íris vermelha (bem maior)
                    ctx.fillStyle = '#FF2222';
                    ctx.beginPath();
                    ctx.ellipse(enemy.x + 5.5, enemy.y + 9, 4.5, 6, -0.3, 0, Math.PI * 2);
                    ctx.fill();
                    ctx.beginPath();
                    ctx.ellipse(enemy.x + 24.5, enemy.y + 9, 4.5, 6, 0.3, 0, Math.PI * 2);
                    ctx.fill();
                    
                    // Pupila preta (pequena)
                    ctx.fillStyle = 'black';
                    ctx.beginPath();
                    ctx.arc(enemy.x + 5, enemy.y + 11, 2, 0, Math.PI * 2);
                    ctx.fill();
                    ctx.beginPath();
                    ctx.arc(enemy.x + 25, enemy.y + 11, 2, 0, Math.PI * 2);
                    ctx.fill();
                    
                    // Sobrancelhas MUITO franzidas
                    ctx.strokeStyle = '#cc0000';
                    ctx.lineWidth = 3;
                    ctx.lineCap = 'round';
                    ctx.beginPath();
                    ctx.moveTo(enemy.x + 1, enemy.y + 3);
                    ctx.lineTo(enemy.x + 9, enemy.y);
                    ctx.stroke();
                    ctx.beginPath();
                    ctx.moveTo(enemy.x + 29, enemy.y);
                    ctx.lineTo(enemy.x + 21, enemy.y + 3);
                    ctx.stroke();
                    
                    // Boca ENORME e raivosa
                    ctx.strokeStyle = '#cc0000';
                    ctx.lineWidth = 3;
                    ctx.beginPath();
                    ctx.moveTo(enemy.x + 8, enemy.y + 22);
                    ctx.quadraticCurveTo(enemy.x + 15, enemy.y + 26, enemy.x + 22, enemy.y + 22);
                    ctx.stroke();
                    
                    // Dentes
                    ctx.strokeStyle = '#cc0000';
                    ctx.lineWidth = 1.5;
                    for (let i = 0; i < 5; i++) {{
                        ctx.beginPath();
                        ctx.moveTo(enemy.x + 9 + i * 2.5, enemy.y + 22);
                        ctx.lineTo(enemy.x + 9.5 + i * 2.5, enemy.y + 25);
                        ctx.stroke();
                    }}
                    
                    // Linhas de raiva (veias raivosas)
                    ctx.strokeStyle = '#cc0000';
                    ctx.lineWidth = 1;
                    ctx.beginPath();
                    ctx.moveTo(enemy.x + 3, enemy.y + 5);
                    ctx.lineTo(enemy.x + 1, enemy.y + 3);
                    ctx.stroke();
                    ctx.beginPath();
                    ctx.moveTo(enemy.x + 27, enemy.y + 5);
                    ctx.lineTo(enemy.x + 29, enemy.y + 3);
                    ctx.stroke();
                }}
            }}
            
            // Game loop
            function gameLoop() {{
                update();
                draw();
                requestAnimationFrame(gameLoop);
            }}
            
            gameLoop();
        </script>
        """
    
    return """
    <style>
        body {
            background: linear-gradient(135deg, #001a4d 0%, #003d99 50%, #001a4d 100%);
            background-attachment: fixed;
            color: white;
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            padding-top: 50px;
            position: relative;
            overflow-x: hidden;
        }
        body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: 
                radial-gradient(circle at 20% 50%, rgba(0, 100, 200, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 80% 80%, rgba(0, 150, 255, 0.1) 0%, transparent 50%);
            pointer-events: none;
            z-index: 0;
        }
        form {
            position: relative;
            z-index: 1;
        }
        form {
            background-color: #003d99;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
        }
        h1 {
            text-align: center;
            font-size: 4em;
            margin: 0 0 30px 0;
            position: relative;
            z-index: 1;
            background: linear-gradient(45deg, #ff0000, #ff6600, #ffff00, #00ff00, #0099ff, #6600ff, #ff0000);
            background-size: 300% 300%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: gradient 3s ease infinite;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
            -webkit-text-stroke: 1px rgba(0, 0, 0, 0.3);
        }
        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        input {
            display: block;
            margin: 10px 0;
            padding: 10px;
            width: 300px;
            border: none;
            border-radius: 5px;
        }
        .password-field {
            position: relative;
        }
        .dica {
            position: absolute;
            bottom: 45px;
            left: 0;
            background-color: #ffff00;
            color: black;
            padding: 8px 10px;
            border-radius: 5px;
            font-size: 0.9em;
            white-space: nowrap;
            display: none;
            z-index: 1000;
        }
        .password-field:hover .dica {
            display: block;
        }
        .welcome-message {
            text-align: center;
            margin-top: 40px;
            font-size: 1.3em;
            position: relative;
            z-index: 1;
            color: white;
            font-weight: bold;
        }
        .welcome-message .highlight {
            color: red;
            -webkit-text-stroke: 1px black;
            text-stroke: 1px black;
            font-size: 1.2em;
        }
        button {
            background-color: #00a300;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            margin-top: 10px;
            width: 100%;
        }
        button:hover {
            background-color: #00cc00;
        }
    </style>
    <h1>sem ele</h1>
    <form method="POST">
        <input type="text" name="nome" placeholder="Digite seu nome" required>
        <div class="password-field">
            <input type="password" name="nome2" placeholder="Digite a senha" required>
            <div class="dica">quem é melhor que tudo e todos</div>
        </div>
        <button type="submit">Enviar</button>
    </form>
    """

@app.route('/sobre')
def sobre():
    return "Esta é a página sobre o sem ele."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
