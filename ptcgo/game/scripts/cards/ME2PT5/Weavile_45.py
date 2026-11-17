from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6c6de298-a593-5039-b6b1-65db7e063c8c",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weavile.Name",
    display_name="Weavile",
    searchable_by=["Weavile", "Stage 1", "Weavile"],
    subtypes=["Stage 1"],
    collector_number=45,
    set_code="ME2PT5",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sneasel.Name",
    family_id=215,
    abilities=[
        Attack(
            title="Slash",
            cost={PokemonTypes.WATER: 1},
            damage=40,
        ),
        Attack(
            title="Hail Claw",
            game_text="Discard all Energy from this Pok\u00e9mon. Your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 2},
            damage=70,
            effect=unimplemented,
        ),
    ],
)