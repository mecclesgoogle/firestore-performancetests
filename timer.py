import time

class Timer:
  def __init__(self, func=time.perf_counter) -> None:
    self.elapsed = 0.0
    self._func = func
    self._start = None
    self.stages = []

  def start(self):
    if self._start is not None:
      raise RuntimeError('Already started')
    self._start = self._func()

  def stop(self):
    if self._start is None:
      raise RuntimeError('Not started')
    end = self._func()
    self.elapsed += end - self._start
    self.stages.append(end - self._start)
    self._start = None
  
  def reset(self):
    self.elapsed = 0.0
    self.stages = []

  @property
  def running(self):
    return self._start is not None

  def __enter__(self):
    self.start()
    return self

  def __exit__(self, *args):
    self.stop()