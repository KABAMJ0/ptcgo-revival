from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6688c118-6989-5c56-8248-e28371b3fcff",
    key="MCD11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klink.Name",
    display_name="Klink",
    searchable_by=["Klink", "Basic", "Klink"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="MCD11",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=599,
    abilities=[
        Attack(
            title="Charge Beam",
            game_text="Flip a coin. If heads, attach an Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Irongrip",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)