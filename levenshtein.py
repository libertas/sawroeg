def distance(s, t):
  m, n = len(s), len(t)
  if not (m and n):
    return m or n

  matrix = [[0 for i in range(n+1)] for j in range(m+1)]
  matrix[0] = list(range(n+1))
  for i in range(m+1):
    matrix[i][0] = i

  for i in range(m):
    for j in range(n):
      cost = int(s[i] != t[j])
      matrix[i+1][j+1] = min(
          matrix[i][j+1] + 1, # a.
          matrix[i+1][j] + 1, # b.
          matrix[i][j] + cost # c.
          )

  return matrix[m][n]
