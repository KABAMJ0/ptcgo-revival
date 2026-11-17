from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1d2ef931-e907-580e-a4a9-b7096b577ce1",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skeledirge.Name",
    display_name="Skeledirge",
    searchable_by=["Skeledirge", "Stage 2", "Skeledirge"],
    subtypes=["Stage 2"],
    collector_number=38,
    set_code="SV1",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Crocalor.Name",
    family_id=909,
    abilities=[
        Attack(
            title="Passionate Singing",
            game_text="Attach up to 2 Basic Energy cards from your discard pile to your Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.FIRE: 1},
            damage=50,
            effect=unimplemented,
        ),
        Attack(
            title="Blazing Shout",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=unimplemented,
        ),
    ],
)