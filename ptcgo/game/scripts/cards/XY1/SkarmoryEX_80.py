from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import bonus_if, damage_counters_on
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="70ef0839-fc4e-5798-b068-4f8593cdde94",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SkarmoryEX.Name",
    display_name="Skarmory-EX",
    searchable_by=["Skarmory-EX", "Basic", "EX", "SkarmoryEX"],
    subtypes=["Basic", "EX"],
    collector_number=80,
    set_code="XY1",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=227,
    abilities=[
        Attack(
            title="Joust",
            game_text="Before doing damage, discard all Pok\u00e9mon Tool cards attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Tailspin Piledriver",
            game_text="If your opponent's Active Pok\u00e9mon already has any damage counters on it, this attack does 40 more damage.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=bonus_if(lambda ctx: damage_counters_on("defender")(ctx) > 0, 40),
        ),
    ],
)