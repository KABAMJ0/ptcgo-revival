from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1cfb67c5-41d1-5027-97ca-7d76dffd7a69",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Larvitar.Name",
    display_name="Larvitar",
    searchable_by=["Larvitar", "Basic", "Larvitar"],
    subtypes=["Basic"],
    collector_number=203,
    set_code="SV3",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=246,
    abilities=[
        Attack(
            title="Corkscrew Punch",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
        Attack(
            title="Confront",
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
        ),
    ],
)