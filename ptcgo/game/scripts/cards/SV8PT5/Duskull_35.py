from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e726b1b9-4800-5d68-bafd-b4a3b7b3ab25",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Duskull.Name",
    display_name="Duskull",
    searchable_by=["Duskull", "Basic", "Duskull"],
    subtypes=["Basic"],
    collector_number=35,
    set_code="SV8PT5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=355,
    abilities=[
        Attack(
            title="Come and Get You",
            game_text="Put up to 3 Duskull from your discard pile onto your Bench.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Mumble",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=30,
        ),
    ],
)