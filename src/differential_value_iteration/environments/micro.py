"""Definitions of Micro MRP and MDPs."""
import numpy as np
from differential_value_iteration.environments import structure


def create_mrp1(dtype: np.dtype) -> structure.MarkovRewardProcess:
  """Creates a cycling 3-state MRP from Sutton's book (Exercise 10.7)
   http://incompleteideas.net/book/RLbook2020.pdf

   Args:
     dtype: Dtype for reward/transition matrices: np.float32/np.float64

   Returns:
     The MRP.
   """
  return structure.MarkovRewardProcess(
      transitions=np.array([
          [0, 1, 0],
          [0, 0, 1],
          [1, 0, 0]
      ], dtype=dtype), rewards=np.array([0, 0, 1], dtype=dtype),
      name=f'mrp1 ({dtype.__name__})')


def create_mrp2(dtype: np.dtype) -> structure.MarkovRewardProcess:
  """Creates a multichain 4-state MRP.

   Args:
     dtype: Dtype for reward/transition matrices: np.float32/np.float64

   Returns:
     The MRP.
   """
  return structure.MarkovRewardProcess(
      transitions=np.array([
          [0, .9, .1, 0],
          [.1, 0, .9, 0],
          [.9, .1, 0, 0],
          [0, 0, 0, 1]], dtype=dtype),
      rewards=np.array([0, 1, 8, 20], dtype=dtype),
      name=f'mrp2 ({dtype.__name__})')


def create_mrp3(dtype: np.dtype) -> structure.MarkovRewardProcess:
  """Creates a unichain 2-state MRP.

   Args:
     dtype: Dtype for reward/transition matrices: np.float32/np.float64

   Returns:
     The MRP.
   """
  return structure.MarkovRewardProcess(
      transitions=np.array([
          [.2, .8],
          [.2, .8]], dtype=dtype),
      rewards=np.array([1, 1], dtype=dtype),
      name=f'mrp3 ({dtype})')


def create_mdp1(dtype: np.dtype) -> structure.MarkovDecisionProcess:
  """Creates a 2-state MDP.
   Args:
     dtype: Dtype for reward/transition matrices: np.float32/np.float64

   Returns:
     The MDP.
   """
  return structure.MarkovDecisionProcess(
      transitions=np.array([
          [[1, 0], [0, 1]],  # first action
          [[0, 1], [1, 0]]  # second action
      ], dtype=dtype),
      rewards=np.array([
          [1, 1],  # first action
          [0, 0]  # second action
      ], dtype=dtype),
      name=f'mdp1 ({dtype})',
  )


def create_mdp2(dtype: np.dtype) -> structure.MarkovDecisionProcess:
  """Creates a 2-state MDP. The 2 states are not communicating.
   Args:
     dtype: Dtype for reward/transition matrices: np.float32/np.float64

   Returns:
     The MDP.
   """
  return structure.MarkovDecisionProcess(
      transitions=np.array([
          [[1, 0], [0, 1]],  # first action
          [[1, 0], [0, 1]]  # second action
      ], dtype=dtype),
      rewards=np.array([
          [1, 1],  # first action
          [0, 2]  # second action
      ], dtype=dtype),
      name=f'mdp2 ({dtype.__name__})',
  )

def create_mdp3(dtype: np.dtype) -> structure.MarkovDecisionProcess:
  """Creates a 3-state MDP.
   Args:
     dtype: Dtype for reward/transition matrices: np.float32/np.float64

   Returns:
     The MDP.
   """
  return structure.MarkovDecisionProcess(
      transitions=np.array([
          [[.5, .25, .25], [.25, .5, .25], [.25, .25, .5]],  # first action
          [[.25, .5, .25], [.25, .25, .5], [.5, .25, .25]],  # second action
      ], dtype=dtype),
      rewards=np.array([
          [1., 2., 3.],  # first action
          [0., 0., 0.]  # second action
      ], dtype=dtype),
      name=f'mdp3 ({dtype})',
  )

def create_mdp4(dtype: np.dtype) -> structure.MarkovDecisionProcess:
  """Creates a 4-state MDP, maybe a MDVI Control 1 counter example.
   Args:
     dtype: Dtype for reward/transition matrices: np.float32/np.float64

   Returns:
     The MDP.
   """
  return structure.MarkovDecisionProcess(
        transitions=np.array([
            # First Action (continue)
            [[0.5, 0.5, 0.,  0.,  0.,  0.,   0., ],
             [0.5, 0.5, 0.,  0.,  0.,  0.,   0., ],
             [0.5, 0.,  0.,  0.5, 0.,  0.,   0., ],
             [0.5, 0.,  0.,  0.5, 0.,  0.,   0., ],
             [0.,  0.,  0.5, 0.,  0.,  0.5,  0., ],
             [0.,  0.,  0.5, 0.,  0.,  0.5,  0., ],
             [0.,  0.,  0.,  0.,  0.5, 0.,   0.5,]],
            # Second Action (admit)
            [[0.5, 0.5, 0.,  0.,  0.,  0.,   0., ],
             [0.5, 0.,  0.,  0.5, 0.,  0.,   0., ],
             [0.5, 0.,  0.,  0.5, 0.,  0.,   0., ],
             [0.,  0.,  0.5, 0.,  0.,  0.5,  0., ],
             [0.,  0.,  0.5, 0.,  0.,  0.5,  0., ],
             [0.,  0.,  0.,  0.,  0.5, 0.,   0.5,],
             [0.,  0.,  0.,  0.,  0.5,  0.,  0.5,]],
            ], dtype=dtype),
        rewards=np.array([
            [ 0.,  0., -1., -1., -2., -2.,  -3.],  # first action (continue)
            [-1.,  9., -2.,  8., -3.,  7.,  -4.]  # second action (admit)
        ], dtype=dtype),
        name=f'mdp4 ({dtype})',
    )
