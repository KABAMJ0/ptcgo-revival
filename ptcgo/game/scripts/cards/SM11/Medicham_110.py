from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b98d8774-25a8-5d8e-ba8b-764df056420a",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Medicham.Name",
    display_name="Medicham",
    searchable_by=["Medicham", "Stage 1", "Medicham"],
    subtypes=["Stage 1"],
    collector_number=110,
    set_code="SM11",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meditite.Name",
    family_id=307,
    abilities=[
        Attack(
            title="Pure Power",
            game_text="Put 4 damage counters on your opponent's Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Master Strike",
            game_text="If this Pok\u00e9mon has a Karate Belt card attached to it, this attack does 60 more damage.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)