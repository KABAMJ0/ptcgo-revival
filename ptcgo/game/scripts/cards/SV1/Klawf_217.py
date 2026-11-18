from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="529cc4f1-b37e-5978-9646-5ad45359df43",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klawf.Name",
    display_name="Klawf",
    searchable_by=["Klawf", "Basic", "Klawf"],
    subtypes=["Basic"],
    collector_number=217,
    set_code="SV1",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=950,
    abilities=[
        Attack(
            title="Vise Grip",
            cost={PokemonTypes.FIGHTING: 2},
            damage=50,
        ),
        Attack(
            title="Adrenaline Hammer",
            game_text="This Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=130,
            effect=unimplemented,
        ),
    ],
)