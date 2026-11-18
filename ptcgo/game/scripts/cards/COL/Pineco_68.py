from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="88865fb5-608d-5906-8242-2bda1c592e24",
    key="COL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pineco.Name",
    display_name="Pineco",
    searchable_by=["Pineco", "Basic", "Pineco"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="COL",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=204,
    abilities=[
        Attack(
            title="Focus Energy",
            game_text="During your next turn, Pineco's Surprise Attack attack's base damage is 80.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Surprise Attack",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=unimplemented,
        ),
    ],
)