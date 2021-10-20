
import heapq, math, pprint

## -------------------------------------------------------------------------
class BinTree:
  m_L = None
  m_R = None
  m_D = None
  m_F = None

  def __init__( self, d, f ):
    self.m_D = d
    self.m_F= f
  # end def

  def __lt__( self, other ): # <
    if self.m_F == other.m_F:
      return self.m_D < other.m_D
    else:
      return self.m_F < other.m_F
  # end def

  def bin_search( self, v ):
    pass
  # end def

  def leaf_searh( self, v ):
    pass
  # end def

  def __str__( self ):
    r = str( self.m_D ) + ':' + str( self.m_F ) + '\n'
    if not self.m_L is None:
      r += '--L--> ' + str( self.m_L ) + '\n'
    # end if
    if not self.m_R is None:
      r += '--R--> ' + str( self.m_R ) + '\n'
    # end if
    return r
  # end def
  
# end class

## -------------------------------------------------------------------------
def opt_bin_tree_bt( D, P, B, i, j ):
  if B[ i ][ j ] == -1:
    return None
  else:
    r = B[ i ][ j ]
    root = BinTree( D[ r - 1 ], P[ r - 1 ] )
    root.m_L = opt_bin_tree_bt( D, P, B, i, r - 1 )
    root.m_R = opt_bin_tree_bt( D, P, B, r + 1, j )
    return root
# end def

## -------------------------------------------------------------------------
def opt_bin_tree( D, P, Q ):
  M = [ [ 0 for j in range( len( Q ) + 1 ) ] for i in range( len( Q ) + 1 ) ]
  B = [ [ -1 for j in range( len( Q ) + 1 ) ] for i in range( len( Q ) + 1 ) ]

  for i in range( 1, len( Q ) + 1 ):
    M[ i ][ i - 1 ] = Q[ i - 1 ]
  # end for

  for i in range( len( P ), 0, -1 ):
    for j in range( i, len( P ) + 1 ):
      q = math.inf
      b = -1
      for r in range( i, j + 1 ):
        v = 0.0
        for l in range( i, j + 1 ):
          v += P[ l - 1 ]
        # end for
        for l in range( i - 1, j + 1 ):
          v += Q[ l ]
        # end for
        v += M[ i ][ r - 1 ]
        v += M[ r + 1 ][ j ]
        if v < q:
          q = v
          b = r
        # end if
      # end for
      M[ i ][ j ] = q
      B[ i ][ j ] = b
    # end for
  # end for

  return opt_bin_tree_bt( D, P, B, 1, len( P ) )
# end def

## -------------------------------------------------------------------------
def build_huffman( D, P ):
  # Forest build
  forest = []
  for i in range( len( D ) ):
    heapq.heappush( forest, BinTree( D[ i ], P[ i ] ) )
  # end for

  # Tree build
  while len( forest ) > 1:
    t0 = heapq.heappop( forest )
    t1 = heapq.heappop( forest )
    n = BinTree( '', t0.m_F + t1.m_F )
    n.m_L = t0
    n.m_R = t1
    heapq.heappush( forest, n )
  # end while

  return forest[ 0 ]
  
# end def

## -------------------------------------------------------------------------
# D = [ 'a' , 'b', 'c',  'd', 'e' ]
# P = [ 0.15, 0.1, 0.05, 0.10, 0.2 ]
# Q = [ 0.05, 0.1, 0.05, 0.05, 0.05, 0.1 ]

## -- Read file
file_hnd = open( sys.argv[ 1 ], 'r' )
txt = file_hnd.read( ).replace( '\n', ' ' )
file_hnd.close( )

# Split delimiters
delimiters = " ,.!?/&-:;@'...()[]<>\""
"["+"\\".join( delimiters )+"]"
tokens = re.split( "["+"\\".join( delimiters )+"]", txt )

# Remove empty strings
tokens = [ t for t in tokens if len( t ) != 0 ]

# Remove accents and transform to lower-case
tokens = [ ''.join( c for c in unicodedata.normalize( 'NFD', t ) if unicodedata.category( c ) != 'Mn' ).lower( ) for t in tokens ]

# Build histogram
histogram = {}
for t in tokens:
  if t in histogram:
    histogram[ t ][ 0 ] += 1
  else:
    histogram[ t ] = [ 1, 0 ]
  # end if
# end for

# Compute frequencies
for b in histogram:
  histogram[ b ][ 1 ] = float( histogram[ b ][ 0 ] ) / float( len( tokens ) )
# end for
D = sorted( histogram.keys( ) )

# 1. Convertir el histograma en P y Q

opt = opt_bin_tree( D, P, Q )
huf = build_huffman( D, P )

# 2. Comprimir el mensaje usando opt

# 3. Comprimir el mensaje usando huf

# 4. Comparar la calidad de comprension
