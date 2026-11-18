from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d927c7b8-6d61-5dc9-933c-75bd1322f34a",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shroodle.Name",
    display_name="Shroodle",
    searchable_by=["Shroodle", "Basic", "Shroodle"],
    subtypes=["Basic"],
    collector_number=189,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=50,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=944,
    abilities=[
        Attack(
            title="Berry Search",
            game_text="Put a Basic Energy card from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Scratch",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
    ],
)