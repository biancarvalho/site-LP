# TINDEMAP
Esse projeto consiste em um site para encontrar quais dos seus colegas da EMAp possuem interesses em comum com você. O interessante é que você não descobrirá quem são essas pessoas, pois elas serão anônimas com codinomes de animais.
Criado para o curso de Linguagens de Programação da EMAp, o propósito deste trabalho é divertir e promover a integração entre os estudantes da EMAp.

## Integrantes
- Bianca Dias de Carvalho - B43663 - 211708009

- Cristiano Júnior Larréa Leal - B43645 - 211708005

- Daniel Jacob Tonn - B43897 - 211704030

- Raul Lomonte Figueiredo - B44399 - 211708043

- Sylvio Jorge Pastene Helt - B43013 - 211708011

## Estrutura
Abaixo segue uma breve descrição de cada folder encontrado na raiz do projeto.

### bootstrap
Nessa pasta encontra-se o source file do Bootstrap 5, de forma que possa ser usado com o SASS.

### main.scss
Esse é o principal arquivo de estilo utilizado no projeto. A extensão escolhida foi .scss e não .sass para ser mais fácil a integração com o framework Bootstrap 5, visto que este já possui diversos arquivos (como módulos e mixins) nativos que podem ser utilizados.

### css
Nessa pasta encontra-se o arquivo .css referenciado no href do html. Esse arquivo é obtido através da execução do comando
```sass --watch main.scss:css/custom.css```
após a instalação local do SASS.

### img
Nessa pasta, localizam-se todas as imagens referentes ao projeto.

### html
Nessa pasta, encontram-se todas as páginas HTML desenvolvidas pelo grupo.

## Processo de Desenvolvimento
O processo aconteceu com o desenvolvimento de páginas HTML estilizadas por todos integrantes do grupo. Todas as páginas e o arquivo .css foi validado através do site https://validator.w3.org/.

### Testes de Acessibilidade
Afim de seguir o padrão WCAG para o nível AAA, o grupo utilizou a ferramente WAVE para fazer a varredura dos HTML's e encontrar possíveis erros para corrigí-los.

## Fluxo 
A sequência de páginas perguntas com perguntas é acessível após o botão de realizar cadastro.