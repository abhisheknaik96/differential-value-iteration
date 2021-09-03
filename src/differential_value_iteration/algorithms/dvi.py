"""Evaluation and Control implementations of Differential Value Iteration."""

import numpy as np
from absl import logging
from differential_value_iteration.algorithms import algorithm
from differential_value_iteration.environments import structure


class Evaluation(algorithm.Evaluation):
  """Differential Value Iteration for prediction, section 2.1.1 in paper."""
  def __init__(
      self,
      mrp: structure.MarkovRewardProcess,
      initial_values: np.ndarray,
      initial_r_bar: float,
      step_size: float,
      beta: float,
      synchronized: bool):
    self.mrp = mrp
    self.initial_values = initial_values.copy()
    self.initial_r_bar = initial_r_bar
    self.step_size = step_size
    self.beta = beta
    self.index = 0
    self.synchronized = synchronized
    self.reset()

  def reset(self):
    self.current_values = self.initial_values.copy()
    #  Be careful, if initial_r_bar is NumPy array this might not work.
    self.r_bar = self.initial_r_bar

  def diverged(self) -> bool:
    if not np.isfinite(self.current_values).all():
      logging.warn('Current values not finite in DVI.')
      return True
    if not np.isfinite(self.r_bar):
      logging.warn('r_bar not finite in DVI.')
      return True
    return False

  def update(self) -> np.ndarray:
    if self.synchronized:
      return self.update_sync()
    return self.update_async()

  def update_sync(self):
    changes = self.mrp.rewards - self.r_bar + np.dot(self.mrp.transitions,
                                                     self.current_values) - self.current_values
    self.current_values += self.step_size * changes
    self.r_bar += self.beta * np.sum(changes)
    return changes

  def update_async(self):
    change = self.mrp.rewards[self.index] - self.r_bar + np.dot(
        self.mrp.transitions[self.index],
        self.current_values) - self.current_values[self.index]
    self.current_values[self.index] += self.step_size * change
    self.r_bar += self.beta * change
    self.index = (self.index + 1) % self.mrp.num_states
    return change