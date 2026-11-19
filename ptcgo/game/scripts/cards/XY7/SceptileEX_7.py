from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import bonus_if, defender_has_any_condition
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="41a3579d-5239-501a-8834-cbc90d33f6d5",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SceptileEX.Name",
    display_name="Sceptile-EX",
    searchable_by=["Sceptile-EX", "Basic", "EX", "SceptileEX"],
    subtypes=["Basic", "EX"],
    collector_number=7,
    set_code="XY7",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=254,
    abilities=[
        Attack(
            title="Sleep Poison",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Asleep and Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Unseen Claw",
            game_text="If your opponent's Active Pok\u00e9mon is affected by a Special Condition, this attack does 70 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=bonus_if(defender_has_any_condition, 70),
        ),
    ],
)