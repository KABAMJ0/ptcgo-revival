from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a276b41a-0dd1-5cee-abbb-c386947e7896",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lycanrocex.Name",
    display_name="Lycanroc ex",
    searchable_by=["Lycanroc ex", "Stage 1", "ex", "Lycanrocex"],
    subtypes=["Stage 1", "ex"],
    collector_number=241,
    set_code="SV2",
    rarity=Rarities.Rare,
    hp=260,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rockruff.Name",
    family_id=744,
    abilities=[
        Attack(
            title="Rock Throw",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
        ),
        Attack(
            title="Scary Fangs",
            game_text="During your opponent's next turn, if this Pok\u00e9mon is damaged by an attack (even if it is Knocked Out), put 10 damage counters on the Attacking Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=140,
            effect=unimplemented,
        ),
    ],
)