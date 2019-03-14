#!/usr/bin/env python

import argparse

def traceback(scoringMatrix, seqA, seqB, seqAsize, seqBsize, match, missmatch, gap):
    AlignmentA = ""
    AlignmentB = ""
    i = seqAsize - 1
    j = seqBsize - 1
    while i > 0 and j > 0:
        score = scoringMatrix[i][j]
        valueScoreDiag = 0
        if seqA[i - 1] == seqB[j - 1]:
            valueScoreDiag = match
        else:
            valueScoreDiag = missmatch
        scoreDiag = scoringMatrix[i - 1][j - 1]
        scoreUp = scoringMatrix[i - 1][j]
        scoreLeft = scoringMatrix[i][j - 1]
        #print("Score : " + str(score) + ", Score Diag : " + str(scoreDiag) + ", Score Up :  " + str(scoreUp) + ", Score Left : " + str(scoreLeft))
        if (score == scoreDiag + valueScoreDiag):
            #print("Go diag")
            AlignmentA = seqA[i - 1] + AlignmentA
            AlignmentB = seqB[j - 1] + AlignmentB
            #print(AlignmentA)
            #print(AlignmentB + "\n")
            i -= 1
            j -= 1
        elif (score == scoreLeft + gap):
            #print("Go left")
            AlignmentA = "-" + AlignmentA
            AlignmentB = seqB[j - 1] + AlignmentB
            #print(AlignmentA)
            #print(AlignmentB + "\n")
            j -= 1
        else:
            #print("Go up")
            AlignmentA = seqA[i - 1] + AlignmentA
            AlignmentB = "-" + AlignmentB
            #print(AlignmentA)
            #print(AlignmentB + "\n")
            i -= 1

    while i > 0:
        AlignmentA = seqA[i - 1] + AlignmentA
        AlignmentB = "-" + AlignmentB
        i -= 1

    while j > 0:
        AlignmentA = "-" + AlignmentA
        AlignmentB = seqB[j - 1] + AlignmentB
        j -= 1

    print(scoringMatrix)
    print("\n")
    print("Alignment A: " + AlignmentA)
    print("Alignment B: " + AlignmentB)
    print("Score = " + str(scoringMatrix[seqAsize - 1][seqBsize - 1]))

def fillMatrix(scoringMatrix, seqA, seqB, seqAsize, seqBsize, match, missmatch, gap):
    i = 1
    while i < seqAsize:
        j = 1
        while j < seqBsize:
            scroeDiag = 0;
            if (seqA[i - 1] == seqB[j - 1]):
                scroeDiag = scoringMatrix[i - 1][j - 1] + match
            else:
                scroeDiag = scoringMatrix[i - 1][j - 1] + missmatch

            scroeLeft = scoringMatrix[i][j - 1] + gap
            scroeUp = scoringMatrix[i - 1][j] + gap

            maxScore = max([max([scroeDiag, scroeLeft]), scroeUp]);

            scoringMatrix[i][j] = maxScore;
            j += 1
        i += 1

    traceback(scoringMatrix, seqA, seqB, seqAsize, seqBsize, match, missmatch, gap)

def init(seqA, seqB, match, missmatch, gap):
    print("Sequence A : " + seqA)
    print("Sequence B : " + seqB)
    seqAsize = len(seqA) + 1
    seqBsize = len(seqB) + 1

    scoringMatrix = [[0 for i in range(seqBsize)] for i in range(seqAsize)]
    #Initialization Step
    i = 1
    while i < seqAsize:
        scoringMatrix[i][0] = i * gap
        i += 1

    j = 1
    while j < seqBsize:
        scoringMatrix[0][j] = j * gap
        j += 1

    fillMatrix(scoringMatrix, seqA, seqB, seqAsize, seqBsize, match, missmatch, gap)

parser = argparse.ArgumentParser(description='Performs the sequence alignment on 2 sequences')
parser.add_argument('seqA', type=str, help='Sequence A')
parser.add_argument('seqB', type=str, help='Sequence B')
parser.add_argument('match', type=int, help='Match value')
parser.add_argument('missmatch', type=int, help='MissMatch value')
parser.add_argument('gap', type=int, help='Gap value')
args = parser.parse_args()
init(args.seqA, args.seqB, args.match, args.missmatch, args.gap)
