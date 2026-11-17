from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9440cda0-ad93-534b-b9e8-b7c5d94de23e",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FlareonE4.Name",
    display_name="Flareon E4",
    searchable_by=["Flareon E4", "Basic", "SP", "FlareonE4"],
    subtypes=["Basic", "SP"],
    collector_number=60,
    set_code="PL2",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=136,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Fire Tail Slap",
            game_text="Flip a coin. If tails, discard a Fire Energy attached to Flareon .",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=unimplemented,
        ),
    ],
)