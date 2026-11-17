from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d50293e8-65c3-54ca-b94b-ca127dce85ca",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ditto.Name",
    display_name="Ditto",
    searchable_by=["Ditto", "Basic", "Ditto"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="HGSS4",
    rarity=Rarities.Rare,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=132,
    abilities=[
        Ability(
            title="Dittobolic",
            game_text="The number of Benched Pok\u00e9mon your opponent can have is now 4. If your opponent has 5 Benched Pok\u00e9mon, your opponent must discard 1 of them and all cards attached to it.",
            effect=unimplemented,
        ),
        Attack(
            title="Sharp Point",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)