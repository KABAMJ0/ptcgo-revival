from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5c3f338e-78df-5f09-87bb-8d8e1c99326a",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowking.Name",
    display_name="Slowking",
    searchable_by=["Slowking", "Stage 1", "Slowking"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="SM3",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    family_id=199,
    abilities=[
        Attack(
            title="Drift Ashore",
            game_text="Search your deck for a card and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Unarmed",
            game_text="If you have no cards in your hand, ignore all Energy in this attack's cost.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=110,
            effect=unimplemented,
        ),
    ],
)