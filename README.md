# TabIt
A machine learning program that converts music audio into guitar tabs

## Status
[![Build Status](https://github.com/samuelflock/TabIt/actions/workflows/python_build_and_test.yml/badge.svg)](https://github.com/samuelflock/TabIt/actions/workflows/python_build_and_test.yml)

## Usage
Using the terminal run the command: `python TabIt`

You may include `-h` for help to learn the different flags and required arguments.


## Available Demucs Models
The list of pre-trained models is:
- `htdemucs`: first version of Hybrid Transformer Demucs. Trained on MusDB + 800 songs. Default model.
- `htdemucs_ft`: fine-tuned version of `htdemucs`, separation will take 4 times more time
    but might be a bit better. Same training set as `htdemucs`.
- `htdemucs_6s`: 6 sources version of `htdemucs`, with `piano` and `guitar` being added as sources.
    Note that the `piano` source is not working great at the moment.
- `hdemucs_mmi`: Hybrid Demucs v3, retrained on MusDB + 800 songs.
- `mdx`: trained only on MusDB HQ, winning model on track A at the [MDX][mdx] challenge.
- `mdx_extra`: trained with extra training data (**including MusDB test set**), ranked 2nd on the track B
    of the [MDX][mdx] challenge.
- `mdx_q`, `mdx_extra_q`: quantized version of the previous models. Smaller download and storage
    but quality can be slightly worse.
- `SIG`: where `SIG` is a single model from the [model zoo](docs/training.md#model-zoo).