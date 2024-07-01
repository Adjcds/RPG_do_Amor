document.addEventListener("DOMContentLoaded", () => {
    const textElement = document.getElementById('text');
    const buttonsElement = document.getElementById('buttons');
    const heartContainer = document.getElementById('heart-container');
    const heartIcon = document.getElementById('heart-icon');

    const textos = {
        introducao: "Oii!. Vamos começar?!🥰",
        escolhaInicial: "Você acordou com uma mensagem do seu amor, e você fez o seguinte:🤔",
        cafeDaManhaVirtual: "Você ligou e começou a preparar um café da manhã na videochamada. O que você vai preparar?👩🏻‍🍳",
        mensagemRomantica: "Você decide enviar uma mensagem romântica de bom dia. O que você vai escrever?✍🏻",
        panquecas: "Você preparou café da manhã simples, com seu amor via videochamada!",
        torradas: "Você preparou um digno café da manhã, com seu amor via videochamada!",
        poema: `Nosso amor é como uma flor a desabrochar,
                Crescendo forte, sem nunca parar.
                Seus olhos brilham como estrelas no céu,
                Num universo de sonhos onde só existe o mel.
                Seus sorrisos são notas de uma doce canção,
                Que embalam meu coração com pura emoção. 
                Nossas mãos se entrelaçam, formando um laço,
                Numa dança eterna de carinho e abraço.
                Juntos enfrentamos tempestades e vendavais,
                Mas nunca deixamos que abalem nossos ideais.
                Pois o nosso amor é forte e verdadeiro,
                Um elo que nos une, um laço derradeiro.
                Assim, neste Dia dos Namorados, meu bem,
                Quero dizer que você é meu maior alguém.
                Que nossa história de amor seja sempre celebrada,
                Porque ao seu lado, minha vida é uma jornada encantada.`,
        mensagemCurta: "Apesar dos desafios que enfrentamos, cada momento ao seu lado é um lembrete do quanto sou abençoada(o) por ter você na minha vida. Seu amor ilumina até os dias mais sombrios e transforma os momentos simples em memórias preciosas. Você é o meu porto seguro, minha fonte de alegria e inspiração. Em cada batida do meu coração, encontro a certeza de que, com você, estou exatamente onde pertenço. Feliz Dia dos Namorados, meu amor!",
        surpresaNaChamada: "Durante a videochamada, você decide fazer uma surpresa. O que você vai fazer?😱",
        cantarMusica: `Vou te colocar em uma moldura, ah, meu bem, não dá pra te culpar.
                Ainda bem que a sua mãe te fez,
                Está me deixando louco, você é inexplicável, uh.
                Você deve ser um anjo. (Justin Timberlake - Selfish)`,
        presenteVirtual: `☀ Nosso amor é como o sol e a lua, sempre presentes, mesmo quando não estão juntos fisicamente, iluminando e guiando um ao outro em todas as fases da vida ☾ `,
        escolherGame: "Vocês decidem jogar um game juntos. Qual jogo vocês vão escolher?",
        jogoFortnite: "Vocês entram no Fortnite e lutam juntos até o final, mostrando um ao outro suas habilidades incríveis e dançam na cara dos inimigos.",
        jogoValorant: "Vocês jogam Valorant, coordenando estratégias e vencendo partidas juntos como uma dupla imbatível.",
        jogoDeadByDaylight: "Vocês jogam Dead by Daylight, trabalhando juntos para sobreviver e escapar dos perigos!",
        finalFeliz: "Mesmo enfrentando alguns 'game overs', vocês percebem que o amor de vocês é como um jogo infinito, onde cada 'game over' é apenas uma oportunidade para começar de novo, juntos. Juntos, vocês descobrem que o verdadeiro desafio é sempre continuar jogando, não importa o que aconteça. ( - Te amo amor)!"
    };

    const criarBotoes = (botoes) => {
        buttonsElement.innerHTML = '';
        botoes.forEach(botao => {
            const button = document.createElement('button');
            button.textContent = botao.texto;
            button.addEventListener('click', botao.acao);
            buttonsElement.appendChild(button);
        });
    };

    const mostrarTexto = (chave) => {
        textElement.textContent = textos[chave];
    };

    const desenharCoracao = () => {
        heartContainer.style.display = 'block'; 
    };

    const esconderCoracao = () => {
        heartContainer.style.display = 'none'; 
    };

    const introducao = () => {
        mostrarTexto('introducao');
        criarBotoes([
            { texto: 'Começar', acao: escolhaInicial }
        ]);
    };

    const escolhaInicial = () => {
        mostrarTexto('escolhaInicial');
        criarBotoes([
            { texto: 'Preparar um café da manhã juntos em videochamada.', acao: cafeDaManhaVirtual },
            { texto: 'Enviar uma mensagem romântica.', acao: mensagemRomantica },
            { texto: 'Voltar', acao: introducao }
        ]);
    };

    const cafeDaManhaVirtual = () => {
        mostrarTexto('cafeDaManhaVirtual');
        criarBotoes([
            { texto: 'Você preparou algo simples e que gostava, mas depois parou para ficar admirando(a).', acao: panquecas },
            { texto: 'Começou a preparar varias coisas para mostrar suas habilidades, para deixar ele(a) impressionado(a).', acao: torradas },
            { texto: 'Voltar', acao: escolhaInicial }
        ]);
    };

    const mensagemRomantica = () => {
        mostrarTexto('mensagemRomantica');
        criarBotoes([
            { texto: 'Um poema de amor.', acao: poema },
            { texto: 'Uma mensagem curta e doce.', acao: mensagemCurta },
            { texto: 'Voltar', acao: escolhaInicial }
        ]);
    };

    const panquecas = () => {
        mostrarTexto('panquecas');
        criarBotoes([
            { texto: 'Próximo', acao: surpresaNaChamada },
            { texto: 'Voltar', acao: cafeDaManhaVirtual }
        ]);
    };

    const torradas = () => {
        mostrarTexto('torradas');
        criarBotoes([
            { texto: 'Próximo', acao: surpresaNaChamada },
            { texto: 'Voltar', acao: cafeDaManhaVirtual }
        ]);
    };

    const poema = () => {
        mostrarTexto('poema');
        criarBotoes([
            { texto: 'Próximo', acao: cafeDaManhaVirtual },
            { texto: 'Voltar', acao: mensagemRomantica }
        ]);
    };

    const mensagemCurta = () => {
        mostrarTexto('mensagemCurta');
        criarBotoes([
            { texto: 'Próximo', acao: cafeDaManhaVirtual },
            { texto: 'Voltar', acao: mensagemRomantica }
        ]);
    };

    const surpresaNaChamada = () => {
        mostrarTexto('surpresaNaChamada');
        criarBotoes([
            { texto: 'Cantar uma música especial.', acao: cantarMusica },
            { texto: 'Mostrar um presente virtual que você criou.', acao: presenteVirtual },
            { texto: 'Sugerir jogar um game juntos.', acao: escolherGame },
            { texto: 'Voltar', acao: panquecas }
        ]);
    };

    const cantarMusica = () => {
        mostrarTexto('cantarMusica');
        criarBotoes([
            { texto: 'Próximo', acao: finalFeliz },
            { texto: 'Voltar', acao: surpresaNaChamada }
        ]);
    };

    const presenteVirtual = () => {
        mostrarTexto('presenteVirtual');
        criarBotoes([
            { texto: 'Próximo', acao: finalFeliz },
            { texto: 'Voltar', acao: surpresaNaChamada }
        ]);
    };

    const escolherGame = () => {
        mostrarTexto('escolherGame');
        criarBotoes([
            { texto: 'Fortnite', acao: jogoFortnite },
            { texto: 'Valorant', acao: jogoValorant },
            { texto: 'Dead by Daylight', acao: jogoDeadByDaylight },
            { texto: 'Voltar', acao: surpresaNaChamada }
        ]);
    };

    const jogoFortnite = () => {
        mostrarTexto('jogoFortnite');
        criarBotoes([
            { texto: 'Próximo', acao: finalFeliz },
            { texto: 'Voltar', acao: escolherGame }
        ]);
    };

    const jogoValorant = () => {
        mostrarTexto('jogoValorant');
        criarBotoes([
            { texto: 'Próximo', acao: finalFeliz },
            { texto: 'Voltar', acao: escolherGame }
        ]);
    };

    const jogoDeadByDaylight = () => {
        mostrarTexto('jogoDeadByDaylight');
        criarBotoes([
            { texto: 'Próximo', acao: finalFeliz },
            { texto: 'Voltar', acao: escolherGame }
        ]);
    };

    const finalFeliz = () => {
        mostrarTexto('finalFeliz');
        desenharCoracao();
        criarBotoes([
            { texto: 'Reiniciar', acao: () => {
                introducao();
                esconderCoracao(); 
            }}
        ]);
    };

    introducao();
});
