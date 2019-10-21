# coding: latin-1

#NON DIMENTICARE DI SCARICARE ANCHE IL MODELLO DI SALVINI:
# naviga col terminale nella folder gpt2salvini e fai partire:
# curl -SL https://transfer.sh/k7gSC/run1.tar.xz | tar -xf - -C checkpoint
# in alternativa scaricalo dal link a mano e decomprimilo nella cartella "checkpoints"

import gpt_2_simple as gpt2  

# DOWNLOAD BASE MODEL

# il modello di base viene salvato nella cartella /models/124M
# basta eseguirlo solo la prima volta, poi queste due linee si possono commentare
# model_name = "124M"
# gpt2.download_gpt2(model_name=model_name) 


sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)

# CON I PARAMETRI
gpt2.generate(sess,
              length=250,
              temperature=0.7,
              prefix="a casa ",
              nsamples=5,
              batch_size=5
              )

# parametri di default
# gpt2.generate(sess)


