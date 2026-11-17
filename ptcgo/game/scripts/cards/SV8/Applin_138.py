from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f7a8b18c-e967-5d92-aaa1-40ea398c9eea",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Applin.Name",
    display_name="Applin",
    searchable_by=["Applin", "Basic", "Applin"],
    subtypes=["Basic"],
    collector_number=138,
    set_code="SV8",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=840,
    abilities=[
        Attack(
            title="Nutrients",
            game_text="Heal 30 damage from 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Trip Over",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIRE: 1},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)