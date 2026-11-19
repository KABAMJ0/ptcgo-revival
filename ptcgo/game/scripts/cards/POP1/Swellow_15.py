from ptcgo.game.card_effects.passives_common import flip_protection
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a6596264-d3fb-517f-97c4-edd73d67b8f0",
    key="POP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swellow.Name",
    display_name="Swellow",
    searchable_by=["Swellow", "Stage 1", "Swellow"],
    subtypes=["Stage 1"],
    collector_number=15,
    set_code="POP1",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Taillow.Name",
    family_id=277,
    abilities=[
        Attack(
            title="Focus Energy",
            game_text="During your next turn, base damage of Swellow's Agility is 70 instead of 30.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Agility",
            game_text="Flip a coin. If heads, prevent all effects of an attack, including damage, done to Swellow during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=flip_protection(effects_too=True),
        ),
    ],
)