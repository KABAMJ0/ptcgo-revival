from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="46c5d73b-757c-5389-9d1a-761786fbf469",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Palkia.Name",
    display_name="Palkia",
    searchable_by=["Palkia", "Basic", "Palkia"],
    subtypes=["Basic"],
    collector_number=136,
    set_code="SV8",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=484,
    abilities=[
        Attack(
            title="Space Crash",
            game_text="This attack does 40 damage for each Basic Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.WATER: 1},
            damage=40,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)