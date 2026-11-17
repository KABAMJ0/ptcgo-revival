from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="766e8458-4070-5df4-9ae1-0526fe714dd8",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aipom.Name",
    display_name="Aipom",
    searchable_by=["Aipom", "Basic", "Aipom"],
    subtypes=["Basic"],
    collector_number=211,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=190,
    abilities=[
        Attack(
            title="Filch",
            game_text="Draw a card.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Smack",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)