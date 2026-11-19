from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_choice

card = PokemonCardDef(
    guid="639594dd-7ceb-5222-8d74-7bfe0e8f0c11",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasAbra.Name",
    display_name="Sabrina's Abra",
    searchable_by=["Sabrina's Abra", "Basic", "SabrinasAbra"],
    subtypes=["Basic"],
    collector_number=94,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=63,
    abilities=[
        Attack(
            title="Psyscan",
            game_text="Look at your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 20 more damage; if tails, this attack does 10 damage.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            damage_operator="+",
            effect=flip_choice(heads=30, tails=10),
        ),
    ],
)