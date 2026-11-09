O app.py.
A variável livros.
Lista (list).
Dicionário (dict).
A rota /, da função inicio().
Abre o arquivo inicio.html da pasta templates e mostra a página no navegador.

O pedido do navegador ao acessar /livros.
Pega a lista livros e envia para o livros.html.
Uma página com a lista de livros, a disponibilidade e o link de detalhes.
No app.py, quando a função da rota roda, antes de a página ser enviada.
No arquivo HTML, na hora de montar a página, para repetir o bloco de cada livro.
livros[0] é o livro inteiro (o dicionário). livro["titulo"] é só o título.
Para pegar o número da URL como inteiro e comparar com o id do livro.
Que a página ou o livro não foi encontrado.
Porque a variável começa como None, e se nenhum id for igual ao da URL, ela continua assim.
O template não receberia a lista, então a página abriria sem nenhum livro.
