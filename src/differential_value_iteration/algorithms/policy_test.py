"""Tests for basic functioning of Multichain DVI algorithms."""
import functools
import itertools
from typing import Callable

import numpy as np
from absl.testing import absltest
from absl.testing import parameterized
from differential_value_iteration.algorithms import dvi
from differential_value_iteration.algorithms import mdvi
from differential_value_iteration.algorithms import rvi
from differential_value_iteration.environments import garet
from differential_value_iteration.environments import micro
from differential_value_iteration.environments import structure

_GARET1 = functools.partial(garet.create,
                            seed=42,
                            num_states=4,
                            num_actions=4,
                            branching_factor=3)
_GARET2 = functools.partial(garet.create,
                            seed=42,
                            num_states=4,
                            num_actions=20,
                            branching_factor=3)
_GARET3 = functools.partial(garet.create,
                            seed=42,
                            num_states=10,
                            num_actions=2,
                            branching_factor=3)
_GARET_DEBUG = functools.partial(garet.create,
                                 seed=42,
                                 num_states=3,
                                 num_actions=2,
                                 branching_factor=3)


class PolicyTest(parameterized.TestCase):

  @parameterized.parameters(itertools.product(
      (micro.create_mdp1, _GARET1, _GARET2, _GARET3),
      (np.float64, )))
  def test_identical_policies_sync(self,
      mdp_constructor: Callable[[np.dtype], structure.MarkovDecisionProcess],
      dtype: np.dtype):
    environment = mdp_constructor(dtype=dtype)
    rvi_control = rvi.Control(
        mdp=environment,
        step_size=.75,
        initial_values=np.zeros(environment.num_states, dtype=dtype),
        reference_index=0,
        synchronized=True)
    dvi_control = dvi.Control(
        mdp=environment,
        step_size=.1,
        beta=.1,
        initial_r_bar=0.,
        initial_values=np.zeros(environment.num_states, dtype=dtype),
        synchronized=True)
    mdvi_control_1 = mdvi.Control1(
        mdp=environment,
        step_size=.1,
        beta=.1,
        threshold=.01,
        initial_r_bar=0.,
        initial_values=np.zeros(environment.num_states, dtype=dtype),
        synchronized=True)

    for i in range(1000):
      rvi_control.update()
      dvi_control.update()
      mdvi_control_1.update()
    # with self.subTest('rvi vs dvi'):
    #   np.testing.assert_array_equal(rvi_control.greedy_policy(),
    #                                 dvi_control.greedy_policy())
    with self.subTest('rvi vs mdvi1'):
      np.testing.assert_array_equal(rvi_control.greedy_policy(),
                                    mdvi_control_1.greedy_policy())


if __name__ == '__main__':
  absltest.main()
