from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="360cfe6c-671d-5ad4-af23-6fb5e6f199fd",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Frillish.Name",
    display_name="Frillish",
    searchable_by=["Frillish", "Basic", "Frillish"],
    subtypes=["Basic"],
    collector_number=126,
    set_code="RSV10PT5",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=592,
    abilities=[
        Attack(
            title="Oceanic Gloom",
            game_text="During your opponent's next turn, they can't play any Item cards from their hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            effect=unimplemented,
        ),
    ],
)