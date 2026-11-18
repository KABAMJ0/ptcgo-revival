from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6ad9f54b-9a7a-5aac-abc4-2998371d8e60",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gulpin.Name",
    display_name="Gulpin",
    searchable_by=["Gulpin", "Basic", "Gulpin"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="PL4",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=316,
    abilities=[
        Attack(
            title="Endure",
            game_text="Flip a coin. If heads, during your opponent's next turn, if Gulpin would be Knocked Out by damage from an attack, Gulpin is not Knocked Out and its remaining HP becomes 10 instead.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Pound",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)