from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.passives_common import prevent_damage_when
from ptcgo.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES, SpecialConditions


def _asleep_ward(calc, carrier):
    if calc.target is None or calc.target is not carrier:
        return False
    name = CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.ASLEEP]
    return name in (carrier.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])


_sleeping_face = prevent_damage_when(_asleep_ward, attacks_only=True, any_side=True)

card = PokemonCardDef(
    guid="1f868748-8128-5b72-b0b0-bda379a54998",
    key="COL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MimeJr.Name",
    display_name="Mime Jr.",
    searchable_by=["Mime Jr.", "Basic", "MimeJr"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="COL",
    rarity=Rarities.Uncommon,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=439,
    abilities=[
        Ability(
            title="Sweet Sleeping Face",
            game_text="As long as Mime Jr. is Asleep, prevent all damage done to Mime Jr. by attacks.",
            passive=_sleeping_face,
        ),
        Attack(
            title="Sleepy Lost",
            game_text="Put the top card of your opponent's deck in the Lost Zone. Mime Jr. is now Asleep.",
            cost={},
            effect=unimplemented,
        ),
    ],
)