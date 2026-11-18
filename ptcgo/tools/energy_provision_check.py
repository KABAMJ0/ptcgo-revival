"""Behaviour check for the wired Special Energy provision shapes.

The smoke harness exercises attack/ability effects; energy provision is attributes
plus a passive hook, so it needs its own assertions:

  * Double Colorless / Twin provide two Colorless in one option.
  * Unit and Blend energies offer one of their listed types at a time.
  * Prism Energy offers every type on a Basic and Colorless elsewhere.
  * Multi / Luminous fall back to Colorless once a second Special Energy is attached.

    python -m ptcgo.tools.energy_provision_check
"""
import json
import sys

from ptcgo.game.attributes import AttrID, CardType, PokemonStage, PokemonTypes
from ptcgo.game.scripts.cards import loader


class StubCard:
    """Just enough of a card entity for the passives to read."""

    def __init__(self, attrs=None, entity_id="card"):
        self._attrs = attrs or {}
        self.entity_id = entity_id

    def get_attribute(self, key):
        return self._attrs.get(key)


class StubBoard:
    def __init__(self, attached=()):
        self._attached = list(attached)

    def attached_energies(self, pokemon):
        return list(self._attached)


def pokemon(stage=PokemonStage.BASIC):
    return StubCard({AttrID.CARD_TYPE: CardType.POKEMON.value, AttrID.STAGE: stage.value})


def special_energy(entity_id="energy"):
    return StubCard({AttrID.IS_SPECIAL_ENERGY: True}, entity_id=entity_id)


def definition(reference):
    loader.load_all()
    return loader.definitions.get(reference)


def options_of(definition):
    raw = definition.extra_attributes[str(AttrID.ENERGY_INFO.value)]["value"]
    return json.loads(raw)["options"] if isinstance(raw, str) else raw["options"]


FAILS = []


def check(label, condition, detail=""):
    if condition:
        print(f"  PASS  {label}")
    else:
        print(f"  FAIL  {label}  {detail}")
        FAILS.append(label)


def main():
    print("provision options")

    double = definition("BASE1/DoubleColorlessEnergy_96")
    options = options_of(double)
    colorless = PokemonTypes.COLORLESS.value
    check("Double Colorless offers exactly two Colorless",
          options == [[colorless, colorless]], options)

    unit = definition("SM5/UnitEnergyGrassFireWater_137")
    options = options_of(unit)
    unit_types = [[PokemonTypes.GRASS.value], [PokemonTypes.FIRE.value], [PokemonTypes.WATER.value]]
    check("Unit Energy offers one of Grass/Fire/Water",
          sorted(options) == sorted(unit_types), options)

    blend = definition("BW6/BlendEnergyGrassFirePsychicDarkness_117")
    options = options_of(blend)
    check("Blend Energy offers one of four types", len(options) == 4 and all(len(o) == 1 for o in options),
          options)

    prism = definition("BW4/PrismEnergy_93")
    base_options = options_of(prism)
    check("Prism defaults to Colorless", base_options == [[colorless]], base_options)
    on_basic = prism.passive.modify_energy_provided(base_options, special_energy(), pokemon(), StubBoard())
    check("Prism on a Basic offers every type", len(on_basic) == 11, on_basic)
    on_stage2 = prism.passive.modify_energy_provided(
        base_options, special_energy(), pokemon(PokemonStage.STAGE2), StubBoard())
    check("Prism on an Evolution stays Colorless", on_stage2 == [[colorless]], on_stage2)

    multi = definition("DP2/MultiEnergy_118")
    base_options = options_of(multi)
    alone = multi.passive.modify_energy_provided(base_options, special_energy("a"), pokemon(), StubBoard())
    check("Multi alone offers every type", len(alone) == 11, alone)
    crowded = multi.passive.modify_energy_provided(
        base_options, special_energy("a"), pokemon(), StubBoard([special_energy("a"), special_energy("b")]))
    check("Multi beside another Special Energy is Colorless", crowded == [[colorless]], crowded)

    rainbow = definition("ECARD2/RainbowEnergy_144")
    check("Rainbow offers every type and carries an attach rider",
          len(options_of(rainbow)) == 11 and rainbow.on_attach is not None, options_of(rainbow))

    print("\nattach restrictions")
    fighting = StubCard({AttrID.CARD_TYPE: CardType.POKEMON.value,
                         AttrID.STAGE: PokemonStage.BASIC.value,
                         AttrID.POKEMON_TYPES: [PokemonTypes.FIGHTING.value]})
    water = StubCard({AttrID.CARD_TYPE: CardType.POKEMON.value,
                      AttrID.STAGE: PokemonStage.STAGE1.value,
                      AttrID.POKEMON_TYPES: [PokemonTypes.WATER.value]})
    stage2 = StubCard({AttrID.CARD_TYPE: CardType.POKEMON.value,
                       AttrID.STAGE: PokemonStage.STAGE2.value,
                       AttrID.POKEMON_TYPES: [PokemonTypes.COLORLESS.value]})

    strong = definition("XY3/StrongEnergy_104")
    check("Strong Energy takes a Fighting carrier",
          strong.attach_to(fighting) and not strong.attach_to(water), None)

    double_rainbow = definition("EX14/DoubleRainbowEnergy_88")
    check("Double Rainbow refuses a Basic and takes an Evolution",
          not double_rainbow.attach_to(fighting) and double_rainbow.attach_to(stage2), None)

    rapid = definition("SWSH5/RapidStrikeEnergy_140")
    marker_card = next((card for card in loader.cards
                        if "Rapid Strike" in (card.subtypes or [])), None)
    plain_card = next((card for card in loader.cards
                       if card.subtypes == ["Basic"] and (card.pokemon_types if hasattr(card, "pokemon_types") else None)), None)
    if marker_card is not None:
        marked = StubCard({AttrID.CARD_TYPE: CardType.POKEMON.value,
                           AttrID.STAGE: PokemonStage.BASIC.value})
        marked.archetype_id = marker_card.guid
        check("Rapid Strike Energy takes a Rapid Strike carrier", rapid.attach_to(marked), None)
        if plain_card is not None:
            plain = StubCard({AttrID.CARD_TYPE: CardType.POKEMON.value,
                              AttrID.STAGE: PokemonStage.BASIC.value})
            plain.archetype_id = plain_card.guid
            check("Rapid Strike Energy refuses a plain Basic", not rapid.attach_to(plain), None)

    print(f"\n{'FAILURES: ' + ', '.join(FAILS) if FAILS else 'all checks passed'}")
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
