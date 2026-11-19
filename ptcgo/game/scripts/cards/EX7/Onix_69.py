from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_or_nothing

card = PokemonCardDef(
    guid="a5361734-1490-53f6-be8e-aa7107fe901a",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Onix.Name",
    display_name="Onix",
    searchable_by=["Onix", "Basic", "Onix"],
    subtypes=["Basic"],
    collector_number=69,
    set_code="EX7",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=95,
    abilities=[
        Attack(
            title="Horn Rush",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=flip_or_nothing(),
        ),
        Attack(
            title="Granite Head",
            game_text="During your opponent's next turn, any damage done to Onix by attacks is reduced by 10 (after applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
    ],
)