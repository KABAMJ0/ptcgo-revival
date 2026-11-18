from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0d305f42-0586-5726-9579-04f7a0c7e21b",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snorunt.Name",
    display_name="Snorunt",
    searchable_by=["Snorunt", "Basic", "Snorunt"],
    subtypes=["Basic"],
    collector_number=37,
    set_code="SV4",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=361,
    abilities=[
        Attack(
            title="Ice Shard",
            game_text="If your opponent's Active Pok\u00e9mon is a Fighting Pok\u00e9mon, this attack does 30 more damage.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)