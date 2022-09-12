

func bagOfTokensScore(tokens []int, power int) int {
    sort.Ints(tokens)
    out := 0
    scores, i, j := 0, 0, len(tokens) - 1
    for  i <= j && (tokens[i] <= power || scores != 0) {
        if tokens[i] <= power {
            power -= tokens[i]
            scores++
            i++
        } else {
            power += tokens[j]
            scores--
            j--

        }
        if scores > out {
            out = scores
        }
    }

    return out
}