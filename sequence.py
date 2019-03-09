#!/usr/bin/env python

import argparse

def traceback(scoringMatrix, seqA, seqB, seqAsize, seqBsize):
    AlignmentA = ""
    AlignmentB = ""
    i = seqAsize - 1
    j = seqBsize - 1
    while i > 0 and j > 0:
        score = scoringMatrix[i][j]
        valueScoreDiag = 0
        if seqA[i - 1] == seqB[j - 1]:
            valueScoreDiag = 4
        else:
            valueScoreDiag = -3
        scoreDiag = scoringMatrix[i - 1][j - 1]
        scoreUp = scoringMatrix[i - 1][j]
        scoreLeft = scoringMatrix[i][j - 1]
        print("Score : " + str(score) + ", Score Diag : " + str(scoreDiag) + ", Score Up :  " + str(scoreUp) + ", Score Left : " + str(scoreLeft))
        if (score == scoreDiag + valueScoreDiag):
            print("Go diag")
            AlignmentA = seqA[i - 1] + AlignmentA
            AlignmentB = seqB[j - 1] + AlignmentB
            print(AlignmentA)
            print(AlignmentB + "\n")
            i -= 1
            j -= 1
        elif (score == scoreLeft - 2):
            print("Go left")
            AlignmentA = "-" + AlignmentA
            AlignmentB = seqB[j - 1] + AlignmentB
            print(AlignmentA)
            print(AlignmentB + "\n")
            j -= 1
        else:
            print("Go up")
            AlignmentA = seqA[i - 1] + AlignmentA
            AlignmentB = "-" + AlignmentB
            print(AlignmentA)
            print(AlignmentB + "\n")
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
    print(AlignmentA)
    print(AlignmentB)

def fillMatrix(scoringMatrix, seqA, seqB, seqAsize, seqBsize):
    i = 1
    while i < seqAsize:
        j = 1
        while j < seqBsize:
            scroeDiag = 0;
            if (seqA[i - 1] == seqB[j - 1]):
                scroeDiag = scoringMatrix[i - 1][j - 1] + 4
            else:
                scroeDiag = scoringMatrix[i - 1][j - 1] + -3

            scroeLeft = scoringMatrix[i][j - 1] - 2
            scroeUp = scoringMatrix[i - 1][j] - 2

            maxScore = max([max([scroeDiag, scroeLeft]), scroeUp]);

            scoringMatrix[i][j] = maxScore;
            j += 1
        i += 1

    traceback(scoringMatrix, seqA, seqB, seqAsize, seqBsize)

def init(seqA, seqB):
    print("Sequence A : " + seqA)
    print("Sequence B : " + seqB)
    seqAsize = len(seqA) + 1
    seqBsize = len(seqB) + 1

    scoringMatrix = [[0 for i in range(seqBsize)] for i in range(seqAsize)]
    #Initialization Step
    i = 1
    while i < seqAsize:
        scoringMatrix[i][0] = i * -2
        i += 1

    j = 1
    while j < seqBsize:
        scoringMatrix[0][j] = j * -2
        j += 1

    fillMatrix(scoringMatrix, seqA, seqB, seqAsize, seqBsize)

parser = argparse.ArgumentParser(description='Performs the sequence alignment on 2 sequences')
parser.add_argument('seqA', type=str, help='Sequence A')
parser.add_argument('seqB', type=str, help='Sequence B')
args = parser.parse_args()
init(args.seqA, args.seqB)
