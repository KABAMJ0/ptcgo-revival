from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import damage_counters_on, damage_per

from ptcgo.game.card_effects.passives_common import prevent_damage_when


def _invisible_wall(calc, carrier):
    return calc.target is not None and calc.target is carrier and calc.amount >= 30


_wall = prevent_damage_when(_invisible_wall, attacks_only=True, any_side=True)

card = PokemonCardDef(
    guid="c7e79044-0207-5529-bcb0-fac65cd34471",
    key="BASE2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MrMime.Name",
    display_name="Mr. Mime",
    searchable_by=["Mr. Mime", "Basic", "MrMime"],
    subtypes=["Basic"],
    collector_number=22,
    set_code="BASE2",
    rarity=Rarities.Rare,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=122,
    abilities=[
        Ability(
            title="Invisible Wall",
            game_text="Whenever an attack (including your own) does 30 or more damage to Mr. Mime (after applying Weakness and Resistance), prevent that damage. (Any other effects of attacks still happen.) This power can't be used if Mr. Mime is Asleep, Confused, or Paralyzed.",
            passive=_wall,
        ),
        Attack(
            title="Meditate",
            game_text="Does 10 damage plus 10 more damage for each damage counter on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=damage_per(damage_counters_on("defender"), 10, base=10),
        ),
    ],
)