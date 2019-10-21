# The Salvinator 🤖

Abbiamo scaricato più di 30.000 tweets di Matteo Salvini per insegnare ad un intelligenza artificiale a twittare come lui. Qua trovate il codice, i modelli già allenati e il dataset (tutti i suoi tweets).

Potete provare una demo di tweets pre-generati [qui](https://editor.p5js.org/banano/full/w4cW8FKYY).

Per generare nuovi tweets senza installare nulla potete seguire le istruzioni in questo [Colab notebook](https://colab.research.google.com/drive/199Clx5klRbYxKPCu7obZkrSYQdQd6g5M) (Chrome only).

## Tweets originali

Nella cartella ``data`` si trovano tutti i tweets dell'account [@matteosalvinimi](https://twitter.com/matteosalvinimi) dall'inizio del suo account fino ad inizio Ottobre 2019.

I files sono in JSON e CSV.
(CSV è una tabella e può  anche essere aperto da Excel o simili.)

Per fare lo scraping è stato utilizzato [questo script](https://github.com/bpb27/twitter_scraping).

## Machine learning

Per generare tweets di Salvini sono stati utilizzati due modelli diversi di machine learning: [LSTM](https://en.wikipedia.org/wiki/Long_short-term_memory) e [GPT-2](https://openai.com/blog/better-language-models/). 

LSTM è più snello e si può utilizzare in un website, ma è molto meno accurato. 
GPT-2 è molto accurato, ma è un po' più laborioso da far girare, soprattutto se non si ha un po' di comprensione di base di python. 

Il modello GPT-2 di Salvini inoltre pesa ~500Mb, contro i 3mb di quello LSTM.

GPT-2 è stato allenato con una Nvidia K80 GPU per circa 8 ore, utilizzando Google Colab, mentre LSTM per un paio d'ore, sempre con K80 / Google Colab

GPT-2 è stato utilizzato per pre-generare i tweets di questa [pagina](https://editor.p5js.org/banano/full/w4cW8FKYY).

### LSTM
Nella cartella ``models/LSTM`` si trova il modello compresso compatibile con [ml5.js](http://ml5js.org). È stato allenato seguendo le istruzioni in [questa repo](https://github.com/ml5js/training-lstm). 

Il modello LSTM può generalmente essere utilizzato con le implementazioni di [charRNN](http://karpathy.github.io/2015/05/21/rnn-effectiveness/), un algoritmo del 2015 di Andrej Karpathy.

### GPT-2

Il modello da utilizzare con GPT-2 lo potete scaricare [qui](https://transfer.sh/k7gSC/run1.tar.xz), pesa circa 500Mb.

Per allenare il modello è stato utilizzato questo [Colab Notebook](https://colab.research.google.com/drive/1VLG8e7YSEwypxU-noRNhsv5dW4NfTGce#scrollTo=H7LoMj4GA4n_), utilizzando il modello minore (124M) e learning rate 1e-4. 
Al momento, dopo circa 8 ore di training siamo arrivati ad una loss di 1.42.

*SI POTREBBE FARE DI MEGLIO. #dimartedi*

Probabilmente rifacendo il training con i modelli più grandi si potrebbero ottenere risultati piu accurati, ma abbiamo anche altro da fare nella vita.

## Generare nuovi tweets

### LSTM 
(*meno accurato ma piu semplice da implementare*)

Per far girare LSTM in locale si può utilizzare lo sketch [charRNN](https://ml5js.org/reference/api-charRNN/) di ml5.js, sostituendo il modello di esempio con quello di Salvini, che si trova nella cartella ``models/LSTM/salvini``

Se avete clonato la repo basta che facciate partire un server nella cartella ``esempi/charRNN``

Per far partire un server su OSX, aprite il terminale:

``` 
cd [path della cartella] 
python -m SimpleHTTPServer 
```

### GPT-2
Nella cartella ```esempi/gpt2``` c'è una cartella ```salvinator``` che contiene un semplicissimo front-end che pesca un tweet a random da un .txt pre-generato nella stessa cartella. Lanciate un server in locale in quella cartella, oppure usatelo online [qui](https://editor.p5js.org/banano/full/w4cW8FKYY).

Nella cartella ```gpt2salvini``` si trova invece il programma in python per generare nuovi tweets.

Per prima cosa si deve scaricare il modello allemato sui tweets di Salvini.
In OSX basta andare dal terminale nella cartella ```gpt2salvini``` e far partire:
```
curl -SL https://transfer.sh/k7gSC/run1.tar.xz | tar -xf - -C checkpoint
```

Per far girare in locale il modello serve python3; per semplificare il processo si può creare un nuovo virtual environment.

```
//se non avete virtualenv installato:
pip install virtualenv

//poi dentro la folder esempi/gpt2
virtualenv venv

source venv/bin/activate
```

dopodichè installiamo [gpt-2-simple](https://github.com/minimaxir/gpt-2-simple) e tensorflow 1.14:

```
pip3 install gpt-2-simple
pip3 install tensorflow==1.14
```

per generare nuovi tweets lanciate l'esempio:
```
python3 main.py
```

Se lo lanciate la prima volta eseguite anche le due linee per scaricare i modelli (basta farlo solo una volta, poi potete commentarle).

In un paio di minuti dovrebbe generare una serie di tweets, in base ai parametri spiegati nel codice. 

Per cambiare i parametri tipo numero di tweets, tempratura, etc. seguite le istruzioni sulla pagina di [gpt-2-simple](https://github.com/minimaxir/gpt-2-simple).

## Licenza

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.





