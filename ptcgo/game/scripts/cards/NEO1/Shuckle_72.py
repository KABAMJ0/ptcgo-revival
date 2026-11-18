from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

card = PokemonCardDef(
    guid="f8b3fb24-fdb4-5fc6-94a0-8ed0b524853c",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shuckle.Name",
    display_name="Shuckle",
    searchable_by=["Shuckle", "Basic", "Shuckle"],
    subtypes=["Basic"],
    collector_number=72,
    set_code="NEO1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=213,
    abilities=[
        Attack(
            title="Withdraw",
            game_text="Flip a coin. If heads, prevent all damage done to Shuckle during your opponent's next turn. (Any other effects of attacks still happen.)",
            cost={PokemonTypes.GRASS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Wrap",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 2},
            damage=20,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)