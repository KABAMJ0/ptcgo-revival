from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bf817701-21eb-5f38-b0e5-f39c6e14a220",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zacian.Name",
    display_name="Zacian",
    searchable_by=["Zacian", "Basic", "Zacian"],
    subtypes=["Basic"],
    collector_number=45,
    set_code="ME2",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=888,
    abilities=[
        Attack(
            title="Limit Break",
            game_text="If your opponent has 3 or fewer Prize cards remaining, this attack does 90 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)