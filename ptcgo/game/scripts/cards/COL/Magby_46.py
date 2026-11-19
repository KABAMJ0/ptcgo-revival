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
    guid="5c6bdbb5-7ef6-5861-8758-b4293fd296a0",
    key="COL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magby.Name",
    display_name="Magby",
    searchable_by=["Magby", "Basic", "Magby"],
    subtypes=["Basic"],
    collector_number=46,
    set_code="COL",
    rarity=Rarities.Uncommon,
    hp=30,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=240,
    abilities=[
        Ability(
            title="Sweet Sleeping Face",
            game_text="As long as Magby is Asleep, prevent all damage done to Magby by attacks.",
            passive=_sleeping_face,
        ),
        Attack(
            title="Play with Fire",
            game_text="The Defending Pok\u00e9mon is now Burned. Magby is now Asleep.",
            cost={},
            effect=unimplemented,
        ),
    ],
)