# Referencias

- [nanoGPT — Andrej Karpathy](https://github.com/karpathy/nanogpt): implementación de GPT para entrenar modelos desde cero y ajustar modelos preentrenados. Referencia para estudiar la arquitectura y el ciclo de entrenamiento.

El repositorio externo está en [`nanogpt/`](nanogpt/) como submódulo de Git. El proyecto registra una revisión específica del repositorio.

Para descargar los submódulos después de clonar este proyecto:

```sh
git submodule update --init --recursive
```

## Papers citados por nanoGPT

Copias descargadas el 25 de octubre de 2026. Las referencias corresponden a la revisión `3adf61e154c3fe3fca428ad6bc3818b27a3b8291` del submódulo.

| Paper | Copia local | Fuente | Cita en nanoGPT |
| --- | --- | --- | --- |
| Language Models are Unsupervised Multitask Learners (GPT-2, 2019) | [PDF](gpt-2.pdf) | [OpenAI](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) | [`data/openwebtext/readme.md`](nanogpt/data/openwebtext/readme.md) |
| PaLM: Scaling Language Modeling with Pathways (2022) | [PDF](palm.pdf) | [arXiv:2204.02311](https://arxiv.org/abs/2204.02311) | [`model.py`](nanogpt/model.py) y [`transformer_sizing.ipynb`](nanogpt/transformer_sizing.ipynb) |
| Training Compute-Optimal Large Language Models (Chinchilla, 2022) | [PDF](chinchilla.pdf) | [arXiv:2203.15556](https://arxiv.org/abs/2203.15556) | [`scaling_laws.ipynb`](nanogpt/scaling_laws.ipynb) |

## Papers del video de Karpathy

Video: [Let's build GPT: from scratch, in code, spelled out.](https://www.youtube.com/watch?v=kCc8FmEb1nY). Copias descargadas el 25 de octubre de 2026.

La descripción del video enlaza los papers de Attention y GPT-3, y menciona GPT-2, cuya [copia local](gpt-2.pdf) figura arriba.

| Paper | Copia local | Fuente |
| --- | --- | --- |
| Attention Is All You Need (2017) | [PDF](attention-is-all-you-need.pdf) | [arXiv:1706.03762](https://arxiv.org/abs/1706.03762) |
| Language Models are Few-Shot Learners (GPT-3, 2020) | [PDF](gpt-3.pdf) | [arXiv:2005.14165](https://arxiv.org/abs/2005.14165) |

También se incluyen los papers de las técnicas tratadas en las secciones de LayerNorm (01:32:51) y dropout (01:37:49). Estos enlaces no figuran en la descripción del video.

| Paper | Copia local | Fuente |
| --- | --- | --- |
| Layer Normalization (2016) | [PDF](layer-normalization.pdf) | [arXiv:1607.06450](https://arxiv.org/abs/1607.06450) |
| Dropout: A Simple Way to Prevent Neural Networks from Overfitting (2014) | [PDF](dropout.pdf) | [JMLR](https://jmlr.org/papers/v15/srivastava14a.html) |

La descripción también enlaza el artículo [Introducing ChatGPT](https://openai.com/index/chatgpt/), que es una publicación de blog.
