from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3680077b-b553-5043-a43c-956b28509cc3",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Trubbish.Name",
    display_name="Trubbish",
    searchable_by=["Trubbish", "Basic", "Trubbish"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="RSV10PT5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=568,
    abilities=[
        Attack(
            title="Drool",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
        Attack(
            title="Sludge Bomb",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)