#!/usr/bin/env python

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import torch
from torch.jit import script, trace
import torch.nn as nn
from torch import optim
import torch.nn.functional as F
import csv
import random
import re
import os
import unicodedata
import codecs
from io import open
import itertools
import math
from parse_transcript import *
from load_data import *
from model import *

USE_CUDA = torch.cuda.is_available()
device = torch.device("cuda" if USE_CUDA else "cpu")

#Generate Transcripts

#Parse Transcript
FIELDS = ["characterID", "text"]
filename = os.path.join("compiled_transcripts.txt")

corpus_name = filename





hidden_size = 256
#encoder1 = EncoderRNN(voc.num_words, hidden_size).to(device)
#attn_decoder1 = AttnDecoderRNN(hidden_size, voc.num_words, dropout_p=0.1).to(device)

trainIters(encoder1, attn_decoder1, 20000, print_every=2500)
'''
output_words, attentions = evaluate(
    encoder1, attn_decoder1, "good morning")
print('output =', ' '.join(output_words))
'''
