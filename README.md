# RadHard
Radiation Hardened Voltage Regulation

Setup inicial de testes em um regulador compensado contra radiação e drifts de temperatura.


O tema central deste trabalho é o desenvolvimento de "Reguladores de tensão lineares para aplicações de baixo ruído em ambientes hostis", uma questão alinhada aos desafios enfrentados em setores críticos, como o aeroespacial e nuclear. Nesses contextos, os sistemas eletrônicos estão frequentemente sujeitos a variações extremas de temperatura e altos níveis de radiação, fatores que podem causar falhas graves, como Efeitos de Evento Único (SEE) e Danos Acumulados de Radiação (TID). Essas condições afetam diretamente o desempenho e a confiabilidade dos circuitos eletrônicos, especialmente em aplicações que exigem alta precisão e baixo ruído.

A escolha pelos reguladores de tensão lineares se justifica por sua capacidade de fornecer uma tensão de saída estável e limpa, essencial para circuitos sensíveis que necessitam de baixo ruído. Embora esses reguladores possam ser menos eficientes do que os modelos chaveados, sua baixa emissão de ruído os torna a opção mais adequada para sistemas de instrumentação e outros dispositivos que requerem alta estabilidade e precisão.

O objetivo deste projeto é desenvolver um regulador linear discreto, capaz de operar de forma eficiente em meio a grandes variações de temperatura e consideráveis níveis de exposição à radiação, evitando que essas condições provoquem alterações na tensão de saída, problema comum em ambientes hostis.

A imagem abaixo é referente a placa principal de regulação de tensão.

![image](https://github.com/user-attachments/assets/e2b72cf6-8983-45f0-b046-af1138b04d5f)


![Data Flow Diagram Whiteboard in Dark Yellow Light Yellow Black Monochromatic Style(1)](https://github.com/user-attachments/assets/883d16f3-e689-430b-ab6b-6cb6f3af1566)

Explicação dos blocos do diagrama: 

* Controle: bloco responsável pelo controle de toda a fonte, controlando a tensão e a corrente e pode desligar a fonte caso condições adversas aconteçam. Ele está localizado no meio da placa. 
* Temperatura: responsável pela medição de temperatura interna da placa. Tem ligação direta ao controle. A direita do bloco de radiação.
* Radiação: responsável pela medição de radiação incidida sobre o dispositivo. Se encontra no canto esquerdo inferior. 
* Referência: como o próprio nome já diz, é uma referência sobre a tensão estável do circuito. Canto superior esquerdo da placa.
* Proteção: protege contra sobretensão, transientes indesejados, proteção contra polaridade reversa e surtos de corrente. Está distribuído por toda a placa.
* Elemento de potência: São os elementos responsáveis por regular a tensão e suportar a maior carga de potência indesejado. Localizado na parte de trás da placa.
  

![image](https://github.com/user-attachments/assets/c19b874c-f62a-4827-9e94-80df92e2e3cd)
