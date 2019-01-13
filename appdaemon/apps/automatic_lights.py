from appdaemon.plugins.hass import hassapi as hass
import globals

# Config:
#   when_this: binary sensor to use as trigger
#   turn_on : anything that can be turned on
#   delay: wait this many seconds (optional, default: 60)
#   turn_off : anything that can be turned off
class BinaryTriggeredDelayedOffSwitch(hass.Hass):
  def initialize(self):
    
    self.handle = None
    
    # Subscribe to state changes on input trigger entity
    if "when_this" in self.args:
      self.listen_state(self.state_change_handler, self.args["when_this"])
    else:
      self.log("No binary_sensor provided")
    
  def state_change_handler(self, entity, attribute, old, new, kwargs):
    if new == "on":
      if "turn_on" in self.args:
        self.log("Binary sensor triggered: turning {} on".format(self.args["turn_on"]))
        self.turn_on(self.args["turn_on"])
      if "delay" in self.args:
        delay = self.args["delay"]
      else:
        delay = 60
      # Cancel last one if retriggered during the delay time
      self.cancel_timer(self.handle)
      # Setup the turn_off callback
      self.handle = self.run_in(self.turn_off_callback, delay)
  
  def turn_off_callback(self, kwargs):
    if "turn_off" in self.args:
        self.log("Turning {} off".format(self.args["turn_off"]))
        self.turn_off(self.args["turn_off"])
        
  def cancel(self):
    self.cancel_timer(self.handle)
