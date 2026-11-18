from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0fc4bb96-0d3a-5359-84bb-4ff9a78da586",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flabb.Name",
    display_name="Flabébé",
    searchable_by=["Flab\u00e9b\u00e9", "Basic", "Flabb"],
    subtypes=["Basic"],
    collector_number=84,
    set_code="SM6",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    family_id=669,
    abilities=[
        Attack(
            title="Secret Blessings",
            game_text="Shuffle 3 in any combination of Pok\u00e9mon and basic Energy cards from your discard pile into your deck.",
            cost={PokemonTypes.FAIRY: 1},
            effect=unimplemented,
        ),
    ],
)