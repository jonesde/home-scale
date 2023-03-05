
## Home-Scale 3D Printer Requirements

- operating environment scale: tabletop to full garage
- fully 3D printable, independently sourceable
  - this is a long term requirement, not likely viable with microprocessors for a long time
  - various components will initially be Commercial Off-The-Shelf (COTS) for an easier minimum viable product
  - being home-scale in terms of technology that is economically available is more important than the eventual goal of being fully independently sourceable, the reason for the 3D printable goal 
  - many initial designs may come from other open projects like Prusa and Voron
- support multiple materials
  - metals, polymers, ceramics, etc
- support multiple heads
  - for throughput and to support multiple materials
  - different materials may have different head requirements
  - consider multiple head mounts or a docking area for heads and a motorized head mount
    - head already needs to be able to position itself precisely
    - docking area for heads would reduce operating space by the amount that cannot extend beyond it
- TODO

## Open Source Printer Design

- initially use VORON designs
  - newer design, sturdier, more flexible, better results than Prusa
  - pricy kit
    - LDO VORON 2.4 R2 CoreXY Self-Assembly 3D Printer Kit
    - https://www.matterhackers.com/store/l/voron-design-corexy-fdm-3d-printer/sk/MRL60G0L
  - LDO VORON Kit other sources https://docs.ldomotors.com/voron/LDO_Voron_Distributors
  - open design
    - model overview: https://docs.vorondesign.com/hardware.html
    - https://vorondesign.com/voron2.4
- runner up: RatRig V-Core
  - might be more flexible for heavier head, uses 4-corner lifting bed design so head has no Z motion
  - https://v-core.ratrig.com/
- initial deliverables are mods to existing printer
  - includes EM-CSAM print head, controller, 3D scanner, base plate (polymer won't cut it), etc
  - with the mod of existing open source approach there is much less initial work, and VORON frame and enclosure with some mods may be adequate for EM-CSAM
- how far will that get? we'll find out...
- current designs have huge limits in being 3D printable, science and technology exists to improve that

## Other Open Source Designs

RepRap Big List https://reprap.org/wiki/RepRap_Options 

X-SCARA with stable arm design https://github.com/madl3x/x-scara


## Main Printer Components

### control computer

  - 3D printable? one day...
  - for probably quite a while this is a COTS component (commercial off-the-shelf)

### print control 3D scanner

- for highly precise iterative deposition, very helpful for CSAM, if good compensates a lot for limited print resolution
- guessing how the material splatted is not likely to yield good results, and the control accuracy possible with EM-CSAM is totally unknown
- EM-CSAM might not even be viable for anything but crude parts without a good 3D scanner
- very close range possible, mounted to print head
- with all that can be done in 3D printed sensors this may be possible at a close range, maybe even with something simple to print sensors for like capacitive effect (as in a touch screen where your finger doesn't have to touch to be sensed)
- if possible to 3D print with good materials, even a basic one would be a huge improvement over nothing
- highly sensitive COTS available
  - offering simple single 'pixel' to arrays for detailed 3D scanning
  - using light, sound, EM waves, etc
  - possibly one simple/cheap micro lidar sensor per barrel to scan ahead (seen down to 7 micrometer tolerance)

### print head power controller

- may not be COTS available, but will require COTS components
- not nearly as difficult to fab as a microprocessor, but still a silicon/gallium/etc semiconductor component, 3D printable... eventually
- high frequency PWM might be best for EM-CSAM
- other print heads like FDM have much simpler power requirements for things like resistive heating (but probably use PWM as well instead of voltage regulation because it's so cheap and easy at ~15khz)
- EM-CSAM railguns different from motors: need higher frequencies, lower voltages, but amperage levels cheaply available are good

### 3 axis motion motor controller

- COTS available with rotary motors, and linear coil motors too
- for 3D printable is like the print head power controller, maybe one day

### 3 axis motors

- COTS available, 3D printable possible
- may have 5 motors total for internal auto-leveling (2 instead of 1 on each of the horizontal axes; avoid manual or motorized feet), or 3 without
- rotary motors and gears and such are great for mechanics with readily available mass produced components
- for 3D printing it is not as good, a viable 3D printable motor would be a huge win
- with a rigid frame (instead of an arm) linear motion is all that is needed so linear motors are a good fit, and when 3D printed can be built into the frame
- if the frame itself is not the rail then separate rails are needed, often pairs of round bars for precise control, also difficult to 3D print
- the frame becomes a rail like a maglev train rail, and the other part
- ability to print thin, insulated wires is a problem but maglev acceleration style coils could be viable with printed wires (0.4 mm 26 AWG, perhaps down to 0.2 mm 32 AWG which is pretty good for a motor), should be within reach of common desktop FDM printers
- active coils embedded on one side; possibly in the frame, but will need fewer active coils if they are in the moving part
- permanent magnetic or shaped conductive material in the other part; opposing coils can also be used, but it is nice to avoid additional components, wires, and controllers
- has similar power needs to the EM-CSAM railguns, PWM controllable, but runs at higher voltages like normal motors with much longer conductive loop than parallel rails
- will need a rail brake
  - automatically engaged between movements for stability, especially the vertical motor(s)
  - on horizontal motors use small fast brake, on vertical will need a bigger brake and can be slower (vertical movements are infrequent)
- commercial high-precision linear motors are available
  - proof of viability
  - are many around this one has a nice T shaped groove design, with slicker plastics even need bearings/rollers?
  - https://motioncontrolsystems.hiwin.us/viewitems/linear-motors/linear-motors-lmc-series

### 3 axis head motion frame

- definitely 3D printable, in current open source designs many opt for COTS or have both printable and COTS 
- needs to be rigid, preferably light
- easy to level, with 2 motors on each horizontal axis intead of 1 or with feet (manual or motorized)
- preferably a material that does not expand or contract much with temperature change, but with a good scanner as long as the frame does not move or distort quickly versus the printing surface then it doesn't matter, the head does not need to know where it is relative to the frame if it knows precisely where it is relative to the printing surface

### print head

- use flexible mount compatible with FDM and other heads
- for metal and ceramics: home-made EM-CSAM (if viable)
- for plastic perhaps use low-velocity EM-CSAM, but conductive carrier fluid may interfere too much at low speeds, will be interesting to test

### print bed

- temperature controlled
  - 
  - need heating and unlike most may also need cooling, heat builds from CSAM impact even if material not hot


### optional enclosure

  - for sound only (supersonic boom dampening) or sound plus thermal
  - heat resistant, thermal insulated, temperature controlled
  - internal temperature always limited by the internal component with the lowest temperature failure point
  - if high temp enclosure needed, all other internal parts must also be high temp: frame, print head, motors, wires, material, etc

## Minor Components

### fans

- probably fully 3D printable with embedded motor
- COTS options are cheap with huge variety and good performance, lower priority

### frame rail segments

- metal rails of all sorts are easy COTS, but also easy to print (just require a lot of material)
- use a common segment design for building larger frame: 100-200mm segments with T extension or something on one end to slide into groove on other
- may need various frame shapes with different connectors in different places (such as for corners), use variations as needed for specific build because 3D printers are good at that and result can use less material than generic shapes
- keep segment length, and all parts, within around 200mm cube supported on smaller cheap FDM printers (use case buy Ender 3 220x220x250mm for less than $200, maybe add mods, then make a real machine)
